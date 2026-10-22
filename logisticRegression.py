# ============================================================
# Logistic Regression 标准化前后对比实验
# ============================================================
import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# ---------- 1. 准备数据 ----------
data = load_breast_cancer()
X, y = data.data, data.target
print(f"数据形状: {X.shape}, 特征数: {X.shape[1]}")
print(f"各特征数值范围差异很大，例如：")
print(f"  特征0 范围: {X[:,0].min():.2f} ~ {X[:,0].max():.2f}")
print(f"  特征1 范围: {X[:,1].min():.2f} ~ {X[:,1].max():.2f}")

# 划分训练集/测试集（先划分，再预处理！）
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)


# ============================================================
# 实验 A：不标准化，直接训练 Logistic Regression
# ============================================================
print("\n" + "="*50)
print("实验 A：不标准化")
print("="*50)

# TODO 1: 创建 Logistic Regression 模型
# 提示：LogisticRegression(max_iter=?, random_state=42)
# 注意 max_iter 要设大一点（比如 5000），否则可能不收敛
model_raw = LogisticRegression(max_iter=5000, random_state=42)  # TODO: 在这里填模型

# TODO 2: 在训练集上训练模型
# 提示：用 model_raw.fit(...)
model_raw.fit(X_train, y_train)  # TODO: 在这里填 fit 代码
# TODO: 在这里填 fit 代码

# 预测 & 评估
y_pred_raw = model_raw.predict(X_test)
acc_raw = accuracy_score(y_test, y_pred_raw)
print(f"测试集准确率: {acc_raw:.4f}")

# 交叉验证（更稳定的评估）
# TODO 3: 用 cross_val_score 做 5 折交叉验证
# 提示：cross_val_score(model_raw, X_train, y_train, cv=5)
cv_raw = cross_val_score(model_raw, X_train, y_train, cv=5) # TODO: 在这里填交叉验证代码
print(f"5折交叉验证准确率: {cv_raw.mean():.4f} (+/- {cv_raw.std():.4f})")


# ============================================================
# 实验 B：标准化 + Logistic Regression（用 Pipeline 防泄漏）
# ============================================================
print("\n" + "="*50)
print("实验 B：标准化 + Logistic Regression（Pipeline）")
print("="*50)

# TODO 4: 构建 Pipeline
# 提示：Pipeline([('scaler', StandardScaler()), ('lr', LogisticRegression(max_iter=5000, random_state=42))])
# 注意：步骤名 'scaler' 和 'lr' 后面调参要用到
pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('Lr', LogisticRegression(max_iter=5000, random_state=42))
    ])
                # TODO: 在这里填 Pipeline

# TODO 5: 在训练集上训练 Pipeline
# 提示：pipe.fit(X_train, y_train)
# TODO: 在这里填 fit 代码
pipe.fit(X_train, y_train)
# 预测 & 评估
y_pred_scaled = pipe.predict(X_test)
acc_scaled = accuracy_score(y_test, y_pred_scaled)
print(f"测试集准确率: {acc_scaled:.4f}")

# TODO 6: 对 Pipeline 做 5 折交叉验证
# 提示：cross_val_score(pipe, X_train, y_train, cv=5)
cv_scaled = cross_val_score(pipe, X_train, y_train, cv=5)# TODO: 在这里填交叉验证代码
print(f"5折交叉验证准确率: {cv_scaled.mean():.4f} (+/- {cv_scaled.std():.4f})")


# ============================================================
# 实验 C：对比结果 + 观察收敛速度
# ============================================================
print("\n" + "="*50)
print("对比总结")
print("="*50)
print(f"{'方法':<25}{'测试准确率':<15}{'CV均值':<12}{'CV标准差':<12}")
print(f"{'不标准化':<25}{acc_raw:<15.4f}{cv_raw.mean():<12.4f}{cv_raw.std():<12.4f}")
print(f"{'标准化(Pipeline)':<25}{acc_scaled:<15.4f}{cv_scaled.mean():<12.4f}{cv_scaled.std():<12.4f}")

# TODO 7（思考题，不用写代码）：
# 1. 两者准确率差多少？为什么 Logistic Regression 对标准化没有
#    像 KNN 那样"天翻地覆"的变化？
# 2. 看看训练时有没有 ConvergenceWarning？标准化前后收敛速度
#    （迭代次数）有什么差别？可以试试把 max_iter 调小到 100 再跑一次对比。
# 3. 把模型换成 KNeighborsClassifier，重复上面的实验，差异会更大吗？为什么？