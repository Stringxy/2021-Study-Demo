import matplotlib.pyplot as plt

if __name__ == "__main__":
    # 用点绘制折线图
    x = range(2, 26, 2)
    print(x)
    y = [15, 13, 14.5, 17, 20, 25, 26, 26, 27, 22, 18, 15]
    # 设置图片大小(长宽)/dots per inch
    plt.figure(figsize=(20, 8), dpi=80)

    # 设置刻度
    # plt.xticks(range(2,26,1))
    # plt.xticks(x)
    _xtick_labels = [i / 2 for i in range(4, 49)]
    plt.xticks(_xtick_labels[::5])
    plt.yticks(range(min(y), max(y) + 1)[::2])
    plt.plot(x, y)

    # 保存图片
    plt.savefig("./dot-line.png")

    plt.show()
