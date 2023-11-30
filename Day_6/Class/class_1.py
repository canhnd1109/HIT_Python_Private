# def my_function():
# 	' ' 'Demonstrates triple double quotes docstrings and does nothing really' ' '

# 	return None

# print("Using __doc__:")
# print(my_function.__doc__)

# print("Using help:")
# help(my_function)
def ham_ngoai():
    x = "Biến cục bộ"
 
    def ham_trong():
       nonlocal x
       x = "Biến nonlocal"
       print("Bên trong:", x)
 
    ham_trong()
    print("Bên ngoài:", x)

hamngoai()