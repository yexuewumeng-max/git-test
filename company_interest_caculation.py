import numpy as np
sales_data = np.array([
    [120, 85, 200, 45],  # 周一
    [115, 92, 180, 50],  # 周二
    [130, 78, 210, 42],  # 周三
    [125, 88, 195, 48],  # 周四
    [150, 95, 220, 55],  # 周五
    [210, 120, 280, 70], # 周六
    [180, 110, 250, 65]  # 周日
])

days = ['Mon','Tus','Wed','Thu','Fri','Sat','Sun']
categories = ['电子产品','服装','食品','日用品']

print(f"该数组的形状是：{sales_data.shape}")

print(f"每个商品在整个一周的总销售额是：{sales_data.sum(axis=0)},其中最高的是：{max(sales_data.sum(axis=0))}")
print(f"每一天所有品类的总销售额：{sales_data.sum(axis=1)}")
print(f"周六的总销售额比周一多{sales_data.sum(axis=1)[5]-sales_data.sum(axis=1)[0]}万元。")
print(f"单日单品类销售额的最高值：{sales_data.max()}")

if sales_data[0:5,].mean(axis=0)[1]-sales_data[5:7,].mean(axis=0)[1] < 0:
    print("周末服装销售额显著高于工作日。")
else:
    print("周末服装销售额没有显著高于工作日。")