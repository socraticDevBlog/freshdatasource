import functools 
import operator  


def tupleToString(tuple): 
    str = functools.reduce(operator.add, (tuple)) 
    return str
