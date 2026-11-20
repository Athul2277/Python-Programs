
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

data = pd.read_csv("news_dataset.csv").dropna()
model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(data["headline"], data["category"])
headline = input("Enter news headline: ")
category = model.predict([headline])[0]
print("Predicted category:", category)
