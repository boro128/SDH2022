import pandas as pd

from sklearn.base import TransformerMixin, BaseEstimator
from datetime import datetime

class DaysSinceEncoder(BaseEstimator, TransformerMixin):
    
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X_ = X.copy()
        X_ = pd.DataFrame(X_) # gdyby wejście było z numpy
        X_ = X_.apply(pd.to_datetime)
        delta = datetime.now() - X_
        days_since = delta.apply(lambda col: col.dt.days)
        days_since = days_since.fillna(-1)
        return days_since
