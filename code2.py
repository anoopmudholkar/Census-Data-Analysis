import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

# load data
censusdatachi = pd.read_csv('final_dataset.csv')
X = censusdatachi[['Age', 'Hours_per_week', 'Workclass_cat_new', 'Education_cat_new', 'Marital_Status_cat_new',
                   'Occupation_cat', 'Race_cat', 'Sex_cat']]
Y = censusdatachi['Income_cat']
# feature extraction
test = SelectKBest(score_func=chi2, k='all')
fit = test.fit(X, Y)
print(fit.scores_)

