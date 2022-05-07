from sklearn.base import TransformerMixin, BaseEstimator


class ColumnDropper(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def transform(self, X, y=None):
        return X.drop(columns=self.columns)

    def fit(self, X, y=None):
        return self
