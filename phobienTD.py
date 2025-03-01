import pandas as pd
from collections import Counter
from itertools import combinations

# Đọc dữ liệu từ file Excel
file_path = "data_demo.xlsx"  # Đổi thành đường dẫn thực tế
sheet_name = "Sheet1"  # Đổi nếu cần

df = pd.read_excel(file_path, sheet_name=sheet_name)

# Bước 1: Nhóm sản phẩm theo mã hóa đơn
grouped = df.groupby("mã hóa đơn")["tên sản phẩm"].apply(set)

# Bước 2: Đếm tần suất xuất hiện của từng tập sản phẩm
counter = Counter()
for items in grouped:
    items = sorted(items)
    for i in range(1, len(items) + 1):
        for subset in combinations(items, i):
            counter[subset] += 1

# Bước 3: Chọn tập phổ biến dựa trên ngưỡng hỗ trợ
min_support = 50  # Điều chỉnh nếu cần
frequent_itemsets = {k: v for k, v in counter.items() if v >= min_support} # Lọc ra sản phẩm >= min

# Bước 4: Tìm tập phổ biến tối đại
def is_subset(smaller, larger_sets):
    for large in larger_sets:
        if set(smaller).issubset(set(large)):
            return True
    return False

maximal_frequent_itemsets = {}
for itemset, count in frequent_itemsets.items():
    if not is_subset(itemset, frequent_itemsets.keys() - {itemset}):
        maximal_frequent_itemsets[itemset] = count

# Xuất kết quả tập phổ biến tối đại ra file JSON
import json
output_file = "maximal_frequent_itemsets.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(
        {"maximal_frequent_itemsets": [[list(k), v] for k, v in maximal_frequent_itemsets.items()]},
        f, ensure_ascii=False, indent=4
    )
