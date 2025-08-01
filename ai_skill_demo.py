from transformers import pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
import torch
import tensorflow as tf
classifier = pipeline("sentiment-analysis")
print("Transformers result:", classifier("AI is revolutionizing the world!"))
iris = load_iris()
X, y = iris.data, iris.target
clf = LogisticRegression(max_iter=200)
clf.fit(X, y)
print("sklearn prediction:", clf.predict([X[0]]))
x = torch.tensor([1.0, 2.0, 3.0])
print("PyTorch tensor:", x * 2)
print("TensorFlow constant:", tf.constant([[42.0]]))
