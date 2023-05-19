# from langchain.document_loaders.csv_loader import CSVLoader

# loader = CSVLoader(file_path='./維修人員助理_db.csv',encoding="utf-8")
# data = loader.load()
# print(data)

import csv
with open('./維修人員助理_db.csv', newline='',encoding="utf-8") as csvfile:

    # 讀取 CSV 檔案內容
    rows = csv.reader(csvfile)

    # 以迴圈輸出每一列
    for row in rows:
        print(type(row[0]))
        if(row[0] == "13"):
            print("ok")