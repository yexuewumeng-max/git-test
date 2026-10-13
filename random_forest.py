from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()
X = iris.data      # 4维特征，花萼长宽，花瓣长宽
y = iris.target    # 标签：0=setosa, 1=versicolor, 2=virginica
print("样本数：", X.shape[0], "特征数：", X.shape[1])

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

#训练决策树
dt = DecisionTreeClassifier(random_state=42)
dt.fit(X_train, y_train) 
y_pred_dt = dt.predict(X_test)
acc_dt = accuracy_score(y_test, y_pred_dt)
print(f"决策树准确率: {acc_dt:.4f}")

rf = RandomForestClassifier(
    n_estimators=100,   # 树的数量
    random_state=42
)
rf.fit(X_train, y_train) 
y_pred_rf = rf.predict(X_test)  
acc_rf = accuracy_score(y_test, y_pred_rf)
print(f"随机森林准确率: {acc_rf:.4f}")

#比对结果
print(f"提升: {(acc_rf - acc_dt) * 100:.2f} 个百分点")