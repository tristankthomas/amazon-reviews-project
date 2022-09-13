import pandas as pd
import json

def helloworld():
    print("helloworld")
def task1():
    data = pd.read_csv('dataset.csv', index_col='ID')
    num_prods = len(data)
    categories = len(data.groupby(['category']))
    json_str = """
    {
      "Number of Products:": %d,
      "Number of Categories:": %d
    } 
    """ % (num_prods, categories)
    json.dump(json.loads(json_str), open("task1.json", 'w'))
    return
    # output_dict = {"Number of Products:": num_prods, "Number of Categories:": categories}
    # output = pd.DataFrame(output_dict, index = [0])
    # json_str = output.to_json()
    
    
