import pandas as pd
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from sklearn.utils.multiclass import type_of_target
import logging
import pickle

def transform_target(y):
    """Transform the continuous output into discrete classes."""
    bins = [-np.inf, -0.2, 0.2, np.inf]
    labels = ['Decrease', 'Maintain', 'Increase']
    y_class = pd.cut(y, bins=bins, labels=labels)
    return y_class

def test(mlp: MLPClassifier, data, target):
    y_pred = mlp.predict(data)
    y_pred = transform_target(y_pred)
    accuracy = accuracy_score(target, y_pred)
    logging.info(f"ACCURACY: {accuracy}")
    logging.info(f"Classification Report for Test Set:\n{classification_report(target, y_pred)}")
    logging.info(f"Confusion Matrix for Test Set:\n{confusion_matrix(target, y_pred)}")
    return y_pred


if __name__ == '__main__':
    LOG_LEVEL = logging.INFO
    # LOG_LEVEL = logging.DEBUG
    LEARN_DATA = 'data/TestResult-FSS_10_rng.csv'
    TEST_DATA = 'data/TestResult-FSS_rng.csv'

    logging.basicConfig(level=LOG_LEVEL, format='%(levelname)s: %(message)s')

    df_learn = pd.read_csv(LEARN_DATA)
    learn_data = df_learn[['MemoryUsage', 'ProcessorLoad', 'OutNetThroughput', 'OutBandwidth']]
    learn_target = df_learn['CLPVariation']

    df_test = pd.read_csv(TEST_DATA)
    data = df_test[['MemoryUsage', 'ProcessorLoad', 'OutNetThroughput', 'OutBandwidth']]
    target = df_test['CLPVariation']

    data_test, data_validate, target_test, target_validate = train_test_split(data, target, test_size=0.5, random_state=42)

    mlp = pickle.load(open('mlp.bin', 'rb'))

    test(mlp, learn_data, transform_target(learn_target))
    test(mlp, data_validate, transform_target(target_validate))
    test(mlp, data_test, transform_target(target_test))
