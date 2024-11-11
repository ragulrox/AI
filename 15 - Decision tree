from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def get_user_inputs():
    test_size = float(input())
    random_state = int(input())
    return test_size, random_state

def main():
    iris = load_iris()
    X = iris.data
    y = iris.target

    test_size, random_state = get_user_inputs()

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy:.2f}")

if _name_ == "_main_":
    main()
