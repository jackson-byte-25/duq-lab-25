import pandas
import sklearn
import sklearn.linear_model

class ReusableClassifier(): 
    def __init__(self, model_type: str):
        """create a classifier, storing a model and metadata

        Args:
            model_type (str): can include random forests, logistic regression
        """
        self.model
        
    def _create_logistic_regression(self):
        """create a new logistic regression model from sklearn.
        """
        return sklearn.linear_model.LogisticRegression()