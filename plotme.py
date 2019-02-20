#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from Results import OutputResult


#task_len$BrutForce$SA_score$h_score$ga_score
path = './results/results.csv'
data = pd.read_csv(path,sep='$')


 
data_all = data.groupby('task_len')

tasks_len = data_all.groups.keys()

def score_figures():
        algorithms_list = ['HC_score','SA_score','GA_score']
        fig, axes = plt.subplots(nrows=1,ncols=6, figsize=(35,8))
        plt.subplots_adjust(left= 0.1, bottom=0.1, right=0.9, top=0.8, wspace=0.5, hspace=0.2)

        # fro each task_len get all scores
        for plt_idx, task_length in enumerate(tasks_len):

                task_scores = []
                # get all scores for this task_len
                for alg in algorithms_list:
                        data_alg = data_all[alg].apply(list)    
                        task_scores.append( data_alg[task_length] )

                axes[plt_idx].violinplot(task_scores)
                # axes[plt_idx].boxplot(task_scores)

                # draw optimal score    
                up_score = data_all['UP_score'].apply(list)[task_length][0]
                axes[plt_idx].axhline(y=up_score, color='r', linestyle='-.', linewidth=0.5)
                
                # ygrid and xlable
                axes[plt_idx].yaxis.grid(True)    
                axes[plt_idx].set_xlabel('Task len='+str(task_length))    
        
        # Ylabel for the first subplot
        axes[0].set_ylabel('User preference score')

        # add x-tick labels
        plt.setp(axes, xticks=[1, 2,3],
                xticklabels=[s.split('_')[0] for s in algorithms_list])
        fig.suptitle('User preference search algorithms', fontsize=12)

        #plt.show()
        plt.savefig("./results/search_score.png")  
        plt.close()

# make it one function
def time_figures():
        algorithms_list = ['HC_time','SA_time','GA_time']
        fig, axes = plt.subplots(nrows=1,ncols=6, figsize=(35,8))
        plt.subplots_adjust(left= 0.1, bottom=0.1, right=0.9, top=0.8, wspace=0.5, hspace=0.2)

        # fro each task_len get all scores
        for plt_idx, task_length in enumerate(tasks_len):

                task_scores = []
                # get all scores for this task_len
                for alg in algorithms_list:
                        data_alg = data_all[alg].apply(list)    
                        task_scores.append( data_alg[task_length] )

                axes[plt_idx].violinplot(task_scores)
                # axes[plt_idx].boxplot(task_scores)

                # draw optimal score    
                up_score = data_all['BF_time'].apply(list)[task_length][0]
                axes[plt_idx].axhline(y=up_score, color='g', linewidth=0.9)
                
                # ygrid and xlable
                axes[plt_idx].yaxis.grid(True)    
                axes[plt_idx].set_xlabel('Task len='+str(task_length))    
        
        # Ylabel for the first subplot
        axes[0].set_ylabel('Elapsed time')

        # add x-tick labels
        plt.setp(axes, xticks=[1, 2,3],
                xticklabels=[s.split('_')[0] for s in algorithms_list])
        fig.suptitle('Elapsed time for searching algorithms', fontsize=12)

        #plt.show()
        plt.savefig("./results/search_time.png")  
        plt.close()

if __name__ == "__main__":
        score_figures()
        time_figures()
  
        res = OutputResult(path)
        exp_iterations = [i*30 for i in range(6)]

        for i in exp_iterations:
                res.create_figures(i, i*30-1)