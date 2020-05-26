import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


def plot_graph_loss(file_name, model_name):
    """ Plots validation and train loss

    :param file_name: name of the csv file containing values for validation and train loss functions
    :type file_name: str
    :param model_name: name of the model
    :type model_name: str
    :return: None
    """
    values = pd.read_table(file_name, sep=',')
    data = pd.DataFrame()
    data['epoch'] = list(values['epoch'].get_values() + 1) + list(values['epoch'].get_values() + 1)
    data['loss name'] = ['training'] * len(values) + ['validation'] * len(values)
    data['loss'] = list(values['loss'].get_values()) + list(values['val_loss'].get_values())
    sns.set(style='darkgrid', context='poster', font='Verdana')
    f, ax = plt.subplots()
    sns.lineplot(x='epoch', y='loss', hue='loss name', style='loss name', dashes=False, data=data, palette='Set2')
    ax.set_ylabel('Loss')
    ax.set_xlabel('Epoch')
    ax.legend().texts[0].set_text('')
    plt.title(model_name)
    plt.show()
