import pandas as pd 
from itertools import chain
from collections import Counter

df = pd.read_excel("TAOK1_S421_uudd_FET_5PMID_5ECCode_ratio10.xlsx", sheet_name=3)

df["Code"] = df["Code"].apply(lambda x:x.split(','))

unique_li = df["Code"].tolist()
unique_li = list(chain.from_iterable(unique_li))

counts = Counter(unique_li)

for value, count in counts.items():
    print(f"{value}: {count} times")

df = pd.DataFrame(list(counts.items()), columns=['code', 'Count'])

df.sort_values(by=["Count"], inplace=True, ascending=False)


df.to_excel("final countdown.xlsx")
