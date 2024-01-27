from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

import pandas as pd

data = {
    'Outlook': ['Rainy', 'Rainy', 'Overcast', 'Sunny', 'Sunny', 'Sunny', 'Overcast', 'Rainy', 'Rainy', 'Sunny', 'Rainy', 'Overcast', 'Overcast', 'Sunny'],
    'Temperature': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild', 'Cool', 'Mild', 'Mild', 'Mild', 'Hot', 'Mild'],
    'Humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'High'],
    'Windy': ['FALSE', 'TRUE', 'FALSE', 'FALSE', 'FALSE', 'TRUE', 'TRUE', 'FALSE', 'FALSE', 'FALSE', 'TRUE', 'TRUE', 'FALSE', 'TRUE'],
    'Play': ['NO', 'NO', 'YES', 'YES', 'YES', 'NO', 'YES', 'NO', 'YES', 'YES', 'YES', 'YES', 'YES', 'NO']
}

golf = pd.DataFrame(data)

# Convert categorical variables to numerical using Label Encoding
label_encoder = LabelEncoder()
for column in ['Outlook', 'Temperature', 'Humidity', 'Windy', 'Play']:
    golf[column] = label_encoder.fit_transform(golf[column])

# Combine the features and target variable
X = golf[['Outlook', 'Temperature', 'Humidity', 'Windy']]
y = golf['Play']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the Neural Network classifier
nn_classifier = MLPClassifier(hidden_layer_sizes=(10,), max_iter=1000, random_state=42)
nn_classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = nn_classifier.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)

print(f"Accuracy: {accuracy * 100:.2f}%")
