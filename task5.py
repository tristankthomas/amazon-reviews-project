import pandas as pd
import matplotlib.pyplot as plt
from task2 import task2


def task5():
    scores = task2()
    scores = scores.groupby(['category']).mean()
    fig, ax = plt.subplots()
    fig.set_figheight(8)
    fig.set_figwidth(18)
    fig.subplots_adjust(bottom=0.25)
    ax.set_ylabel('Average score out of 5', fontsize=13)
    ax.set_xlabel('Category', fontsize=13)
    ax.set_title('Average review score for each Amazon category', fontsize=18)
    ax.bar(scores.index, scores['average_score'])
    
    ax.tick_params(axis='x', labelrotation=40)
    plt.xticks(ha='right')
    
    plt.savefig('task5.png')
    plt.close()
    
    return


