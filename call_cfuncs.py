import os
import ctypes
import numpy as np

# cc -Wall -o cfuncs cfuncs.c
# cc -fPIC -shared -o cfuncs.so cfuncs.c

# load c library
so_file = os.getcwd() + "/cfuncs.so"
c_funcs = ctypes.CDLL(so_file)

# wrapper functions to call cfuncs

def c_square(int1):
    return c_funcs.square(ctypes.c_int(int1))

def c_multiply(float1, float2, float3):
    c_funcs.multiply.restype = ctypes.c_float  # set result type
    return c_funcs.multiply(ctypes.c_float(float1), ctypes.c_float(float2), ctypes.c_float(float3))

def c_caps(str1):
    # encode the original str to get bytes for string_buffer
    mutable_string = ctypes.create_string_buffer(str.encode(str1))
    c_funcs.caps(mutable_string)
    return mutable_string.value

def c_dot_prod(a1, a2):
    c_funcs.dot_prod.restype = ctypes.c_float  # set result type
    c_float_p = ctypes.POINTER(ctypes.c_float)  # substantiate pointer object

    # array 1
    a1 = np.array(a1).astype(np.float32)  # convert into np-1d float32 array
    a1_p = a1.ctypes.data_as(c_float_p)  # marshall into pointer
    # array 2
    a2 = np.array(a2).astype(np.float32)  # convert into np-1d float32 array
    a2_p = a2.ctypes.data_as(c_float_p)  # marshall into pointer
    # dot product
    return c_funcs.dot_prod(a1_p, len(a1), a2_p, len(a2))

def c_returna(a1):
    c_float_p = ctypes.POINTER(ctypes.c_float)  # substantiate pointer object
    c_funcs.return_a.restype = np.ctypeslib.ndpointer(dtype=ctypes.c_float, shape=(len(a1),))  # set result type
    a1 = np.array(a1).astype(np.float32)  # convert into np-1d float32 array
    a1_p = a1.ctypes.data_as(c_float_p)  # marshall into pointer
    return c_funcs.return_a(a1_p)

def c_hadamard_1d(a1, a2):
    c_float_p = ctypes.POINTER(ctypes.c_float)  # substantiate pointer object
    c_funcs.hadamard_1d.restype = np.ctypeslib.ndpointer(dtype=ctypes.c_float, shape=(len(a1),))  # set result type

    # return array
    ar = np.empty_like(a1)  # init
    ar_p = ar.ctypes.data_as(c_float_p)  # marshall into pointer
    # array 1
    a1 = np.array(a1).astype(np.float32)  # convert into np-1d float32 array
    a1_p = a1.ctypes.data_as(c_float_p)  # marshall into pointer
    # array 2
    a2 = np.array(a2).astype(np.float32)  # convert into np-1d float32 array
    a2_p = a2.ctypes.data_as(c_float_p)  # marshall into pointer
    # multiply
    return c_funcs.hadamard_1d(a1_p, len(a1), a2_p, len(a2), ar_p)

print(c_square.__name__)
print(c_square(10))

print(c_multiply.__name__)
print(c_multiply(7.5, 8.5, 9.5))

print(c_caps.__name__)
print(c_caps("testabc1"))

print(c_dot_prod.__name__)
print(c_dot_prod([1,2], [1,2]))

print(c_returna.__name__)
print(c_returna([1.5,2]))

print(c_hadamard_1d.__name__)
print(c_hadamard_1d([1.5,2], [1.5,2]))