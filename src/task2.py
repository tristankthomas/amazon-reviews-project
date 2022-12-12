import pandas as pd
import re

def task2():
    data = pd.read_csv('data/dataset.csv', index_col=False)
    
    # output dataframe
    output = data.loc[:, ['ID', 'category']].set_index('ID')
    # review list dataframe
    review_list = data['REVIEWLIST']
    average_score = []
    for review in review_list:
        # finds average score for each product
        average_score.append(get_average_score(review))

    output['average_score'] = average_score
    output.to_csv('task2.csv')
    return output

def get_average_score(review):
    matches = get_scores(review)

    return average([int(x) for x in matches])

def get_scores(review):
    # this function split up so can be used in task 6
    pattern = r'(?<=a-star-)(\d)'
    # wont add to matches if invalid review
    matches = re.findall(pattern, review)
    return matches

def average(lst):
    # average of 0 if no valid reviews for product
    return 0 if len(lst) == 0 else sum(lst) / len(lst)



