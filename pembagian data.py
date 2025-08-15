#tipe data: angka satuan (integer)
data_integer = 10000
print("data :", data_integer,)
print("- bertipe :", type( data_integer))

#tipe data: angka dengan koma (float)
data_float = 1,5
print("data :", data_float,)
print("- bertipe :", type( data_float))

#tipe data: kumpulan karakter (string)
data_string = "markucup"
print("data :", data_string,)
print("- bertipe :", type( data_string))

#tipe data: biner true/false (bolean)
data_bool = True
print("data :", data_bool,)
print("- bertipe :", type( data_bool))

##tipe data khusus

#bilangan kompleks
data_complex = complex (5,6)
print("data :", data_complex,)
print("- bertipe :", type( data_complex))

#tipe data dari bahasa C
from ctypes import c_double
data_c_double = c_double (10.5)
print("data :", data_c_double,)
print("- bertipe :", type( data_c_double))

#data casting
#merubah dari satu tipe ke tipe lain
#tipe data = int,float,str,bool

##INTEGER
print("====DATA INTEGER====")
data_int = 9;
print ("data = ", data_int, "tipe =",type (data_int))

data_float = float(data_int)
data_string = str(data_int)
data_bool = bool(data_int)# akan false jika nilai int = 0
print ("data = ", data_float, "tipe =",type (data_float))
print ("data = ", data_string, "tipe =",type (data_string))
print ("data = ", data_bool, "tipe =",type (data_bool))

##FLOAT
print("====DATA FLOAT====")
data_float = 9.5;
print ("data = ", data_float,"tipe =",type (data_float))

data_int = int(data_float)# akan di bulatkan kebawah
data_string = str(data_float)
data_bool = bool(data_float)# akan false jika nilai int = 0
print ("data = ", data_int, "tipe =",type (data_int))
print ("data = ", data_string, "tipe =",type (data_string))
print ("data = ", data_bool, "tipe =",type (data_bool))


##BOOLEAN
print("====DATA BOOLEAN====")
data_bool = True;
print ("data = ", data_bool,"tipe =",type (data_bool))

data_int = int(data_bool)# akan di bulatkan kebawah
data_string = str(data_bool)
data_float = float(data_bool)# akan false jika nilai int = 0
print ("data = ", data_int, "tipe =",type (data_int))
print ("data = ", data_string, "tipe =",type (data_string))
print ("data = ", data_float, "tipe =",type (data_float))


##STRING
print("====DATA STRING====")
data_string = "10";
print ("data = ", data_string,"tipe =",type (data_string))

data_int = int(data_string)# string harus angka
data_float = float(data_string)# string harus angka
data_bool = str(data_string)# false jika string kosong
print ("data = ", data_int, "tipe =",type (data_int))
print ("data = ", data_float, "tipe =",type (data_float))
print ("data = ", data_bool, "tipe =",type (data_bool))