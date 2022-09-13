import pandas as pd
from task6 import task6
from collections import Counter
import matplotlib.pyplot as plt
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

    pos_count = Counter(positive)
    neg_count = Counter(negative)
    vocab_count = Counter(vocab)
    vocab_dict = {}
    
    for bi in vocab_count:
        if bi in pos_count and bi in neg_count:
            vocab_dict[bi] = round(math.log10(get_odds(pos_count[bi], len(positive)) / get_odds(neg_count[bi], len(negative))), 4)
            

    df = pd.DataFrame(list(vocab_dict.items()), columns = ['bigram','log_odds_ratio']).sort_values(by=['log_odds_ratio'])
    
    df.to_csv('task7a.csv', index=False)
    
    # plots
    fig1, ax1 = plt.subplots()
    fig1.set_figheight(11)
    fig1.set_figwidth(8)
    ax1.hist(df['log_odds_ratio'], bins=25)
    ax1.set_ylabel('Number of bigrams', fontsize=13)
    ax1.set_xlabel('Log odds ratio', fontsize=13)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    ax1.set_title('Bigram log odds ratio distribution', fontsize=18)
    plt.savefig('task7b.png')
    plt.close()

    fig2, ax2 = plt.subplots()
    largest = df.nlargest(10, 'log_odds_ratio')
    smallest = df.nsmallest(10, 'log_odds_ratio')

    smallest = smallest.astype({'bigram':'string'})
    largest = largest.astype({'bigram':'string'}).iloc[::-1]
    
    fig2.set_figheight(12)
    fig2.set_figwidth(12)
    fig2.subplots_adjust(bottom=0.23)
    ax2.bar(smallest['bigram'], smallest['log_odds_ratio'], color='red')
    ax2.bar(largest['bigram'], largest['log_odds_ratio'], color='blue')
    ax2.tick_params(axis='x', labelrotation=30)
    plt.xticks(ha='right', fontsize=13)
    plt.yticks(fontsize=12)
 
    for t in range(10):
        ax2.get_xticklabels()[t].set_color("red")
        ax2.get_xticklabels()[t + 10].set_color("blue")
        
    colours = [plt.Rectangle((0,0),1,1, color='blue'), plt.Rectangle((0,0),1,1, color='red')]
    plt.legend(colours, ['Top 10 highest log odds ratios', 'Top 10 lowest log odds ratios'], fontsize=15)
    ax2.set_ylabel('Log odds ratio', fontsize=15)
    ax2.set_xlabel('Bigrams', fontsize=15)
    ax2.set_title('Top 10 highest and lowest bigrams based on log odds ratio', fontsize=20)
    plt.savefig('task7c.png')
    plt.close()
    
    
    return



def get_odds(count, total):
    prob = count / total

    return prob / (1 - prob)
