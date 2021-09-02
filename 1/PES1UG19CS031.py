#This weeks code focuses on understanding basic functions of pandas and numpy 
#This will help you complete other lab experiments


# Do not change the function definations or the parameters
import numpy as np
import pandas as pd

#input: tuple (x,y)    x,y:int 
def create_numpy_ones_array(shape):
    #return a numpy array with one at all index
    array=None
    #TODO
    if type(shape)==tuple:
        arr = []
        x,y = shape
        for i in range(x):
            arr.append(np.ones(y, int))
        array = np.array(arr)
    return array

#input: tuple (x,y)    x,y:int 
def create_numpy_zeros_array(shape):
    #return a numpy array with zeros at all index
    array=None
    #TODO
    if type(shape)==tuple:
        arr = []
        x,y = shape
        for i in range(x):
            arr.append(np.zeros(y, int))
        array = np.array(arr)
        # print(array)
    return array

#input: int  
def create_identity_numpy_array(order):
    #return a identity numpy array of the defined order
    array=None
    #TODO
    a = create_numpy_zeros_array((order,order))
    # print(a)
    for i in range(order):
        a[i][i] = 1
    # print(a)
    array = np.array(a)
    return array

#input: numpy array
def matrix_cofactor(array):
    #return cofactor matrix of the given array
    #TODO
    x,y=array.shape
    if x==y:
        a = np.linalg.inv(array).T * np.linalg.det(array)
    else:
        print("array is not square")
    # print(a)
    return a

#Input: (numpy array, int ,numpy array, int , int , int , int , tuple,tuple)
#tuple (x,y)    x,y:int 
def f1(X1,coef1,X2,coef2,seed1,seed2,seed3,shape1,shape2):
    #note: shape is of the forst (x1,x2)
    #return W1 x (X1 ** coef1) + W2 x (X2 ** coef2) +b
    # where W1 is random matrix of shape shape1 with seed1
    # where W2 is random matrix of shape shape2 with seed2
    # where B is a random matrix of comaptible shape with seed3
    # if dimension mismatch occur return -1
    ans=None
    #TODO
    row1, col1 = shape1
    row2, col2 = shape2

    # raises np array X1 and X2 to the power coef1 or coef2
    M1 = np.power(X1, coef1)
    # print('A1', M1)
    M2 = np.power(X2, coef2)
    # print('A2', M2)

    mrow1, mcol1 = M1.shape
    mrow2, mcol2 = M2.shape
    if (col1 != mrow1) or (col2 != mrow2):
        # print('dimension error')
        return -1

    # generate matrices W1 W2 using respective seeds
    np.random.seed(seed1)
    W1 = np.random.rand(row1, col1)
    np.random.seed(seed2)
    W2 = np.random.rand(row2, col2)
    
    # A = W1 x (X1 ** coef1) + W2 x (X2 ** coef2)
    a1 = np.matmul(W1, M1)
    a2 = np.matmul(W2, M2)

    if a1.shape != a2.shape:
        return -1
    else:
        A = a1 + a2 

    Brow, Bcol = A.shape 
    np.random.seed(seed3)
    B = np.random.rand(Brow, Bcol)

    ans = A + B
    return ans

def fill_with_mode(filename, column):
    """
    Fill the missing values(NaN) in a column with the mode of that column
    Args:
        filename: Name of the CSV file.
        column: Name of the column to fill
    Returns:
        df: Pandas DataFrame object.
        (Representing entire data and where 'column' does not contain NaN values)
        (Filled with above mentioned rules)
    """
    df=None
    df=pd.read_csv(filename)

    # why the '[0]'? 
    # .mode() returns a series regardless whether one value is returned. so [0] selects the firzt one in the series.
    # print(df.columns.tolist())
    # for attribute in df.columns.tolist():
    df1 = df.copy()
    mode = df[column].mode()[0]
    df[column].fillna(mode, inplace=True)

    return df

def fill_with_group_average(df, group, column):
    """
    Fill the missing values(NaN) in column with the mean value of the 
    group the row belongs to.
    The rows are grouped based on the values of another column

    Args:
        df: A pandas DataFrame object representing the data.
        group: The column to group the rows with
        column: Name of the column to fill
    Returns:
        df: Pandas DataFrame object.
        (Representing entire data and where 'column' does not contain NaN values)
        (Filled with above mentioned rules)
    """
    df[column].fillna(df.groupby(group)[column].transform('mean'), inplace=True)
    return df


def get_rows_greater_than_avg(df, column):
    """
    Return all the rows(with all columns) where the value in a certain 'column'
    is greater than the average value of that column.

    row where row.column > mean(data.column)

    Args:
        df: A pandas DataFrame object representing the data.
        column: Name of the column to fill
    Returns:
        df: Pandas DataFrame object.
    """
    # print(df)

    mean = df[column].mean()
    df = df[mean < df[column]]
    return df