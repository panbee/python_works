import matplotlib.pyplot as plt

from random_walk import RandomWalk


while True:
    
    rw = RandomWalk(50000)
    rw.fill_walk()

    # 设置绘图窗口大小尺寸
    plt.figure(figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)

    # 突出起点和终点
    plt.scatter(rw.x_values[0], rw.y_values[0], c='green', edgecolor='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=100)

    # 隐藏坐标轴
    plt.gca().xaxis.set_visible(False)
    plt.gca().yaxis.set_visible(False)
    # plt.gca().set_axis_off()
    # plt.axis('off')

    plt.show()

    keep_running = input("Make another walk?(y/n): ")
    if keep_running == 'n':
        break