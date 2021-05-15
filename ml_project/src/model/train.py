import pickle
import yaml
from sklearn.metrics import roc_auc_score, accuracy_score


def model_metrics(x_train, y_train, x_test, y_test, model):
    metrics = {
      'train_accuracy': float(accuracy_score(y_train, model.predict(x_train))),
      'test_accuracy': float(accuracy_score(y_test, model.predict(x_test))),
      'train_roc_auc': float(roc_auc_score(y_train, model.predict_proba(x_train)[:, 1])),
      'test_roc_auc': float(roc_auc_score(y_test, model.predict_proba(x_test)[:, 1]))}
    return metrics


def logistic_regression_model(x_train, y_train):
    from sklearn.linear_model import LogisticRegression
    return LogisticRegression(max_iter=2000).fit(x_train, y_train)


def naive_bayes_model(x_train, y_train):
    from sklearn.naive_bayes import GaussianNB
    return GaussianNB().fit(x_train, y_train)


def save_model(model, model_path):
    with open(model_path, 'wb') as file:
        pickle.dump(model, file)


def train_save_model(x_train, y_train, x_test,
                     y_test, model_type, metrics_path, model_path):
    if model_type == 'LR':
        model = logistic_regression_model(x_train, y_train)

    elif model_type == 'NB':
        model = naive_bayes_model(x_train, y_train)

    metrics = model_metrics(x_train, y_train, x_test, y_test, model)

    with open(metrics_path, 'w') as file:
        yaml.dump(metrics, file)

    save_model(model, model_path)


