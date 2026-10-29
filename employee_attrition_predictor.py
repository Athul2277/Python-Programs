
from sklearn.tree import DecisionTreeClassifier

features = [[1, 2], [5, 9], [2, 3], [6, 8], [1, 4]]
labels = [1, 0, 1, 0, 1]

model = DecisionTreeClassifier(random_state=42)
model.fit(features, labels)

employee = [[2, 3]]
prediction = model.predict(employee)[0]

print("Attrition Prediction:", "High Risk" if prediction == 1 else "Low Risk")
print("Prediction Completed")
