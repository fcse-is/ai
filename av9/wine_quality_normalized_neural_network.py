from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler, MinMaxScaler

from wine_quality_neural_network import read_dataset, divide_sets

if __name__ == '__main__':
    dataset = read_dataset()
    train_set, val_set, test_set = divide_sets(dataset)

    train_x = [x[:-1] for x in train_set]
    train_y = [x[-1] for x in train_set]
    val_x = [x[:-1] for x in val_set]
    val_y = [x[-1] for x in val_set]
    test_x = [x[:-1] for x in test_set]
    test_y = [x[-1] for x in test_set]

    scaler = StandardScaler()
    scaler.fit(train_x)
    scaler2 = MinMaxScaler()
    scaler2.fit(train_x)

    classifier = MLPClassifier(10, activation='relu', learning_rate_init=0.001, max_iter=500, random_state=0)
    classifier2 = MLPClassifier(10, activation='relu', learning_rate_init=0.001, max_iter=500, random_state=0)
    classifier3 = MLPClassifier(10, activation='relu', learning_rate_init=0.001, max_iter=500, random_state=0)

    classifier.fit(train_x, train_y)
    classifier2.fit(scaler.transform(train_x), train_y)
    classifier3.fit(scaler2.transform(train_x), train_y)

    val_acc1 = 0
    val_predictions = classifier.predict(val_x)
    for true, pred in zip(val_y, val_predictions):
        if true == pred:
            val_acc1 += 1

    val_acc1 = val_acc1 / len(val_y)

    print(f'Bez normalizacija imame tochnost so validacisko mnozestvo od {val_acc1}')

    val_acc2 = 0
    val_predictions = classifier2.predict(scaler.transform(val_x))
    for true, pred in zip(val_y, val_predictions):
        if true == pred:
            val_acc2 += 1

    val_acc2 = val_acc2 / len(val_y)

    print(f'So standardna normalizacija imame tochnost so validacisko mnozestvo od {val_acc2}')

    val_acc3 = 0
    val_predictions = classifier3.predict(scaler2.transform(val_x))
    for true, pred in zip(val_y, val_predictions):
        if true == pred:
            val_acc3 += 1

    val_acc3 = val_acc3 / len(val_y)

    print(f'So min-max skaliranje imame tochnost so validacisko mnozestvo od {val_acc3}')

    tp, fp, tn, fn = 0, 0, 0, 0
    predictions = classifier3.predict(scaler2.transform(test_x))
    for pred, true in zip(predictions, test_y):
        if true == 'good':
            if pred == true:
                tp += 1
            else:
                fn += 1
        else:
            if pred == true:
                tn += 1
            else:
                fp += 1

    acc = (tp + tn) / (tp + fp + tn + fn)
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)

    print('Evaluacija:')
    print(f'Tochnost: {acc}')
    print(f'Preciznost: {precision}')
    print(f'Odziv: {recall}')
