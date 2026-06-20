# ml-phishing/ — flag phishing sites with machine learning (my favourite)

A small decision tree that learns to tell phishing URLs from real ones using 30 URL features. It learns from examples then guesses on URLs it's never seen.

Run:
```
pip install scikit-learn
python phishing_decision_tree.py
```
It uses the included `sample_dataset.csv` so it runs out of the box. The real dataset is the UCI one from the repo below.

Dataset + idea: github.com/npapernot/phishing-detection (UCI). The experiments are mine.
Make it mine (todo): try RandomForest and compare the accuracy; a "paste a URL -> predict" script.
