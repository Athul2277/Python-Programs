
actual = [1, 0, 1, 1, 0, 1, 0, 0]
predicted = [1, 0, 1, 0, 0, 1, 1, 0]

correct = sum(a == p for a, p in zip(actual, predicted))
accuracy = correct / len(actual) * 100

print("Total Predictions:", len(actual))
print("Correct Predictions:", correct)
print("Incorrect Predictions:", len(actual) - correct)
print("Model Accuracy:", round(accuracy, 2), "%")
