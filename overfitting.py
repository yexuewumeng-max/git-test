import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

X, y = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

print(f"{'max_depth':>10} {'train_acc':>10} {'test_acc':>10} {'gap':>8} {'leaves':>7}")
print("-" * 50)
for depth in [1, 2, 3, 4, 5, 6, 8, 10, None]:
    clf = DecisionTreeClassifier(max_depth=depth, random_state=42)
    clf.fit(X_train, y_train)
    tr = accuracy_score(y_train, clf.predict(X_train))
    te = accuracy_score(y_test, clf.predict(X_test))
    label = str(depth) if depth is not None else "None"
    print(f"{label:>10} {tr:>10.3f} {te:>10.3f} {tr-te:>8.3f} {clf.get_n_leaves():>7}")