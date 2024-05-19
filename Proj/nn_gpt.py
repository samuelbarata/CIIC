import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error

# Step 1: Generate some synthetic data for the example
# Note: In a real scenario, you would load your dataset here
np.random.seed(42)
X = np.random.rand(1000, 4)  # 100 samples, 4 features
y = np.random.rand(1000)     # 100 target values

# Step 2: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Define the MLPRegressor model
mlp = MLPRegressor(hidden_layer_sizes=(2000,), activation='logistic', solver='sgd', max_iter=1000, random_state=42)

# Step 4: Train the model
mlp.fit(X_train, y_train)

# Step 5: Test the model
y_pred = mlp.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Optionally, print predictions and true values
# print("Predicted values:", y_pred)
# print("True values:", y_test)
