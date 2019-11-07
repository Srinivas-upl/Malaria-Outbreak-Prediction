import pandas as pd
import numpy as np

df = pd.read_excel('cowise1.xlsx')


s=input( " : " )

print(df.loc[df['country'] == 's'])
