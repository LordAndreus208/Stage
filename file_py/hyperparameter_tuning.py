class HyperparameterTuning:
    """
    This class provides methods for tuning hyperparameters of machine learning models using grid search.
    """

    from sklearn.model_selection import GridSearchCV
    from sklearn.metrics import make_scorer, f1_score
    from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
    from sklearn.naive_bayes import GaussianNB
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import StandardScaler
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.linear_model import LogisticRegression

    def tune_hyperparameters(X_train, y_train):
        """
        Performs hyperparameter tuning for various machine learning algorithms using grid search.

        Parameters:
        - X_train: array-like, shape (n_samples, n_features), training input data
        - y_train: array-like, shape (n_samples,), training target labels

        Returns:
        - best_models: dict, best estimator for each algorithm after hyperparameter tuning
        """
        algorithms = {
            'Random Forest': (HyperparameterTuning.RandomForestClassifier(), {
                'n_estimators': [100, 200, 300],
                'max_depth': [None, 10, 20],
                'min_samples_split': [2, 5, 10]
            }),
            'Gradient Boosting': (HyperparameterTuning.GradientBoostingClassifier(), {
                'n_estimators': [100, 200, 300],
                'learning_rate': [0.01, 0.1, 0.3],
                'max_depth': [3, 5, 7]
            }),
            'Naive Bayes': (HyperparameterTuning.GaussianNB(), {}),
            'KNN': (HyperparameterTuning.Pipeline([
                ('knn', HyperparameterTuning.KNeighborsClassifier())
            ]), {
                'knn__n_neighbors': [3, 5, 7, 9],
                'knn__weights': ['uniform', 'distance'],
                'knn__metric': ['euclidean', 'manhattan', 'minkowski']
            }),
            'Logistic Regression': (HyperparameterTuning.Pipeline([
                ('scaler', HyperparameterTuning.StandardScaler()),
                ('logreg', HyperparameterTuning.LogisticRegression(max_iter=1000))
            ]), {
                'logreg__C': [0.01, 0.1, 1, 10, 100],
                'logreg__solver': ['lbfgs', 'liblinear']
            })
        }

        scorer = HyperparameterTuning.make_scorer(HyperparameterTuning.f1_score)
        best_models = {}
        for name, (model, params) in algorithms.items():
            grid_search = HyperparameterTuning.GridSearchCV(model, params, scoring=scorer, cv=5, n_jobs=-1)
            grid_search.fit(X_train, y_train)
            best_models[name] = grid_search.best_estimator_
            print(f'Best parameters for {name}: {grid_search.best_params_}')
            print(f'Best F1-score: {grid_search.best_score_}')
        return best_models