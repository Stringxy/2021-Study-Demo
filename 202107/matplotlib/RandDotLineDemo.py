import matplotlib.pyplot as plt
import random
import matplotlib.font_manager as fm

if __name__ == "__main__":
    x = range(0,120)
    y = [random.randint(0,40) for i in range(120)]
    plt.figure(figsize=(20,8))
    plt.plot(x,y)
    #设置x轴时间刻度
    _x = list(x)[::5]
    _xtick_labels_ = ["10点{}分".format(i) for i in range(60)]
    _xtick_labels_ += ["11点{}分".format(i) for i in range(60)]
    # 设置中文显示
    my_font = fm.FontProperties(fname = "/System/Library/Fonts/PingFang.ttc")
    plt.xticks(_x,_xtick_labels_[::5],rotation=270,fontproperties=my_font)

    #添加描述信息
    plt.xlabel("time",fontproperties=my_font)
    plt.ylabel("温度",fontproperties=my_font)
    plt.title("气温变化情况",fontproperties=my_font)
    plt.show()
