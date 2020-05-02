list = [58, 69, 23, 8, 26, 53]  # 创建一个列表
for i in range(len(list) - 1):  # 排序次数
    print("这是第{}次排序".format(i+1))     #打印排序次数
    for j in range(len(list) - i - 1):  # 比较次数
        print("这是第{}次对比".format(j+1))  #打印对比次数
        if list[j] > list[j + 1]:  # 对相邻的两个数做比较
            list[j], list[j + 1] = list[j + 1], list[j]  # 如果前面的数大于后面的数，则交换两个数的位置
print(list)  # 打印排序后的列表
