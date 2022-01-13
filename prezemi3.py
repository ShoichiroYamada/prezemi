import matplotlib.pyplot as plt

data = [
    [1452, 3231],
    [1796, 3747],
    [1894, 3726],
    [2584, 5853],
    [2735, 8866],
    [3447, 10913],
    ]


x, y = zip(*data)
plt.xlabel("オープンキャンパス参加者数(人)", fontname="MS Gothic")
plt.ylabel("志願者数(人)",fontname="MS Gothic")
plt.scatter(x, y)
plt.show()