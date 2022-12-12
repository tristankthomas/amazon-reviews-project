import pandas as pd
import re
from task2 import average

def task3():
    data = pd.read_csv('data/dataset.csv', index_col=False)
    # output dataframe
    output = data.loc[:, ['ID', 'category']].set_index('ID')
    prices = data['cost']
    average_cost = []
    for price in prices:
        # adds average cost to list
        average_cost.append(get_price(price))
    
    output['average_cost'] = average_cost
    output.to_csv('task3.csv')
    
    return output

def get_price(price):
    pattern = r'(?<=\$)([\d,]+\.\d+)'
    # accounts for invalid costs
    matches = re.findall(pattern, price)
    matches = [x.replace(',','') for x in matches]
    
    return round(average([float(x) for x in matches]), 2)
