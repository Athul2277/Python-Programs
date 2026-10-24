
from collections import Counter
import re

reviews = [
    "great product and great service",
    "poor product quality",
    "excellent customer service",
    "great delivery experience"
]

words = re.findall(r"\b[a-z]+\b", " ".join(reviews).lower())
frequency = Counter(words)

for word, count in frequency.most_common(5):
    print(word, "-", count)
