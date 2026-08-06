import numpy as np

data = [[12, 8, 15],    # 第1天：苹果12个，香蕉8个，橙子15个
        [10, 9, 13],    # 第2天
        [14, 7, 11],    # 第3天
        [9, 11, 16]]    #第四天
sales = np.array(data)
print("原始销量数据：")
print(sales)

print(sales.shape)
print(sales.dtype)

sales_float = sales.astype(float)
print(sales_float.dtype)
print(sales_float)

sales_str = sales_float.astype('U10')
print(sales_str.dtype)
print(sales_str)

day3 = sales[2,]
print(f"\n第3天的销量: {day3}")

banana = sales[:,1] #列索引怎么写？
print(f"香蕉销量: {banana}")

days_2to4 = sales[1:3,]
print(f"第2-4天的销量:\n{days_2to4}")

specific = sales[(0,0),(0,2)]
print(f"第1天的苹果和橙子: {specific}")


sales[1, 1] = 10  # 请修改
print(f"\n修改后的数据：\n{sales}")

sales[3, :] = sales[3, :] + 2  # 请给第4行所有列加2
print(f"第4天加2后的数据：\n{sales}")

high_sales = sales[sales > 12]  # 请用布尔索引
print(f"\n销量>12的数据: {high_sales}")

equal_11 = sales[sales == 11]  # 请用布尔索引
print(f"销量等于11的数据: {equal_11}")