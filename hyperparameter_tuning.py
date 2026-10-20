from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import classification_report


def main():
    # 1. 加载数据并划分训练集 / 测试集
    data = load_breast_cancer()
    X_train, X_test, y_train, y_test = train_test_split(
        data.data, data.target, test_size=0.2, random_state=42, stratify=data.target
    )

    # 2. 定义超参数搜索空间
    #    这些是 RandomForest 的超参数，不是模型内部学到的参数
    param_grid = {
        "n_estimators": [50, 100, 200],        # 森林中树的数量
        "max_depth": [None, 10, 20, 30],       # 树的最大深度，None 表示不限
        "min_samples_split": [2, 5, 10],       # 内部节点再划分所需的最小样本数
    }

    # 3. 初始化随机森林与 GridSearchCV
    rf = RandomForestClassifier(random_state=42)

    grid_search = GridSearchCV(
        estimator=rf,
        param_grid=param_grid,
        cv=5,                   # 5 折交叉验证
        scoring="accuracy",     # 以准确率作为评价标准
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
    print(classification_report(y_test, y_pred, target_names=data.target_names))


if __name__ == "__main__":
    main()