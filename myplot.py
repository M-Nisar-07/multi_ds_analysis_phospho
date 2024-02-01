# importing package
import matplotlib.pyplot as plt
import numpy as np
import time

def get_stacked_plot(df):

    cmap = plt.cm.get_cmap('tab20c', 50)

    colors = [cmap(i) for i in range(50)]

    color_list = ['#%02x%02x%02x' % (int(r * 255), int(g * 255), int(b * 255)) for r, g, b, _ in colors]


    x = df["Code"]
    over =df["overlaps"].tolist()

    data = list()
    data.append(df["conut_uniq"].tolist())

    index = 0
    for i in over:
        list(i.items())
        

    # print(len(data))

    # c_i = 0
    # for d in data:
    #     plt.bar(x, d, color=color_list[c_i])

    #     c_i += 1
    
    # plt.show()

    # y1 = np.array([10, 20, 10, 30])
    # y2 = np.array([20, 25, 15, 25])
    # y3 = np.array([12, 15, 19, 6])
    # y4 = np.array([10, 29, 13, 19])
    

    # plt.bar(x, y1, color='r')
    # plt.bar(x, y2, bottom=y1, color='b')
    # plt.bar(x, y3, bottom=y1+y2, color='y')
    # plt.bar(x, y4, bottom=y1+y2+y3, color='g')
    # plt.xlabel("Teams")
    # plt.ylabel("Score")
    # plt.legend(["Round 1", "Round 2", "Round 3", "Round 4"])
    # plt.title("Scores by Teams in 4 Rounds")
    # plt.show()