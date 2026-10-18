import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

X, y = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# 模型训练随机森林
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# 模型逻辑回归
LR = LogisticRegression(max_iter=10000, random_state=42)
LR.fit(X_train, y_train)

# 模型预测
y_pred_rf = rf.predict(X_test)
y_pred_LR = LR.predict(X_test)

# 模型评估
acc_rf = accuracy_score(y_test, y_pred_rf)
acc_LR = accuracy_score(y_test, y_pred_LR)
print(f"随机森林准确率: {acc_rf:.4f}")
print(f"逻辑回归准确率: {acc_LR:.4f}")




