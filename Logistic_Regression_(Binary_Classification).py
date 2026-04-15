from sklearn.linear_model import LogisticRegression
import numpy as np

X = np.array([[1],[2],[3],[4],[5],[6]])
y = [0,0,0,1,1,1]

model = LogisticRegression()
model.fit(X, y)

pred = model.predict([[3.5]])

print("Prediction:", pred[0])
print("Model trained")
