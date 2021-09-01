import matplotlib.pyplot as plt

if __name__ == "__main__":
    y = [1, 2, 2, 3, 1, 4]
    x = range(1, 7)
    plt.figure(figsize=(20, 8))
    plt.scatter(x, y)
    plt.show()
