# phishing_decision_tree.py - teach a computer to smell a scam
# this is the part i like most. its a tiny machine-learning model: i show
# it lots of example urls already labelled phishing or safe, it finds the
# patterns by itself, then it can guess on urls its never seen.
#
# a "decision tree" is basically a flowchart of yes/no questions the
# computer builds for itself - like "is the url super long?", "does it
# use an ip address instead of a name?". still kinda amazed it works.
#
# pip install scikit-learn
# needs a csv: 30 number-features per url + a label in the last column
# (1 = phishing, -1 = safe). a small sample_dataset.csv is included so
# you can just run it; the real one is the UCI set from the repo below.
import csv
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def load(path="sample_dataset.csv"):
    X, y = [], []                  # X = the clues, y = the answers
    for row in csv.reader(open(path)):
        *features, label = map(int, row)
        X.append(features)
        y.append(label)
    return X, y


if __name__ == "__main__":
    X, y = load()

    # learn from 80%, TEST on the other 20% the model never saw - thats
    # how i prove it actually learned instead of just memorising.
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=1)

    model = DecisionTreeClassifier().fit(Xtr, ytr)   # build the flowchart

    print("Accuracy on unseen URLs:", round(accuracy_score(yte, model.predict(Xte)), 3))
    # todo (make it mine): swap to RandomForestClassifier and see if the
    # accuracy climbs, and write a "paste a url -> predict" mini script.
