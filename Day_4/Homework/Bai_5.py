def flatten_list(nested_list): 
    flattened_list = [] 
    for item in nested_list:
        if isinstance(item, list): 
            flattened_list.extend(flatten_list(item))
        else: flattened_list.append(item)
    return flattened_list

print(flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]])) 

# Chỗ này em cần tìm hiểu thêm
# import numpy as np
# arr = np.array([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]])
# arr = np.array([[0, 10, 40], [20, 30,50], [60, 70, 80], [90, 100, 110]])
# flattened_arr = arr.flatten()
# print(flattened_arr)
