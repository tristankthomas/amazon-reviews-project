import pandas as pd
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
    print(data.head())
    # x = range(len(data))
    # fig, ax1 = plt.subplots()

    # ax1.set_xlabel('Abitrary values')
    # ax1.set_ylabel('Average Cost ($)', color='red')
    # plt.plot(x, data['average_cost'], marker='.', color='red')

    # ax2 = ax1.twinx()
    # ax2.set_ylabel('Average Score (out of 5)', color='blue')
    # plt.plot(x, data['average_score'], marker='o', color='blue')
    # plt.savefig('tsk4.png')
    plt.plot(data['average_cost'], data['average_score'])
    plt.savefig('task5.png')
    return
