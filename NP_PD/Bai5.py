import pandas as pd
import matplotlib.pyplot as plt

sale = pd.read_csv('sale.csv')
car = pd.read_csv('car.csv')    
print(sale.head())
print(car.head())
# Tính Tổng số lượng bán ô tô trên thị trường
print("Tổng số lượng bán ô tô trên thị trường là: ",sale['Sales_in_thousands'].sum())

# Tính giá trung bình của ô tô
print("giá trung bình của ô tô là: ",sale['Price_in_thousands'].mean())

# Xác định 10 ID có giá trị bán lại cao nhất và in ra thông tin xe từ DataFrame Car của 10 xe đó.
top10car = sale.sort_values(by='Price_in_thousands', ascending=False).head(10).merge(car, on='ID')
print(top10car)

# Đếm số lượng phương tiện mỗi loại (Passenger, Car)
print("số lượng phương tiện mỗi loại: ",car['Vehicle_type'].value_counts())

# Xác định mode của hãng xe
print("mode của hãng xe",car['Manufacturer'].mode())
# Sắp xếp DataFrame Sale giảm dần theo mức độ ưu tiên số lượng bán, giá bán, giá bán lại dự kiến và in kết quả ra màn hình.
sortDataFrameSale=sale.sort_values(by=['Sales_in_thousands', 'Price_in_thousands', '__year_resale_value'], ascending=False)
print(sortDataFrameSale)

# Gộp 2 DataFrame lại theo thuộc tính “ID” 
sale.merge(car, on='ID')