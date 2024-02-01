import pandas as pd 
from itertools import chain
from collections import Counter
from itertools import chain
from myplot import get_stacked_plot

def get_unique(c_site,all_site):

    a_s = [j for j in all_site if j != c_site]
    print(len(a_s))
    a_s = list(set(chain.from_iterable(a_s)))
    print(len(a_s))
    op = [i for i in c_site if i not in a_s]
    return op


def get_overlaps(all_codes,sites, all_site):
    op_dict = dict()
    
    for j in range(0,len(all_codes)):
        pr_site = all_site[j]
        code = all_codes[j]
        common_si = len(set([si for si in sites if si in pr_site]))
        op_dict[code] = common_si

    op_dict = sorted(op_dict.items(), key=lambda x: x[1], reverse=True)

    return op_dict

df = pd.read_excel("TAOK1_S421_uudd_FET_5PMID_5ECCode_ratio10.xlsx", sheet_name=3)

df = df[["site2","Code"]]
df["Code"] = df["Code"].apply(lambda x:x.split(","))
df = df.explode("Code")
df = df.groupby("Code").agg(pd.Series.tolist).reset_index()

df["site2"] = df["site2"].apply(lambda x:list(set(x)))

all_site = df["site2"].tolist()

df["conut_site2"] = df["site2"].apply(lambda x:len(x))

df.sort_values(by=["conut_site2"], ascending = False, inplace = True)

all_codes = df["Code"].tolist()
all_sites = df["site2"].tolist()

df["overlaps"] = df.apply(lambda x:get_overlaps(all_codes, x["site2"], all_sites), axis = 1)


# df.to_excel("output.xlsx", index = False)

# get_stacked_plot(df)
