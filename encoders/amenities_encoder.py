import pandas as pd
import itertools
import re

from sklearn.base import TransformerMixin, BaseEstimator
from collections import Counter


class AmenitiesEncoder(BaseEstimator, TransformerMixin):
    
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        
        def replacespaces(s):
            s = re.sub(r"[^\w\s]", '', s)
            s = re.sub(r"\s+", '-', s)
            return s
        
        l = list(X.iloc[0])
        l = [[word.strip('[" ]') for word in row[1:-1].split(',')] for row in l]
        lst = list(itertools.chain.from_iterable(l))
        final = Counter(lst)
        final = final.most_common(35)

        amenities_list = [el for el, _ in final]

        tmp = pd.DataFrame()
        for el in amenities_list:
            tmp[el] = X['amenities'].str.contains(el).astype(int)
            
        cols = [replacespaces(col) for col in tmp.columns]
        tmp.columns = cols
        
        return tmp
