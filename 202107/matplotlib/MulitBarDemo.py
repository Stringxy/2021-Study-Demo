import matplotlib.pyplot as plt
import random
import matplotlib.font_manager as fm

if __name__ == "__main__":
    # 设置中文显示
    my_font = fm.FontProperties(fname = "/System/Library/Fonts/PingFang.ttc")
    x = ["电影1","电影2","电影3","电影4","电影5"]
    y1 = [20,5,10,2,100]
    y2 = [15, 7, 12, 1, 80]
    y3 = [10, 3, 5, 1, 50]

    bar_width = 0.2

    x1 = list(range(len(x)))
    x2 = [i+bar_width for i in x1]
    x3 = [i+bar_width*2 for i in x1]


    plt.figure(figsize=(20,8))
    plt.bar(range(len(x)),y1,width=bar_width,label="14日")
    plt.bar(x2, y2, width=bar_width, label="15日")
    plt.bar(x3, y3, width=bar_width, label="16日")

    plt.legend(prop=my_font)

    #设置x轴时间刻度
    _x = range(len(x))

    plt.xticks(x2, x, fontproperties=my_font)
    # 背景网格
    plt.grid(alpha=0.3)
    #添加描述信息
    plt.xlabel("电影",fontproperties=my_font)
    plt.ylabel("票房",fontproperties=my_font)
    plt.title("电影票房柱状图",fontproperties=my_font)
    plt.show()
