def print_name(arg1,arg2):
   print(arg1,arg2)

#calling 1
print_name("ABCD","XYZ")

#calling 2
v=["ABCD1","xyz1"]
print_name(v[1],v[0])

#calling 3
print_name(*v)

v=("ABCD2","XYZ2")
print_name(v[0],v[1])
print_name(*v)

v={"ABCD3","XYZ3"}
print_name(*v)


