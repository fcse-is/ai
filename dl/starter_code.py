import numpy as np


def read_dataset(file_path):
    """ Read the dataset and return the features and encoded classes

    :param file_path: path to the file that contains the dataset
    :type file_path: str
    :return: features and encoded classes
    :rtype: np.array, np.array
    """
    features = []
    classes = []
    with open(file_path) as f:
        _ = f.readline()
        while True:
            line = f.readline().strip()
            if line == '':
                break
            parts = line.split(';')
            features.append(list(map(float, parts[:-1])))
            classes.append(one_hot_encoding(int(parts[-1])))
    return np.array(features), np.array(classes)


def one_hot_encoding(sample):
    """ Encodes the ranking into class (with one-hot encoding)
    bad quality -> [1, 0, 0]
    medium quality -> [0, 1, 0]
    good quality -> [0, 0, 1]

    :param sample: one ranking value
    :type sample: int
    :return: one-hot encoded class
    :rtype: list(int)
    """
    if sample < 6:
        return [1, 0, 0]
    elif sample == 6:
        return [0, 1, 0]
    else:
        return [0, 0, 1]
