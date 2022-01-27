import os
import pandas as pd
import csv

file_name_check = "after_file_list"
file_name_list = os.listdir(file_name_check)

info = pd.read_csv(rf"/Users/hoonjo/Documents/pdf/info.csv",encoding="euc-kr", usecols=["사번", "이름", "주민번호"])
info_list = []
for a in info.itertuples():
    number = a[1]
    name = a[2]
    jumin = a[3]
    set_data = "경진여객"+str(number)+str(name)+str(jumin)+".pdf"
    info_list.append(set_data)

file_name_list_set = set(file_name_list)
info_list_set = set(info_list)
not_file_meaning_list = (info_list_set - file_name_list_set)


result_list = []
for i in not_file_meaning_list:
    result_list.append(f"미제출 :{i}")

for b in file_name_list_set:
    result_list.append(f"제출   :{b}")

print(len(result_list))

for c in result_list:
    print(c)