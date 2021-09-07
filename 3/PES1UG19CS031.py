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

def getYes(df):
    ''' counts the number of times result was a yes in a df'''
    return len(df[(df['play'] == "yes")])

def getNo(df):
    ''' counts the number of times result was a no in a df'''
    return len(df[(df['play'] == "no")])

def get_entropy_of_dataset(df):
    # TODO

    # E(S) = -aloga-blogb
    # where, a = p/(n+p)
    #    and b = n/(n+p)
    p = getYes(df)
    n = getNo(df)

    print(p, n)

    a = p/(n+p)
    b = n/(p+n)

    entropy = -(a*(math.log(a,2))+(b*(math.log(b,2))))
    
    # print(entropy, "entropy of the system")

    return entropy


'''Return avg_info of the attribute provided as parameter'''
# input:pandas_dataframe,str   {i.e the column name ,ex: Temperature in the Play tennis dataset}
# output:int/float
def get_avg_info_of_attribute(df, attribute):
    # TODO

    # weighted average mean
    sum = 0
    attrList = list(df.columns.values)

    # remove last column of result
    attrList.pop()

    for att in attrList:
        # print("YO MAMA so fat she a", att)



    return avg_info


'''Return Information Gain of the attribute provided as parameter'''
# input:pandas_dataframe,str
# output:int/float
def get_information_gain(df, attribute):
    # TODO

    # attr_in_df = dataset with only that column and the results column
    attr_in_df = df[attribute]
    print("in get IG", attribute, attr_in_df)

    attr_entropy = get_entropy_of_dataset()

    return information_gain




#input: pandas_dataframe
#output: ({dict},'str')
def get_selected_attribute(df):
    '''
    Return a tuple with the first element as a dictionary which has IG of all columns 
    and the second element as a string with the name of the column selected

    example : ({'A':0.123,'B':0.768,'C':1.23} , 'C')
    '''
    # TODO
    pass

# -------------------------------------------------------------------------
outlook = 'overcast,overcast,overcast,overcast,rainy,rainy,rainy,rainy,rainy,sunny,sunny,sunny,sunny,sunny'.split(',')
temp = 'hot,cool,mild,hot,mild,cool,cool,mild,mild,hot,hot,mild,cool,mild'.split(',')
humidity = 'high,normal,high,normal,high,normal,normal,normal,high,high,high,high,normal,normal'.split(',')
windy = 'FALSE,TRUE,TRUE,FALSE,FALSE,FALSE,TRUE,FALSE,TRUE,FALSE,TRUE,FALSE,FALSE,TRUE'.split(',')
play = 'yes,yes,yes,yes,yes,yes,no,yes,no,no,no,no,yes,yes'.split(',')
dataset = {'outlook': outlook, 'temp': temp,'humidity': humidity, 'windy': windy, 'play': play}
df = pd.DataFrame(dataset, columns=['outlook', 'temp', 'humidity', 'windy', 'play'])

print(df)

try:
    if get_entropy_of_dataset(df) >= 0.938 and get_entropy_of_dataset(df) <= 0.942:
        print("Test Case 1 for the function get_entropy_of_dataset PASSED")
    else:
        print("Test Case 1 for the function get_entropy_of_dataset FAILED")
except:
    print("Test Case 1 for the function get_entropy_of_dataset FAILED")

try:
    if get_avg_info_of_attribute(df, 'outlook') >= 0.691 and get_avg_info_of_attribute(df, 'outlook') <= 0.695:
        print("Test Case 2 for the function get_avg_info_of_attribute PASSED")
    else:
        print("Test Case 2 for the function get_avg_info_of_attribute FAILED")

except:
    print("Test Case 2 for the function get_avg_info_of_attribute FAILED")

try:
    if get_avg_info_of_attribute(df, 'temp') >= 0.908 and get_avg_info_of_attribute(df, 'temp') <= 0.914:
        print("Test Case 3 for the function get_avg_info_of_attribute PASSED")
    else:
        print("Test Case 3 for the function get_avg_info_of_attribute FAILED")

except:
    print("Test Case 3 for the function get_avg_info_of_attribute FAILED")

try:
    columns = ['outlook', 'temp', 'humidity', 'windy', 'play']
    ans = get_selected_attribute(df)
    dictionary = ans[0]
    flag = (dictionary['outlook'] >= 0.244 and dictionary['outlook'] <= 0.248) and (dictionary['temp'] >= 0.0292 and dictionary['temp'] <= 0.0296) and (
        dictionary['humidity'] >= 0.150 and dictionary['humidity'] <= 0.154) and (dictionary['windy'] >= 0.046 and dictionary['windy'] <= 0.05) and (ans[1] == 'outlook')
    if flag:
        print("Test Case 4 for the function get_selected_attribute PASSED")
    else:
        print("Test Case 4 for the function get_selected_attribute FAILED")

except:
    print("Test Case 4 for the function get_selected_attribute FAILED")
