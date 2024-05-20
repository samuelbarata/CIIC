import pandas as pd
import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report, accuracy_score
from sklearn.utils.multiclass import type_of_target
import logging
import pickle

"""
- Training set: A set of examples used for learning, that is to fit the parameters of the classifier.

- Validation set: A set of examples used to tune the parameters of a classifier, for example to choose the number of hidden units in a neural network.

- Test set: A set of examples used only to assess the performance of a fully-specified classifier.
"""

def transform_target(y):
    """Transform the continuous output into discrete classes."""
    bins = [-np.inf, -0.2, 0.2, np.inf]
    labels = ['Decrease', 'Maintain', 'Increase']
    y_class = pd.cut(y, bins=bins, labels=labels)
    return y_class.cat.codes

def train(data, target, hidden_layer_sizes=(1,), transform_function=None):
    if transform_function is not None:
        target = transform_function(target)

    mlp = MLPRegressor(
        hidden_layer_sizes=hidden_layer_sizes,
        activation='relu',
        solver='adam',
        max_iter=2000,
        random_state=42
    )
    mlp.fit(data, target)
    return mlp

def test(mlp: MLPRegressor, data, target, transform_function=None):
    y_pred = mlp.predict(data)
    if transform_function is not None:
        target = transform_function(target)

    mse = mean_squared_error(target, y_pred)
    logging.info(f"MSE: {mse}")

    if transform_function:
        accuracy = accuracy_score(target, y_pred)
        logging.info(f"ACCURACY: {accuracy}")
        logging.info(f"Classification Report for Test Set:\n{classification_report(target, y_pred)}")
        logging.info(f"Confusion Matrix for Test Set:\n{confusion_matrix(target, y_pred)}")

    return y_pred

if __name__ == '__main__':
    LOG_LEVEL = logging.INFO
    # LOG_LEVEL = logging.DEBUG

    LEARN_DATA = 'data/TestResult-FSS_10_rng.csv'

    DATA_VALIDATE = 'data/data_validate.csv'
    TARGET_VALIDATE = 'data/target_validate.csv'

    DATA_TEST = 'data/data_test.csv'
    TARGET_TEST = 'data/target_test.csv'

    MLP_PATH = 'mlp.pickle'

    FIND_BEST_MATCH = False


    logging.basicConfig(level=LOG_LEVEL, format='%(levelname)s: %(message)s')

    df_learn = pd.read_csv(LEARN_DATA)
    learn_data = df_learn[['MemoryUsage', 'ProcessorLoad', 'OutNetThroughput', 'OutBandwidth']]
    learn_target = df_learn['CLPVariation']

    data_validate = pd.read_csv(DATA_VALIDATE)
    target_validate = pd.read_csv(TARGET_VALIDATE)

    data_test = pd.read_csv(DATA_TEST)
    target_test = pd.read_csv(TARGET_TEST)


    if FIND_BEST_MATCH:
        # Define the parameter grid
        parameter_grid = {
            'hidden_layer_sizes': [(x,) for x in range(1, 11, 1)] + [(x,y) for x in range(1,30,1) for y in range(1,11,1)],
            'activation': ['relu', 'identity', 'logistic', 'tanh'],
            'solver': ['lbfgs', 'sgd', 'adam'],
            'alpha': [0.0001],
            'learning_rate': ['constant'],
            'max_iter': [2000]
        }

        mlp = MLPRegressor(random_state=42)
        grid_search = GridSearchCV(mlp, parameter_grid, scoring='neg_mean_squared_error', cv=3, n_jobs=-1)


        grid_search.fit(learn_data, learn_target)
        logging.info(f"Best parameters found: {grid_search.best_params_}")

        # Evaluate the best model found by grid search
        best_mlp = grid_search.best_estimator_
        target_pred = best_mlp.predict(data_validate)
        mse = mean_squared_error(target_validate, target_pred)
        logging.info(f"Mean Squared Error with best parameters: {mse}")
    
    else:
        mlp = train(learn_data, learn_target, (8,3))
        with open(MLP_PATH, "wb") as file:
            pickle.dump(mlp, file)
        logging.info(f"VALIDATE MSE:")
        test(mlp, data_validate, target_validate)
        logging.info(f"TEST MSE:")
        test(mlp, data_test, target_test)
