import pandas as pd
import sklearn as sl
import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error
import logging

"""
- Training set: A set of examples used for learning, that is to fit the parameters of the classifier.

- Validation set: A set of examples used to tune the parameters of a classifier, for example to choose the number of hidden units in a neural network.

- Test set: A set of examples used only to assess the performance of a fully-specified classifier.
"""


def train(df: pd.DataFrame, hidden_layer_sizes=(1,)):
    x = df[['MemoryUsage', 'ProcessorLoad', 'OutNetThroughput', 'OutBandwidth']]
    y = df['CLPVariation']

    mlp = MLPRegressor(
        hidden_layer_sizes=hidden_layer_sizes,
        activation='logistic',
        solver='sgd',
        max_iter=1000,
        random_state=42
    )
    mlp.fit(x, y)
    return mlp

def test(mlp: MLPRegressor, df: pd.DataFrame):
    x = df[['MemoryUsage', 'ProcessorLoad', 'OutNetThroughput', 'OutBandwidth']]
    y = df['CLPVariation']

    y_pred = mlp.predict(x)
    mse = mean_squared_error(y, y_pred)
    return mse

if __name__ == '__main__':
    LOG_LEVEL = logging.INFO
    # LOG_LEVEL = logging.DEBUG
    # values linearly distributed
    LEARN_DATA = 'data/TestResult-FSS_10_rng.csv'
    # values linearly distributed that don't intersect with the learn data
    VALIDATE_DATA = 'data/TestResult-FSS_33_rng.csv'
    # truly random values
    TEST_DATA = 'data/TestResult-FSS_rng.csv'
    FIND_BEST_MATCH = False

    logging.basicConfig(level=LOG_LEVEL, format='%(levelname)s: %(message)s')

    df_learn = pd.read_csv(LEARN_DATA)
    df_validate = pd.read_csv(VALIDATE_DATA)
    df_test = pd.read_csv(TEST_DATA)

    if FIND_BEST_MATCH:
        hidden_layer_sizes = [(x,) for x in range(1, 11, 1)] + [(x, y) for x in range(1, 11, 1) for y in range(1, 11, 1)]
        min_mse = float('inf')
        best_neuron = None

        for hidden_layer_size in hidden_layer_sizes:
            mlp = train(df_learn, hidden_layer_size)
            mse = test(mlp, df_validate)
            if mse < min_mse:
                best_neuron = hidden_layer_size
                min_mse = mse
            logging.debug(f"Hidden Layer Size: {hidden_layer_size}, MSE: {mse}")
        logging.info(f"Best Hidden Layer Size: {best_neuron}, MSE: {min_mse}")

        mlp = train(df_learn, best_neuron)
        mse_test = test(mlp, df_test)
        logging.info(f"TEST MSE: {mse_test}")
    else:
        mlp = train(df_learn, (5,))
        mse_validate = test(mlp, df_validate)
        logging.info(f"VALIDATE MSE: {mse_validate}")
        mse_test = test(mlp, df_test)
        logging.info(f"TEST MSE: {mse_test}")
