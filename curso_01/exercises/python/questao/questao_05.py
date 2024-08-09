import pandas as pd
import numpy as np

sales2 = pd.read_csv('../basedados/sales2.csv')
sales3 = sales2.query('(`Order Priority` == "H" or `Order Priority` == "M") &  `Units Sold` > 1000 ')
print(sales3)

sales4 = sales3.query('`Item Type` == "Beverages" or `Item Type` == "Fruits"')

sales5 = sales4.groupby(['Item Type'])['Total Profit'].agg([
                            ('tip_mean', np.mean),
                            ('max_mean', max)
                            ])



print(sales5)