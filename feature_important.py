import pandas as pd
import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import permutation_importance
from sklearn.model_selection import train_test_split

# 1. 加载数据并加入随机特征（模拟真实世界的干扰项）
X, y = fetch_openml("titanic", version=1, as_frame=True, return_X_y=True)
rng = np.random.RandomState(42)
X['random_num'] = rng.randn(X.shape[0])  # 纯随机数值 X.shape是一个元组，分别是行，列，所以X.shape[0]是行数，X.shape[1]是列数.
X['random_cat'] = rng.randint(3, size=X.shape[0])  # 纯随机类别

# 只保留简单的几列方便演示
cols = ['pclass', 'sex', 'age', 'fare', 'random_num', 'random_cat']
X = pd.get_dummies(X[cols], dummy_na=True)  # 简单处理一下类别变量，pd.get_dummies(...)：把类别变量转成“独热编码”（one-hot）
y = (y == '1').astype(int)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. 训练模型
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# 3. 计算 Permutation Importance（关键：在测试集上算！）
result = permutation_importance(
    rf, X_test, y_test,
    n_repeats=10,      # 每个特征打乱10次，取平均，结果更稳
    random_state=42,
    n_jobs=-1
)

# 4. 整理并查看结果
imp_df = pd.DataFrame({
    'feature': X.columns,
    'importance_mean': result.importances_mean,
    'importance_std': result.importances_std
}).sort_values('importance_mean', ascending=False)

print(imp_df)