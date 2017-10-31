###############################################################################
# Coral Classification Project -- Visualizations 
# 
# Author(s): Roger Doles
#            Nicholas Houghton
#
# Date: 10/31/17
#
# Purpose: Plot frequncy counts of coral species 
#
###############################################################################


import os
import glob
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter

def csvToPlot(filename):
    df = pd.read_csv(filename)
  
    count = {}
    counts = {}
    # count each species into dictionary
    for i in range(len(df)):
        count = df.iloc[i].value_counts().to_dict()
        counts = dict(Counter(count)+Counter(counts))
    
    # remove count of 'no species' aka 0
    del counts[0]
    
    # Turn counts into a dataframe
    counts=pd.DataFrame.from_dict(counts, orient='index' )
    
    
    # get species / code map
    species_map = pd.read_csv('palmyra_legend.csv', index_col=0)
    mapped = pd.concat([counts,species_map],axis=1,ignore_index=False)
    mapped = mapped.dropna(axis=0,how='any')
    mapped = mapped.reset_index()
    mapped.columns = ['key','count','species','morph']
    
    
    filename = filename.replace('.csv','.png')
    
    #seaborn
    sns.set()
    
    # plot counts of each type
    x = mapped.index
    y = mapped['count'] / 1000000
    labels = mapped['species']
    fig = plt.figure(figsize=(12, 10))
    plt.bar(x, y)
    plt.title('Coral Frequencies on Palmyra--' + filename.replace('.png','') );
    plt.xticks(x, labels, rotation=82) 
    plt.ylabel('Population (in millions)')
    plt.subplots_adjust(bottom=0.15)
    
    plt.savefig('../../../../palmyraVis/VIS_'+filename, bbox_inches='tight')
    #plt.clf()
    plt.close(fig)
  
    return;

# Get mosacic file names
os.chdir( '../data/mosaics/palmyra/' )
result = glob.glob( r'*.csv' )

for r in result[2:]:
    csvToPlot(r)
