'''
Assume df is a pandas dataframe object of the dataset given
'''

import numpy as np
import pandas as pd
import random

import math

'''Calculate the entropy of the enitre dataset'''
# input:pandas_dataframe
# output:int/float
print("HI!")

#-------------------------------
def get_entropy_of_dataset(df):
    # TODO

    # E(S) = -aloga-blogb
    
    return 0

#-------------------------------
'''Return avg_info of the attribute provided as parameter'''
# input:pandas_dataframe,str   {i.e the column name ,ex: Temperature in the Play tennis dataset}
# output:int/float
def get_avg_info_of_attribute(df, attribute):
    # TODO

    return avg_info

#-------------------------------
'''Return Information Gain of the attribute provided as parameter'''
# input:pandas_dataframe,str
# output:int/float
def get_information_gain(df, attribute):
    # TODO

    # attr_in_df = dataset with only that column and the results column
    attr_in_df = df[[attribute]]

    information_gain = get_entropy_of_dataset(df) - get_avg_info_of_attribute(df, attribute)

    return information_gain

#-------------------------------
#input: pandas_dataframe
#output: ({dict},'str')
def get_selected_attribute(df):
    '''
    Return a tuple with the first element as a dictionary which has IG of all columns 
    and the second element as a string with the name of the column selected

    example : ({'A':0.123,'B':0.768,'C':1.23} , 'C')
    '''
    # TODO
    getCount(df)
    pass
# --------------------------------------------------
def getCount(df):
    '''returns number of times the each class we want'''
    print("in getCount")
    #TODO
        #  extract types of classes forst
    # In iloc, [initial row:ending row, initial column:ending column]
    last = df.columns.values[-1]
    categories = {key:0 for key in df[last].unique()}
    print(categories)

    # iterate over each of these classes to get count
    for categ in categories.keys():
        countpercateg = 0
        minidf = df[df[last] == categ]
        countpercateg = len(minidf)
        categories[categ] = countpercateg

    print(categories)

    return categories