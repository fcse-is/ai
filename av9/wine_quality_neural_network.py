from sklearn.neural_network import MLPClassifier


def read_dataset():
    data = []
    with open('winequality.csv') as f:
        _ = f.readline()
        while True:
            line = f.readline().strip()
            if line == '':
                break
            parts = line.split(';')
            data.append(list(map(float, parts[:-1])) + parts[-1:])

    return data


def divide_sets(dataset):
    bad_classes = [x for x in dataset if x[-1] == 'bad']
    good_classes = [x for x in dataset if x[-1] == 'good']

    train_set = bad_classes[:int(len(bad_classes) * 0.7)] + good_classes[:int(len(good_classes) * 0.7)]
    val_set = bad_classes[int(len(bad_classes) * 0.7):int(len(bad_classes) * 0.8)] + \
              good_classes[int(len(good_classes) * 0.7):int(len(good_classes) * 0.8)]
    test_set = bad_classes[int(len(bad_classes) * 0.8):] + good_classes[int(len(good_classes) * 0.8):]

    return train_set, val_set, test_set


if __name__ == '__main__':
    dataset = read_dataset()
    train_set, val_set, test_set = divide_sets(dataset)

    train_x = [x[:-1] for x in train_set]
    train_y = [x[-1] for x in train_set]
    val_x = [x[:-1] for x in val_set]
    val_y = [x[-1] for x in val_set]
    test_x = [x[:-1] for x in test_set]
    test_y = [x[-1] for x in test_set]

    classifier = MLPClassifier(5, activation='relu', learning_rate_init=0.001, max_iter=500, random_state=0)
    classifier2 = MLPClassifier(10, activation='relu', learning_rate_init=0.001, max_iter=500, random_state=0)
    classifier3 = MLPClassifier(100, activation='relu', learning_rate_init=0.001, max_iter=500, random_state=0)

    classifier.fit(train_x, train_y)
    classifier2.fit(train_x, train_y)
    classifier3.fit(train_x, train_y)

    final_classifier = None
    max_acc = 0
    for i, c in enumerate([classifier, classifier2, classifier3]):
        val_predictions = c.predict(val_x)
        val_acc = 0
        for true, pred in zip(val_y, val_predictions):
            if true == pred:
                val_acc += 1

        val_acc = val_acc / len(val_y)

        print(f'Klasifikatorot {i} ima tochnost so validacisko mnozestvo od {val_acc}')

        if val_acc > max_acc:
            max_acc = val_acc
            final_classifier = c

    acc = 0
    predictions = final_classifier.predict(test_x)

    for true, pred in zip(test_y, predictions):
        if true == pred:
            acc += 1

    acc = acc / len(test_y)

    print(f'Tochnosta so testirachkoto mnozhestvo e: {acc}')
