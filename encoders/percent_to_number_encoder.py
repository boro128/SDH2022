from sklearn.base import TransformerMixin, BaseEstimator
import pandas as pd

class PercentToNumberEncoder(BaseEstimator, TransformerMixin):

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X_ = X.copy()
        X_ = pd.DataFrame(X_) # gdyby wejście było z numpy
        X_ = X_.apply(lambda col: col.str.rstrip('%'))
        X_ = X_.fillna(0)
        X_ = X_.astype(int)
        return X_
