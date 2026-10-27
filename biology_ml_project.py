import pandas as pd
import gzip
from io import StringIO
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold, cross_val_score, cross_validate
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import classification_report
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# 读文件
file_path = "/Users/xiexuewumeng/昌平实验室/AI/MachinLearning/data/GSE2034_series_matrix.txt.gz"

with gzip.open(file_path, "rt") as f:
    lines = f.readlines()

# 查看样本信息
for line in lines:
    if line.startswith("!Sample_characteristics_ch1"):
        print(line[:300])

# 提取基因表达矩阵
start = lines.index("!series_matrix_table_begin\n")
end = lines.index("!series_matrix_table_end\n")

expression_text = "".join(lines[start + 1:end])

df = pd.read_csv(
    StringIO(expression_text),
    sep="\t",
    index_col=0
)

print(df.shape)
print(df.iloc[:5, :5])

# 行需要是样本，列是特征(gene)
X = df.T
print(X.shape)

metadata = [
    line for line in lines
    if line.startswith("!Sample_characteristics_ch1")
]

# 提取标签
import csv

fields = next(csv.reader(
    [metadata[0]], delimiter="\t"
))

labels = [
    int(x.split(":")[-1].strip())
    for x in fields[1:]
]

y = pd.Series(labels, index=X.index)

# 查看数据信息，样本量是否一致，然后y的标签是不是只有0和1
print("X:", X.shape)
print("y:", y.shape)
print(y.value_counts())

# 检查数据有无缺失值，并且X和y的索引是否一致
print(X.shape)
print(y.value_counts())
print(X.isna().sum().sum())

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# 训练逻辑回归模型
model = Pipeline([
    ("scaler", StandardScaler()),
    ("selector", SelectKBest(f_classif)), # 选择100个最重要的特征
    ("classifier", LogisticRegression(max_iter=2000))
])

    # 2. 定义超参数搜索空间
    #    这些是 RandomForest 的超参数，不是模型内部学到的参数
param_grid = {
    "classifier__C": [1000, 5000, 10000],        # 
    "selector__k": [50, 100, 200],       #
}

grid_search = GridSearchCV(
    estimator=model,
    param_grid=param_grid,
    cv=StratifiedKFold(n_splits=5, shuffle=True, random_state=42),                   # 5 折交叉验证
    scoring="f1",     # 以准确率作为评价标准
    n_jobs=-1,              # 使用所有可用 CPU 核心并行搜索
    verbose=1,
    refit=True,             # 找到最佳超参数后，用全部训练数据重新拟合
    )

    # 4. 执行网格搜索
grid_search.fit(X_train, y_train)

    # 5. 输出调优结果
print("=" * 60)
print("最佳超参数组合：", grid_search.best_params_)
print("最佳交叉验证分数：", grid_search.best_score_)
print("=" * 60)

    # 6. 在独立测试集上评估最终模型
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)
print("测试集分类报告：")
print(classification_report(
    y_test,
    y_pred,
    labels=[0, 1],
    target_names=["Negative", "Positive"],
    zero_division=0
))


