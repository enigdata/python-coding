# The memory need is doubled if you use int64. Ask this question to yourself; which data type would suffice? 
# Until your numbers are higher than 2,147,483,648 and lower than -2,147,483,647, using int32 is enough.
import numpy as np 

x = np.array([[1,2,3],[4,5,6]], dtype = np.int64)
x_copy = np.array(x, dtype=np.float)
x_copy_int = x_copy.astype(np.int)

# Please keep in mind that when you use the astype attribute, it doesn't change the dtype of the x_copy, 
# even though you applied it to x_copy. It keeps the x_copy, but creates a x_copy_int

Data_Cancer = np.random.rand(100000, 100)
print(Data_Cancer.dtype)
print(Data_Cancer.nbytes)
Data_Cancer_new = np.array(Data_Cancer, dtype=np.float32)
print(Data_Cancer_new.nbytes)

# As you can see from the preceding code, their size decreases from 80 MB to 40 MB just by changing the dtype. 
# What we get in return is less precision after decimal points. 
# Instead of being precise to 16 decimals points, you will have only 7 decimals. 
# In some machine learning algorithms, precision can be negligible. 
# In such cases, you should feel free to adjust your dtype so that it minimizes your memory usage.

my_list = [2,14,6,8]
my_array = np.array(my_list)

#Vectorized operations
my_array + 2 
my_array * 2 
my_array / 2 

second_array = np.zeros(4) + 3 
my_array - second_array

###Identity matrix
identity_array = np.identity(4)

identity_array + 4 

my_array - identity_array

