import numpy as np

from sklearn.base import TransformerMixin, BaseEstimator


class BinaryEncoder(BaseEstimator, TransformerMixin):

    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        X_ = X.copy()
        X_ = np.where(X_ == 't', 1, 0)
        return X_
