This folder contains the numerical_vars.csv file with 7 float64 columns and 900 rows

When SimpleImputer method from [SciKitLearn library](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html)
is applied to this data: columns 0 and 1 was imputed normaly but from 2 to 6 raise the following warning.

``` python
/python3.6/site-packages/numpy/core/fromnumeric.py:87: RuntimeWarning: invalid value encountered in reduce
  return ufunc.reduce(obj, axis, dtype, out, **passkwargs)
```

## Environment data
-   OS and version: Ubuntu 20.04.2 LTS
-   Python version: 3.6.9
-   virtual enviroment: requirements.txt

## Expected behaviour

Impute all .csv file without raise warning


## Actual behaviour
numpy raise a warning
``` python
/python3.6/site-packages/numpy/core/fromnumeric.py:87: RuntimeWarning: invalid value encountered in reduce
  return ufunc.reduce(obj, axis, dtype, out, **passkwargs)
```

## Code Snippet / Additional information
In simple_imputer_warning.py
