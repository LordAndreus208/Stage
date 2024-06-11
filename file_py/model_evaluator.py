class ModelEvaluator:
    """
    This class provides methods for evaluating machine learning models using classification reports.
    """

    from sklearn.metrics import classification_report

    def __init__(self, models):
        """
        Initializes the ModelEvaluator with a dictionary of models.

        Parameters:
        - models: dict, a dictionary containing names of models as keys and their corresponding trained models as values
        """
        self.models = models

    def evaluate_models(self, X_test, y_test):
        """
        Evaluates the performance of each model in the provided dictionary on the test data.

        Parameters:
        - X_test: array-like, shape (n_samples, n_features), testing input data
        - y_test: array-like, shape (n_samples,), testing target labels

        Returns:
        - evaluation_results: dict, classification reports for each model
        """
        evaluation_results = {}
        for name, model in self.models.items():
            y_pred = model.predict(X_test)
            report = ModelEvaluator.classification_report(y_test, y_pred, output_dict=True)
            evaluation_results[name] = report
            print(f'\n{name} Classification Report:')
            print(ModelEvaluator.classification_report(y_test, y_pred))
        return evaluation_results