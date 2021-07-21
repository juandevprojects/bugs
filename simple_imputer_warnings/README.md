I was working in a project and when I arrive to imputation step I realized that imputation step was raising a warning.

When SimpleImputer method from [SciKitLearn library](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html)
is applied to this data: columns 0 and 1 was imputed normally but from 2 to 6 raise the following warning:

``` python
/python3.6/site-packages/numpy/core/fromnumeric.py:87: RuntimeWarning: invalid value encountered in reduce
  return ufunc.reduce(obj, axis, dtype, out, **passkwargs)
```
So I decided to start this repo to put bugs that I have not solved.

This folder contains two data files with 7 float64 columns and 900 rows: 
- numerical_vars.pkl
- numerical_vars.csv 

Both files were obtained from the original dataset using:
```.to_csv('numerical_vars.csv', index = False, sep = '\t', decimal = '.')``` 
and 
```.to_pickle ('numerical_vars.csv')``` 
respectively.


## Environment data
-   OS and version: Ubuntu 20.04.2 LTS
-   Python version: 3.6.9
-   virtual enviroment: requirements.txt

## Expected behaviour

Impute all columns without raise warning and using any data source (pickle or .csv)

## Actual behaviour
numpy raise a warning when download data from pickle file
``` python
/python3.6/site-packages/numpy/core/fromnumeric.py:87: RuntimeWarning: invalid value encountered in reduce
  return ufunc.reduce(obj, axis, dtype, out, **passkwargs)
```

## Code Snippet / Additional information
In simple_imputer_warning.py
