import pandas as pd
import re

def task2():
    data = pd.read_csv('dataset.csv', index_col=False)
    output = data.loc[:, ['ID', 'category']].set_index('ID')
    review_list = data['REVIEWLIST']
    average_score = []
    for review in review_list:
        average_score.append(get_average(review))
    #get_review_field(review_list, "review_star")
    output['average_score'] = average_score
    output.to_csv('task2.csv')
    return output

def get_average(review):
    matches = get_scores(review)

    return average([int(x) for x in matches])

def get_scores(review):
    pattern = r'(?<=a-star-)(\d)'
    matches = re.findall(pattern, review)
    return matches

def average(lst):
    return 0 if len(lst) == 0 else sum(lst) / len(lst)



