import csv
from sklearn.preprocessing import OrdinalEncoder
from sklearn.tree import DecisionTreeClassifier

if __name__ == '__main__':
    with open('car.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        dataset = list(csv_reader)[1:]

    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])

    train_set = dataset[:int(0.7 * len(dataset))]
    train_x = [t[:-1] for t in train_set]
    train_x = encoder.transform(train_x)
    train_y = [t[-1] for t in train_set]

    test_set = dataset[int(0.7 * len(dataset)):]
    test_x = [t[:-1] for t in test_set]
    test_x = encoder.transform(test_x)
    test_y = [t[-1] for t in test_set]

    classifier = DecisionTreeClassifier(criterion='entropy')
    classifier.fit(train_x, train_y)

    print(f'Depth: {classifier.get_depth()}')
    print(f'Number of leaves: {classifier.get_n_leaves()}')

    correct_samples = 0
    for x, y in zip(test_x, test_y):
        y_predicted = classifier.predict([x])[0]
        if y == y_predicted:
            correct_samples += 1

    accuracy = correct_samples / len(test_set)
    print(f'Accuracy: {accuracy}')

    feature_importances = list(classifier.feature_importances_)
    print(f'Feature importances: {feature_importances}')

    most_important_feature = feature_importances.index(max(feature_importances))
    print(f'Most important feature: {most_important_feature}')

    least_important_feature = feature_importances.index(min(feature_importances))
    print(f'Least important feature: {least_important_feature}')

    train_x_2 = list()
    for t in train_x:
        sample = [t[i] for i in range(len(t)) if i != most_important_feature]
        train_x_2.append(sample)

    test_x_2 = list()
    for t in test_x:
        sample = [t[i] for i in range(len(t)) if i != most_important_feature]
        test_x_2.append(sample)

    train_x_3 = list()
    for t in train_x:
        sample = [t[i] for i in range(len(t)) if i != least_important_feature]
        train_x_3.append(sample)

    test_x_3 = list()
    for t in test_x:
        sample = [t[i] for i in range(len(t)) if i != least_important_feature]
        test_x_3.append(sample)

    classifier2 = DecisionTreeClassifier(criterion='entropy')
    classifier3 = DecisionTreeClassifier(criterion='entropy')

    classifier2.fit(train_x_2, train_y)
    classifier3.fit(train_x_3, train_y)

    print(f'Depth (removed most important feature): {classifier2.get_depth()}')
    print(f'Number of leaves (removed most important feature): {classifier2.get_n_leaves()}')

    print(f'Depth (removed least important feature): {classifier3.get_depth()}')
    print(f'Number of leaves (removed least important feature): {classifier3.get_n_leaves()}')

    correct_samples2 = 0
    for x, y in zip(test_x_2, test_y):
        y_predicted = classifier2.predict([x])[0]
        if y == y_predicted:
            correct_samples2 += 1

    correct_samples3 = 0
    for x, y in zip(test_x_3, test_y):
        y_predicted = classifier3.predict([x])[0]
        if y == y_predicted:
            correct_samples3 += 1

    accuracy2 = correct_samples2 / len(test_set)
    accuracy3 = correct_samples3 / len(test_set)

    print(f'Accuracy (removed most important feature): {accuracy2}')
    print(f'Accuracy (removed least important feature): {accuracy3}')
