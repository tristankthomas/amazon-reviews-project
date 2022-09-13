import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from task2 import task2
from task3 import task3

def task4():
    avg_score = task2()
    avg_score_pet = avg_score.loc[avg_score['category'] == 'Pet Supplies']
    
    avg_cost = task3()
    avg_cost_pet = avg_cost.loc[avg_score['category'] == 'Pet Supplies']
    data = avg_cost_pet.copy().assign(average_score = avg_score_pet['average_score'])
    
    data = data.sort_values(by=['average_cost'])
    fig, ax = plt.subplots()
    fig.set_figheight(7)
    fig.set_figwidth(15)

    ax.scatter(data['average_cost'], data['average_score'], s=15)
    ax.set_ylabel('Average score out of 5', fontsize=13)
    ax.set_xlabel('Average cost ($)', fontsize=13)
    ax.set_title('Average review score for Pet Supply products against cost', fontsize=18)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    # trendline
    z = np.polyfit(data['average_cost'], data['average_score'], 1)
    p = np.poly1d(z)
    ax.plot(data['average_cost'], p(data['average_cost']), linestyle='dashed')
    plt.savefig('task4.png')
    plt.close()
    return
