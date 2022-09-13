import pandas as pd
from task6 import task6
from collections import Counter
import math
import csv

def task7():
    data = task6()
    count = 0
    count2 = 0
    neg_df = data.loc[data['score'] == 1]
    pos_df = data.loc[data['score'] == 5]
    positive = []
    negative = []
    vocab = []
    for review in neg_df['bigrams']:
        for bi in review:
            negative.append(bi)
            vocab.append(bi)
    for review in pos_df['bigrams']:
        for bi in review:
            positive.append(bi)
            vocab.append(bi)
    num_pos = len(positive)
    num_neg = len(negative)

    pos_count = Counter(positive)
    neg_count = Counter(negative)
    vocab_count = Counter(vocab)
    vocab_dict = {}
    for bi in vocab_count:
        if bi in pos_count and bi in neg_count:
            vocab_dict[bi] = round(math.log10(get_odds(pos_count[bi], num_pos) / get_odds(neg_count[bi], num_neg)), 4)
            

    df = pd.DataFrame(list(vocab_dict.items()), columns = ['bigram','log_odds_ratio'])
    df = df.sort_values(by=['log_odds_ratio'])
    df.to_csv('task7a.csv', index=False)
    # csv_writer = csv.DictWriter(open("task7a.csv", 'w'), ['bigram', 'log_odds_ratio'])
    # csv_writer.writerows(vocab_dict)
    return

def get_odds(count, total):
    prob = count / total

    return prob / (1 - prob)
