import pandas as pd

table = pd.read_html('TKB.html')

print(table[1])


for data in table[1]:
    print(data)