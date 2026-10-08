from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
import numpy as np

iris = load_iris()
X = iris.data      # 特征：花萼长/宽、花瓣长/宽（150×4）
y = iris.target    # 标签：0=setosa, 1=versicolor, 2=virginica

print("特征形状:", X.shape)   # (150, 4)
print("类别名称:", iris.target_names)

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.3,        # 30% 作为测试集
    random_state=42,      # 固定随机种子，保证结果可复现
    stratify=y            # 按类别比例分层抽样
)

clf = DecisionTreeClassifier(
    criterion='gini',     # 使用基尼系数作为分裂标准
    max_depth=3,          # 限制树深，防止过拟合
    random_state=42
)

clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print("预测结果:", y_pred)
print("真实标签:", y_test)

train_acc = clf.score(X_train, y_train)   # 训练集准确率
test_acc  = clf.score(X_test, y_test)     # 测试集准确率

print(f"训练集准确率: {train_acc:.4f}")
print(f"测试集准确率: {test_acc:.4f}")

print("accuracy_score 校验:", accuracy_score(y_test, y_pred))

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

fig, axes = plt.subplots(1, 2, figsize=(20, 7))

# --- 左图：决策树可视化 ---
plot_tree(
    clf,
    feature_names=iris.feature_names,
    class_names=iris.target_names,
    filled=True,
    rounded=True,
    ax=axes[0]              # 指定画到左子图
)
axes[0].set_title("Iris 决策树可视化", fontsize=14)

# --- 右图：特征重要程度柱状图 ---
importances = clf.feature_importances_
feature_names = iris.feature_names
indices = np.argsort(importances)[::-1]

bars = axes[1].bar(
    range(len(importances)),
    importances[indices],
    color='steelblue',
    edgecolor='black',
    align='center'
)

# 柱顶标数值
for bar, val in zip(bars, importances[indices]):
    axes[1].text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.005,
        f'{val:.3f}',
        ha='center', va='bottom', fontsize=10
    )

axes[1].set_xticks(range(len(importances)))
axes[1].set_xticklabels(
    [feature_names[i] for i in indices],
    rotation=15
)
axes[1].set_ylabel('重要程度 (Importance)')
axes[1].set_xlabel('特征')
axes[1].set_title("特征重要程度", fontsize=14)

plt.tight_layout()
plt.show() 