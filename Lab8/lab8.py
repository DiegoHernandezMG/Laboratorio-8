import pandas as pd

file_path = 'iris/bezdekIris.data'
df = pd.read_csv(file_path, sep=',', header=None)
print(df)