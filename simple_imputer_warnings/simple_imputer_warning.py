# %%
import pandas as pd
from sklearn.impute import SimpleImputer

data_source = 'pickle' # change to 'csv' to download data from .csv file
# data_source = 'csv'
if data_source == 'pickle':
    numerical_vars = pd.read_pickle('numerical_vars.pkl')
elif data_source == 'csv':
    sep = '\t'
    sep_decimals = '.'
    numerical_vars = pd.read_csv('numerical_vars.csv', sep=sep, decimal=sep_decimals)

# %%
print(numerical_vars.info()) # [7 float64 columns,  900 rows]

# %%
# change col values
col = '1' # cols ['0', '1'] Impute good  without raising warning
df = numerical_vars[[col]].copy()
my_imputer = SimpleImputer(strategy='mean')
imputed_X_train = pd.DataFrame(my_imputer.fit_transform(df))

# %%
# change col values
col = '2' # cols ['2', '3', '4', '5', '6] Impute bad. Raise  RuntimeWarning (only using data in pickle format)
df = numerical_vars[[col]].copy()
my_imputer = SimpleImputer(strategy='mean')
imputed_X_train = pd.DataFrame(my_imputer.fit_transform(df))
