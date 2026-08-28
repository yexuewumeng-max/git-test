import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score

plt.rcParams['font.sans-serif'] = ['Heiti SC'] 
plt.rcParams['axes.unicode_minus'] = False

print("步骤1：读取数据")
print("="*50)

diabetes = load_diabetes()
df = pd.DataFrame(data=diabetes.data, columns=diabetes.feature_names)
df['disease_progression'] = diabetes.target

print(df.head(10))
print(df.shape)
print(df.columns)
print(df.describe())


print(df.isna().sum())  # 检查缺失值
count = (df['disease_progression'] > 300).sum()  # 统计病情进展值大于300的样本数量
print(f"病情进展值大于300的样本数量: {count}")
df_cleaned = df[df['disease_progression'] <= 300]  # 去除病情进展值大于300的异常样本

def bmi_iqr():
    Q1 = df_cleaned['bmi'].quantile(0.25)
    Q3 = df_cleaned['bmi'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return lower_bound, upper_bound

lower, upper = bmi_iqr()
bmi_outliers = df_cleaned[(df_cleaned['bmi'] < lower) | (df_cleaned['bmi'] > upper)]
print(f"正常范围: [{lower:.4f}, {upper:.4f}]")
print(f"BMI异常值数量: {len(bmi_outliers)} 个")
print(f"异常值:\n{bmi_outliers[['bmi', 'disease_progression']]}")

df_cleaned_features = df_cleaned.drop(columns=['disease_progression'])
X_train, X_test, y_train, y_test = train_test_split(df_cleaned_features, df_cleaned['disease_progression'], test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
print(X_train_scaled.shape)
print(X_test_scaled.shape)

#线性回归模型
lr_model = LinearRegression()
lr_model.fit(X_train_scaled, y_train)
lr_pred = lr_model.predict(X_test_scaled)

# 随机森林回归模型
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train_scaled, y_train)
rf_pred = rf_model.predict(X_test_scaled)

# 决策树回归模型
dt_model = DecisionTreeRegressor(random_state=42)
dt_model.fit(X_train_scaled, y_train)
dt_pred = dt_model.predict(X_test_scaled)

# 评估模型性能
for name, pred in [("线性回归", lr_pred), ("随机森林", rf_pred), ("决策树", dt_pred)]:
    mse = mean_squared_error(y_test, pred)
    r2 = r2_score(y_test, pred)
    print(f"{name}:")
    print(f"  MSE = {mse:.4f}")
    print(f"  R²  = {r2:.4f}")


new_data = X_test.iloc[:5].copy()
new_data_scaled = scaler.transform(new_data)
predictions = lr_model.predict(new_data_scaled)
print("新数据预测结果:")
for i, (idx, pred) in enumerate(zip(new_data.index, predictions)):
    print(f"样本 {i+1} (原索引 {idx}): disease_progression = {pred:.2f} ")

print("\n对比真实值:")
for i, idx in enumerate(new_data.index):
    print(f"样本 {i+1}: 预测={predictions[i]:.2f}, 真实={y_test.iloc[i]:.2f}")

fig, axes = plt.subplots(2, 3, figsize=(15, 10))
#直方图
axes[0, 0].hist(df['disease_progression'], bins=30, edgecolor='black', color='steelblue')
axes[0, 0].set_title('病情进展分布直方图')
axes[0, 0].set_xlabel('病情进展')
axes[0, 0].set_ylabel('target')
#散点图
axes[0, 1].scatter(df['bmi'], df['disease_progression'], alpha=0.6, color='darkorange')
axes[0, 1].plot([df['bmi'].min(), df['bmi'].max()], 
                [df['disease_progression'].min(), df['disease_progression'].max()], 'r--', lw=2)
axes[0, 1].set_xlabel('bmi')
axes[0, 1].set_ylabel('病情进展')
axes[0, 1].set_title('bmi vs 病情进展')
#散点图
axes[0, 2].scatter(y_test, lr_pred, alpha=0.6, color='darkorange')
axes[0, 2].plot([y_test.min(), y_test.max()], 
                [lr_pred.min(), lr_pred.max()], 'r--', lw=2)
axes[0, 2].set_xlabel('真实病情进展')
axes[0, 2].set_ylabel('预测病情进展')
axes[0, 2].set_title('线性回归: 预测 vs 真实')
#条形图
feature_vars = df.drop('disease_progression', axis=1).var().sort_values(ascending=True)

axes[1, 0].bar(df_cleaned['bmi'], df_cleaned['disease_progression'], color='steelblue', alpha=0.7)
axes[1, 0].barh(feature_vars.index, feature_vars.values, color='teal')
axes[1, 0].set_title('标准化前各特征的方差', fontsize=12)
axes[1, 0].set_xlabel('方差值')
axes[1, 0].set_ylabel('特征名称')
axes[1, 0].grid(axis='x', alpha=0.3)
for i, v in enumerate(feature_vars.values):
    axes[1, 0].text(v + 10, i, f'{v:.1f}', va='center', fontsize=9)

#条形图
# 在练习6的 (1,1) 位置
# 获取特征重要性
importances = rf_model.feature_importances_
feature_names = df_cleaned.columns[:-1]  # 或 df.columns[:-1]

# 创建DataFrame方便排序
feature_importance_df = pd.DataFrame({
    '特征': feature_names,
    '重要性': importances
}).sort_values('重要性', ascending=True)  # 升序排列，让最重要的在顶部

# 画水平条形图
axes[1, 1].barh(feature_importance_df['特征'], 
                feature_importance_df['重要性'], 
                color='coral')
axes[1, 1].set_title('随机森林特征重要性', fontsize=12)
axes[1, 1].set_xlabel('重要性分数')
axes[1, 1].set_ylabel('特征名称')
axes[1, 1].grid(axis='x', alpha=0.3)

# 在条形上显示数值
for i, v in enumerate(feature_importance_df['重要性']):
    axes[1, 1].text(v + 0.01, i, f'{v:.3f}', va='center', fontsize=9)

# 你练习4已经计算了这三个值
lr_mse = mean_squared_error(y_test, lr_pred)      # 线性回归
rf_mse = mean_squared_error(y_test, rf_pred)      # 随机森林
dt_mse = mean_squared_error(y_test, dt_pred)      # 决策树
# 在练习6的 (1,2) 位置
models = ['线性回归', '随机森林', '决策树']
mse_values = [lr_mse, rf_mse, dt_mse]
colors = ['#4CAF50', '#2196F3', '#FF5722']  # 绿、蓝、红

# 画柱状图
bars = axes[1, 2].bar(models, mse_values, color=colors, alpha=0.7)
axes[1, 2].set_title('三个模型MSE对比', fontsize=12)
axes[1, 2].set_ylabel('均方误差 (MSE)')
axes[1, 2].grid(axis='y', alpha=0.3)

# 在柱子上显示数值
for bar, value in zip(bars, mse_values):
    axes[1, 2].text(bar.get_x() + bar.get_width()/2, 
                    value + 50, 
                    f'{value:.1f}', 
                    ha='center', 
                    va='bottom',
                    fontsize=10)

plt.tight_layout()
plt.show()