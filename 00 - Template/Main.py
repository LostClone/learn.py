#casting = changing data types

#integer
print("===int===")
data_int = 1;
print("Data :", data_int)
print("Tipe Data", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) # false if 0 else true

print("Data =", data_float, ", Tipe Data =", type(data_float))
print("Data =", data_str, ", Tipe Data =", type(data_str))
print("Data =", data_bool, ", Tipe Data =", type(data_bool))

#float
print("===float===")
data_float = 8.9;
print("Data :", data_float)
print("Tipe Data", type(data_float))

data_int = int(data_float) # rounded down
data_str = str(data_float)
data_bool = bool(data_float) # false if 0 else true

print("Data =", data_int, ", Tipe Data =", type(data_int))
print("Data =", data_str, ", Tipe Data =", type(data_str))
print("Data =", data_bool, ", Tipe Data =", type(data_bool))

#Boolean
print("===bool===")
data_bool = 1
print("Data :", data_bool)
print("Tipe Data", type(data_bool))

data_float = float(data_bool)
data_str = str(data_bool)
data_int = str(data_bool) # false if 0 else true

print("Data =", data_float, ", Tipe Data =", type(data_float))
print("Data =", data_str, ", Tipe Data =", type(data_str))
print("Data =", data_bool, ", Tipe Data =", type(data_bool))

#string
print("===str===")
data_str = "2" #str must be number to be changed
print("Data :", data_str)
print("Tipe Data", type(data_str))

data_float = float(data_str)
data_int = int(data_str)
data_bool = bool(data_str) # if string is filled true else false

print("Data =", data_float, ", Tipe Data =", type(data_float))
print("Data =", data_str, ", Tipe Data =", type(data_str))
print("Data =", data_bool, ", Tipe Data =", type(data_bool))