import numpy

def arrays(arr):
    my_array=numpy.array(arr)
    return numpy.reshape(my_array,(3,3))



arr = list(map(int, input(' ').split()))
result = arrays(arr)
print(result)
