import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    # 绘制正弦余弦
    c, s = np.cos(x), np.sin(x)
    plt.figure(1)
    plt.title("cos&sin")
    plt.plot(x, c, color="blue", linewidth=1.0, linestyle="-", label="cos",alpha=0.5)
    plt.plot(x, s,"r*",label = "sin")
    #图表编辑器
    ax=plt.gca()
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")
    ax.spines["bottom"].set_position(("data",0))
    ax.spines["left"].set_position(("data",0))
    ax.xaxis.set_ticks_position("bottom")
    ax.yaxis.set_ticks_position("left")
    plt.xticks([-np.pi, -np.pi /2 ,0,np.pi/2,np.pi],
               [r'$-\pi$',r'$-\pi/2$',r'$0$',r'$+\pi/2$',r'$+\pi$'])
    plt.yticks(np.linspace(-1,1,5,endpoint=True))
    for label in ax.get_xticklabels()+ax.get_yticklabels():
        label.set_fontsize(16)
        label.set_bbox(dict(facecolor="white",edgecolor="None",alpha=0.2))
    plt.legend(loc="upper left")
    plt.grid()
    # 设置显示范围
    # plt.axis([-1,1,-0.5,1])
    plt.fill_between(x,np.abs(x)<0.5,c,c>0.5,color="yellow",alpha=0.4)
    plt.show()
