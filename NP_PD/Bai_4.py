import pandas as pd
import matplotlib.pyplot as plt
# Đọc file và in ra DataFrame
df = pd.read_csv('Car_sales.csv')
print(df.head())
print(df.shape)

# Kiểm tra và điền dữ liệu thiếu ở cột số lượng bán (điền giá trị 0.0), 
df['Sales_in_thousands'].fillna(0.0, inplace=True)
# giá bán lại (điền giá trị trung bình của cột), 
df['__year_resale_value'].fillna(df['__year_resale_value'].mean(), inplace=True)

# giá của ô tô (điền median của cột), 
df['Price_in_thousands'].fillna(df['Price_in_thousands'].median(), inplace=True)

# in ra màn hình vị trí thiếu dữ liệu và DataFrame kết quả .
print(df.head())



df['Latest_Launch']=pd.to_datetime(df['Latest_Launch'])
print(df.info())


# Kiểm tra và xóa các dòng trùng lặp dữ liệu trong DataFrame. In ra số dòng trùng lặp và DataFrame kết quả.

# Check for duplicate rows
duplicate_rows = df.duplicated()

# Count the number of duplicate rows
num_duplicate_rows = duplicate_rows.sum()
print("Number of duplicate rows:", num_duplicate_rows)

# Remove duplicate rows
df = df.drop_duplicates()

# Print the resulting DataFrame
print(df)

# Thêm cột mới tên “ID” dạng “manufacturer_model”, in cột đó ra màn hình.
df['ID'] = df['Manufacturer'] + '_' + df['Model']
print(df['ID'])

# Tách DataFrame thành 2 DataFrame khác: Sale (lưu thuộc tính “ID”, “Sales_in_thousands”, “year_resale_value”, “price_in_thousands”), Car (lưu Series “ID” và Series còn lại).
sale = df[['ID', 'Sales_in_thousands', '__year_resale_value', 'Price_in_thousands']]
car = df.drop(['Sales_in_thousands', '__year_resale_value', 'Price_in_thousands'], axis=1)

print(sale.head())
print(car.head())

# Lưu 2 DataFrame sau khi clean vào file sale.csv và car.csv
sale.to_csv('./sale.csv', index=False)
car.to_csv('./car.csv', index=False)
