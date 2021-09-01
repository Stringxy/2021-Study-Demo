import matplotlib.pyplot as plt
import random
import matplotlib.font_manager as fm

if __name__ == "__main__":
    x = ["电影1","电影2","电影3","电影4","电影5"]
    y = [20,5,10,2,100]
    plt.figure(figsize=(20,8))
    # plt.bar(range(len(x)),y,width=0.3)
    plt.barh(range(len(x)),y,height=0.3,color="orange")
    #设置x轴时间刻度
    _x = range(len(x))
    # 设置中文显示
    my_font = fm.FontProperties(fname = "/System/Library/Fonts/PingFang.ttc")
    # plt.xticks(_x, x, fontproperties=my_font)
    plt.yticks(_x,x,fontproperties=my_font)
    # 背景网格
    plt.grid(alpha=0.3)
    #添加描述信息
    plt.xlabel("电影",fontproperties=my_font)
    plt.ylabel("票房",fontproperties=my_font)
    plt.title("电影票房柱状图",fontproperties=my_font)
    plt.show()
