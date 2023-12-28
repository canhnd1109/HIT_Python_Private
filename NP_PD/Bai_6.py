import numpy as np
import pandas as pd
N = 50

# Tạo mảng numpy với kích thước 50x7
data = np.zeros((N, 7), dtype='object')

# Tuổi: random trong khoảng [18:22]
data[:, 0] = np.random.randint(18, 23, size=N)

nganh_values = ["CNTT", "KTPM", "KHMT", "HTTT", "CNDPT"]
data[:, 1] = np.random.choice(nganh_values, size=N)

# Typing
data[:, 2] = np.random.choice([np.nan, *np.arange(11)], size=N)

# Lập trình thi đấu
data[:, 3] = np.random.choice([np.nan, *np.arange(11)], size=N)

# Web
data[:, 4] = np.random.choice([np.NAN, *np.arange(11)], size=N)

# AI-Tank
data[:, 5] = np.random.choice([np.NAN, *np.arange(11)], size=N)

# Rung chuông vàng
data[:, 6] = np.random.choice([np.NAN, *np.arange(11)], size=N)

# Tạo DataFrame từ mảng numpy
columns = ["Tuổi", "Ngành", "Typing", "Lập trình thi đấu", "Web", "AI-Tank", "Rung chuông vàng"]
df = pd.DataFrame(data, columns=columns)

# In ra kết quả
print(df.head())

# Thêm cột mới là ID”, “Tổng cuộc thi” (những giá trị NaN là member không tham gia thi cuộc thi đó), “Tổng điểm”.
df['Tổng cuộc thi'] = df.iloc[:, 2:].notna().sum(axis=1)
df['Tổng điểm'] = df.iloc[:, 2:].sum(axis=1, skipna=True)
df['ID'] = np.arange(len(df)) + 2022605692

print(df.head())

df.set_index('ID', inplace=True)  

#  In ra thông tin “ID”, “Tuổi”, “Ngành” của 3 người có tổng điểm cao nhất.
print(df.sort_values(by='Tổng điểm', ascending=False).head(3)[['Tuổi', 'Ngành']])

#  Xác định các bạn ngành “CNTT” có xu hướng tham gia cuộc thi nào.
print(df[df['Ngành'] == 'CNTT'].iloc[:, 2:-2].notna().sum(axis=0).sort_values(ascending=False).head(1))

# * Xác định cuộc thi nào có số lượng tham gia lớn nhất, 
print(df.iloc[:, 2:-2].notna().sum(axis=0).sort_values(ascending=False).head(1))

# cuộc thi nào có số lượng tham gia ít nhất.
print(df.iloc[:, 2:-2].notna().sum(axis=0).sort_values(ascending=False).tail(1))