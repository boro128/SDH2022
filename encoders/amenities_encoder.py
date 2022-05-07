import pandas as pd
import itertools
import re

from sklearn.base import TransformerMixin, BaseEstimator
from collections import Counter


class AmenitiesEncoder(BaseEstimator, TransformerMixin):
    
    def __init__(self):
        super().__init__()
        self.amenities_list = list()
    
    def fit(self, X, y=None):
        l = list(X.iloc[0])
        l = [[word.strip('[" ]') for word in row[1:-1].split(',')] for row in l]
        lst = list(itertools.chain.from_iterable(l))
        final = Counter(lst)
        final = final.most_common(35)
        self.amenities_list = [el for el, _ in final]
        return self

    def transform(self, X, y=None):
        
        def replacespaces(s):
            s = re.sub(r"[^\w\s]", '', s)
            s = re.sub(r"\s+", '-', s)
            return s
               

        tmp = pd.DataFrame()
        for el in self.amenities_list:
            tmp[el] = X['amenities'].str.contains(el).astype(int)
            
        cols = [replacespaces(col) for col in tmp.columns]
        tmp.columns = cols
        
        return tmp

    def get_feature_names(self):
        return self.amenities_list
