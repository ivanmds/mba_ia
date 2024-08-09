import pandas as pd
import numpy as np

dtips = pd.read_csv('basedados/tips.csv')

dtips2 = dtips.query('time == "Dinner" & total_bill > 40')
print(dtips2)


dtips3 = dtips.groupby(['day', 'time'])['tip'].agg([
                            ('tip_mean', np.mean),
                            ('max_mean', max)
                            ])
print(dtips3)