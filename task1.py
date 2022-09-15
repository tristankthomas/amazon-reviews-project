import pandas as pd
import json

def task1():
    data = pd.read_csv('dataset.csv', index_col='ID')
    # number of products and number of categories
    num_prods = len(data)
    categories = len(data.groupby(['category']))

    # defining json string and dumping to file
    json_str = """
    {
      "Number of Products:": %d,
      "Number of Categories:": %d
    } 
    """ % (num_prods, categories)
    json.dump(json.loads(json_str), open("task1.json", 'w'))
    
    return

    
    
