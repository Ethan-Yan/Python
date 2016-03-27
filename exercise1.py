import numpy as np
import pandas as pd

# Functions useful for statistical analysis -- mean median std
numbers = [1, 2, 3, 4, 5]
print(np.mean(numbers))
print(np.median(numbers))
print(np.std(numbers))

# Dataframe

d = {'name': pd.Series(['Braund', 'Cummings', 'Heikkinen', 'Allen'],
                   index = ['a', 'b', 'c', 'd']),
     'age': pd.Series([22, 38, 26, 35], index = ['a', 'b', 'c', 'd']),
     'fare': pd.Series([7.25, 71.83, 8.05], index = ['a', 'b', 'd']),
     'survived?': pd.Series([False, True, True, False], index = ['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
print(df)

# Columns
df['name']
df[['name', 'age']]
df.loc['a']
df[df['age']>=30]
df['survived?'][df['age']>=30]

# Vectorized Methods
