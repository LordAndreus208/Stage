class InitialTraining:
    """
    This class provides methods for training and evaluating initial machine learning models.
    """

    from sklearn.tree import DecisionTreeClassifier
    from sklearn.ensemble import AdaBoostClassifier, ExtraTreesClassifier
    from xgboost import XGBClassifier
    from catboost import CatBoostClassifier
    from sklearn.neural_network import MLPClassifier
    from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
    from sklearn.metrics import classification_report

    def train_and_evaluate_initial_models(X_train, y_train, X_test, y_test):
        """
        Trains and evaluates a set of initial machine learning models on the provided training and testing data.

        Parameters:
        - X_train: array-like, shape (n_samples, n_features), training input data
        - y_train: array-like, shape (n_samples,), training target labels
        - X_test: array-like, shape (n_samples, n_features), testing input data
        - y_test: array-like, shape (n_samples,), testing target labels

        Returns:
        - results: dict, classification reports for each model
        """
        algorithms = {
            'Decision Tree': InitialTraining.DecisionTreeClassifier(),
            'AdaBoost': InitialTraining.AdaBoostClassifier(),
            'XGBoost': InitialTraining.XGBClassifier(use_label_encoder=False, eval_metric='logloss'),
            'CatBoost': InitialTraining.CatBoostClassifier(verbose=0),
            'MLP': InitialTraining.MLPClassifier(max_iter=1000),
            'Quadratic Discriminant Analysis': InitialTraining.QuadraticDiscriminantAnalysis(reg_param=0.1),
            'Extra Trees': InitialTraining.ExtraTreesClassifier()
        }

        results = {}
        for name, model in algorithms.items():
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            results[name] = InitialTraining.classification_report(y_test, y_pred, output_dict=True)
            print(f"\n{name} Classification Report:")
            print(InitialTraining.classification_report(y_test, y_pred))
        return results