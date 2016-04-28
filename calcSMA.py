# -*- coding: UTF-8 -*-
# 移動平均を計算する

import numpy as np
import pandas as pd
import importData.py

# 単純移動平均の計算
data = importData.data
sma5 = pd.rolling_mean(data, 5)
sma25 = pd.rolling_mean(data, 25)

# 移動平均（SMA5,SMA25）の大小でタイミング決定用のフラグを立てる
def difference_SMA():
    if sma5 - sma25 > 0:
        flag = 1
    elif sma5 - sma25 < 0:
        flag = -1
    else:
        message()

# flagは過去のフラグと比較するため保存しておく
# 過去のフラグは50件分保持する
bkflag =  flag

# flagが変化した時点でメッセージを投げる
def message(flag, null=None):
    if flag > flag[i-1]:
        buy = 1
    elif flag < flag[i-1]:
        buy = -1
    else:
        return null

# メッセージの内容
def message():


