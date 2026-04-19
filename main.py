import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report

# 1. Load Data
iris = datasets.load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names
target_names = iris.target_names

# 2. Split Data (80% Training, 20% Testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Model Naive Bayes (Gaussian)
nb_model = GaussianNB()
nb_model.fit(X_train, y_train)
nb_predictions = nb_model.predict(X_test)
nb_accuracy = accuracy_score(y_test, nb_predictions)

# 4. Model Decision Tree
dt_model = DecisionTreeClassifier(random_state=42)
dt_model.fit(X_train, y_train)
dt_predictions = dt_model.predict(X_test)
dt_accuracy = accuracy_score(y_test, dt_predictions)

# 5. Output Hasil di Terminal
print("=== PERBANDINGAN MODEL MACHINE LEARNING ===")
print(f"Dataset: Iris (Klasifikasi Spesies Bunga)")
print(f"Akurasi Naive Bayes   : {nb_accuracy * 100:.2f}%")
print(f"Akurasi Decision Tree : {dt_accuracy * 100:.2f}%")
print("\nLaporan Klasifikasi Naive Bayes:\n", classification_report(y_test, nb_predictions, target_names=target_names))

# 6. Visualisasi
plt.figure(figsize=(12, 8))
plot_tree(dt_model, feature_names=feature_names, class_names=target_names, filled=True, rounded=True)
plt.title("Visualisasi Decision Tree")
plt.savefig("visualisasi_tree.png")
print("Visualisasi berhasil disimpan sebagai 'visualisasi_tree.png'")
plt.show()
