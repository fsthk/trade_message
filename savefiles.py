# -*- coding: UTF-8 -*-
# データをファイルに保存するスクリプト
import csv

#  csv形式で保存
def saveCSV(data):
    with open("data.csv", "w", newline="") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerows(data)

# txt形式で保存


