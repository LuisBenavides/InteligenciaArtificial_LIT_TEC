def load_data():
    import pandas as pd
    x_train = pd.read_csv('data/x_train.csv')
    y_train = pd.read_csv('data/y_train.csv')
    x_test = pd.read_csv('data/x_test.csv')
    y_test = pd.read_csv('data/y_test.csv')
    return x_train, y_train, x_test, y_test

def train_model(x_train, y_train):
    from sklearn.linear_model import LogisticRegression
    classifier = LogisticRegression()
    classifier.fit(x_train, y_train)
    return classifier

def evaluate_model(classifier, x_test, y_test):
    from sklearn.metrics import f1_score
    y_pred = classifier.predict(x_test)
    model_f1_score = f1_score(y_test, y_pred)
    print(f'F1_Score: {model_f1_score}')

def save_model_v1(model):
    import pickle
    filename = 'finalized_model.sav'
    pickle.dump(model, open(f'models/{filename}', 'wb'))
    return 

def save_model_v2(model):
    import joblib
    # save the model to disk
    filename = 'finalized_model.sav'
    joblib.dump(model, filename)

def main():
    x_train, y_train, x_test, y_test = load_data()
    classifier = train_model(x_train, y_train)
    evaluate_model(classifier, x_test, y_test)
    save_model_v1(classifier)

if __name__ == '__main__':
    main()
