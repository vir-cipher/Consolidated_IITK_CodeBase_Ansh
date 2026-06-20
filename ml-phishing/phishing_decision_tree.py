"""
phishing_decision_tree.py - teach a computer to smell a scam.

this is the part i like most. its a tiny machine-learning model. i show it
lots of example URLs that are already labelled phishing or safe, it works out
the patterns by itself, and then it can guess on URLs its never seen before.

a "decision tree" is literally a flowchart of yes/no questions the computer
builds for itself from the data - stuff like "is the URL crazy long?", "does
it use a raw IP address instead of a domain name?", "is there an @ in it?".
each answer sends you down a branch until you land on phishing or safe. still
kinda amazed it figures out the questions on its own.

the data (sample_dataset.csv): each row is 30 numeric features describing one
URL, and the last column is the label (1 = phishing, -1 = safe). the features
are already turned into numbers - thats the classic UCI phishing dataset format.

pip install scikit-learn
"""
import csv
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def load(path="sample_dataset.csv"):
    """Load the dataset.

    Returns:
        X: list of feature-lists (the clues for each URL).
        y: list of labels (the answers: 1 phishing, -1 safe).
    """
    X, y = [], []
    for row in csv.reader(open(path)):
        *features, label = map(int, row)   # last value in the row is the label
        X.append(features)
        y.append(label)
    return X, y


if __name__ == "__main__":
    X, y = load()
    print("loaded", len(X), "labelled URLs, each with", len(X[0]), "features")

    # split: learn from 80%, TEST on the other 20% the model has never seen.
    # thats how i prove it actually learned the patterns instead of just
    # memorising the training rows.
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=1)

    model = DecisionTreeClassifier().fit(Xtr, ytr)   # build the flowchart

    acc = accuracy_score(yte, model.predict(Xte))
    print("Accuracy on unseen URLs:", round(acc, 3))

    # which clue did the tree lean on most? (the headline question at the top
    # of its flowchart - higher number = more important.)
    importances = model.feature_importances_
    top = max(range(len(importances)), key=lambda i: importances[i])
    print("most useful single feature: column", top)

    # one concrete prediction on a held-out URL, to make it real:
    guess = model.predict([Xte[0]])[0]
    print("example URL predicted:", "PHISHING" if guess == 1 else "safe",
          "| actually:", "PHISHING" if yte[0] == 1 else "safe")
    # todo (make it mine): swap to RandomForestClassifier and see if accuracy
    # climbs, then write a "paste a url -> features -> predict" mini script.
