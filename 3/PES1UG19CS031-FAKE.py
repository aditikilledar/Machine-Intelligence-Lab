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
def getYes(df):
    ''' counts the number of times result was a yes in a df'''
    last = df.columns.values[-1]
    print("last is", last)
    print(df[last])
    yes = sorted(list(df[last].unique()))[1]    
    # print("uniqueword!!", uniqueword, "=", len(df[(df[last] == uniqueword)]))
    return len(df[(df[last] == yes)])

#-------------------------------
def getNo(df):
    ''' counts the number of times result was a yes in a df'''
    last = df.columns.values[-1]
    uniqueword = sorted(list(df[last].unique()))[0]    
    # print("uniqueword!!", uniqueword, "=", len(df[(df[last] == uniqueword)]))
    return len(df[(df[last] == uniqueword)])
# def getNo(df):
#     ''' counts the number of times result was a no in a df'''
#     last = df.columns.values[-1]
#     uniqueword = "no"
#     return len(df[(df[last] == uniqueword)])

#-------------------------------
def get_entropy_of_dataset(df):
    # TODO

    # E(S) = -aloga-blogb
    # where, a = p/(n+p)
    #    and b = n/(n+p)
    p = getYes(df)
    n = getNo(df)

    print(p, n, "(P, N)")

    a = p/(n+p)
    b = n/(p+n)

    if n == 0:
        return -(a*(math.log(a,2)))
    elif p == 0:
        return -(b*(math.log(b,2)))
    else:
        return -(a*(math.log(a,2))+(b*(math.log(b,2))))
    
    return 0

#-------------------------------
'''Return avg_info of the attribute provided as parameter'''
# input:pandas_dataframe,str   {i.e the column name ,ex: Temperature in the Play tennis dataset}
# output:int/float
def get_avg_info_of_attribute(df, attribute):
    # TODO

    # weighted average mean
    sum = 0
    # attrList = list(df.columns.values)
    # remove last column of result
    # result = attrList.pop()
    # print(attrList)
    totalyesno = getYes(df) + getNo(df)
    print("totalyesno", totalyesno)
    attrList = df[attribute].unique()
    print(attrList, "for", attribute)

    for att in attrList:
        # need to do [[blah, blah]] instead of just df[blah, blah] to select multiple columns # NOT NEEDED (idk why i did it)
        # minidf = df[[att, result]]
        print("in subatribute", att)
        minidf = df[df[attribute] == att]
        print("till here 1")
        print("minidf for ", att, "\n", minidf)
        miniyesno = getYes(minidf) + getNo(minidf)
        print("till here 2")
        print(miniyesno, "miniyesno for ", att)
        sum += (miniyesno/totalyesno)*get_entropy_of_dataset(minidf)
        print("till here 3")


    avg_info = sum
    print("Avg info of!!!!!!", attribute, "= ", avg_info)

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
    # # TODO
    # # Step 1 : make dict
    # information_gains = dict()
    # attrNames = (df.iloc[:,:-1]).columns.values
    # for each in attrNames:
    #     information_gains[each] = get_information_gain(df, each)

    # # Step 2 : pick biggest
    # selected_column = max(information_gains, key=information_gains.get)
    # finalans = (information_gains, selected_column)

    # return finalans
    return ()
# --------------------------------------------------