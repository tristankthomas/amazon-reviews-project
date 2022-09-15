import pandas as pd
import matplotlib.pyplot as plt
from task2 import task2


def task5():
    # output from task 2
    scores = task2()
    # groups scores with mean of each category
    scores = scores.groupby(['category']).mean()

    # plots average score for each category
    fig, ax = plt.subplots()
    fig.set_figheight(8)
    fig.set_figwidth(18)
    # makes room for slanted labels
    fig.subplots_adjust(bottom=0.3)
    ax.set_ylabel('Average score out of 5', fontsize=13)
    ax.set_xlabel('Category', fontsize=13)
    ax.set_title('Average review score for each Amazon category', fontsize=18)
    ax.bar(scores.index, scores['average_score'])

    # alternates tick colour for better readability
    for t in range(len(scores)):
        if t % 2 != 0:
            ax.get_xticklabels()[t].set_color('#0D316B')

    # rotates x labels
    ax.tick_params(axis='x', labelrotation=40)
    plt.xticks(ha='right', fontsize=11)
    plt.yticks(fontsize=12)
    
    plt.savefig('task5.png', dpi=200)
    plt.close()
    
    return


