# ============================================================
#  phishing_decision_tree.py  -  teach a computer to smell a scam
#  Ansh - this is your flagship. It's a tiny "machine-learning" model:
#  we show it lots of example URLs already labelled "phishing" or
#  "safe", it finds the patterns by itself, then it can guess on URLs
#  it has never seen before.
# ============================================================
#  A "decision tree" is just a flowchart of yes/no questions the
#  computer builds for itself - e.g. "is the URL very long?",
#  "does it use an IP address instead of a name?".
#
#  pip install scikit-learn
#  You also need dataset.csv: 30 number-features per URL, and a label
#  in the last column (1 = phishing, -1 = safe). Get it from the
#  npapernot/phishing-detection repo I learned this from.
import csv
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def load(path="dataset.csv"):
    # Each row = 30 numbers describing a URL, then the answer.
    X, y = [], []                 # X = the clues, y = the answers
    for row in csv.reader(open(path)):
        *features, label = map(int, row)
        X.append(features)
        y.append(label)
    return X, y


if __name__ == "__main__":
    X, y = load()

    # Learn from 80% of the examples, then TEST on the other 20% the
    # model has never seen - that's how we prove it actually learned,
    # instead of just memorising.
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=1)

    # Build (train) the flowchart from the training examples.
    model = DecisionTreeClassifier().fit(Xtr, ytr)

    # How often is it right on the unseen test URLs?
    print("Accuracy on unseen URLs:", round(accuracy_score(yte, model.predict(Xte)), 3))
    # TODO (make it yours): swap DecisionTreeClassifier for
    # RandomForestClassifier and see if the accuracy climbs.
