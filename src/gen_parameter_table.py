import pandas as pd

# load the database
parameter_db = pd.read_csv('src/data/parameter_db.csv')  

# sorting rows by Hamming weight
parameter_db.sort_values(by=['$h$','$\log_2(q)$'], inplace=True)

# print the markdown table
print(parameter_db.to_markdown(index=False))

