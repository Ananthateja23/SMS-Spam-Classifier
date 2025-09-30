import nltk

resources = ["punkt", "punkt_tab", "stopwords", "wordnet", "omw-1.4"]

for r in resources:
    nltk.download(r, quiet=True)
