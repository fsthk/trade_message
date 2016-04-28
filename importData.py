# -*- coding: UTF-8 -*-
# dataをインポートする

import numpy as np
import pandas as pd
import os
import savefiles

# dataの置き場情報の設定
script_dir = os.path.abspath(os.path.dirname(__file__))
data_dir = "%s\data" % script_dir

# ファイルの読み込み
data = pd.DataFrame(index=[], columns=[])
for i in range(1, 4):
    file_name = "2016%02d.csv" % i
    data_tmp = pd.read_csv("%s\%s" % (data_dir, file_name))
    # data_tmp.index = ["%d" % i]
    # data.append(data, data_tmp)
    data = pd.concat([data, data_tmp], axis=0)
data.sort_index(axis=0)
print data

calcSMA.py(data)

# fileへ書き出し
# savefiles.saveCSV(data)
