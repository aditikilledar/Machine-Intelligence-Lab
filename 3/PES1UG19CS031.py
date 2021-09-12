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
# print("HI!")

#-------------------------------
def get_entropy_of_dataset(df):
    # TODO
    # print("getting entropy...")
    categcount = getCount(df)
    total = float(sum(categcount.values()))
    # print(categcount)

    # print(total, 'is total')
    # E(S) = -aloga-blogb
    entropy = 0

    for key in categcount.keys():
        a = (float(categcount[key])/total)
        if a != 0:
            val = a*(math.log(a,2))
            entropy -= val

    # print(entropy, "is entropy")

    return entropy

#-------------------------------
'''Return avg_info of the attribute provided as parameter'''
# input:pandas_dataframe,str   {i.e the column name ,ex: Temperature in the Play tennis dataset}
# output:int/float
def get_avg_info_of_attribute(df, attribute):
    # TODO
    avg_info = 0

    # print(f"--------------{attribute}-------------")

    totaldf = getCount(df)
    total = float(sum(totaldf.values()))

    for subatt in df[attribute].unique():
        # avg_info
        minidf = df[df[attribute] == subatt]
        minicategories = getCount(minidf)
        # print(subatt)
        # print("minidf", minidf, minicategories)

        # proportion = (float(sum(minicategories.values())) / float(sum(total.values())))
        proportion = (float(len(minidf)) / total)
        # print(proportion, "is proportion")

        value = proportion * get_entropy_of_dataset(minidf)
        # print(f"{proportion}*{get_entropy_of_dataset(minidf)}")
        avg_info += value
        # print(avg_info, "avg info!")

    return avg_info

#-------------------------------
'''Return Information Gain of the attribute provided as parameter'''
# input:pandas_dataframe,str
# output:int/float
def get_information_gain(df, attribute):
    # TODO

    # attr_in_df = dataset with only that column and the results column
    # attr_in_df = df[[attribute]]

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
    # getCount(df)
    information_gains = dict()
    attrNames = (df.iloc[:,:-1]).columns.values
    for each in attrNames:
        information_gains[each] = get_information_gain(df, each)

    # Step 2 : pick biggest
    selected_column = max(information_gains, key=information_gains.get)
    finalans = (information_gains, selected_column)
    # print(finalans)
    return finalans
# --------------------------------------------------
def getCount(df):
    '''returns number of times the each class we want'''
    # print("in getCount")
    #TODO
        #  extract types of classes forst
    # In iloc, [initial row:ending row, initial column:ending column]
    last = df.columns.values[-1]
    categories = {key:0 for key in df[last].unique()}
    # print(categories)

    # iterate over each of these classes to get count
    for categ in categories.keys():
        countpercateg = 0
        minidf = df[df[last] == categ]
        countpercateg = len(minidf)
        categories[categ] = countpercateg

    # print(categories)

    return categories

    # ---------------------------------------------