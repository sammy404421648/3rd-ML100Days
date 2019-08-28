
#%%
# import 是 Python 載入套件的基本語法 (類似 C 語言的 include), 後面接要載入的套件
# import AAAAA as BB, 其中 BB 是代稱, 表示除了載入 AAAAA 之外, 之後都可以用 BB 代替 AAAAA 這個名稱
# 常用套件往往有其對應代稱, numpy的代稱是np, pandas的代稱是pd, matplotlib.pyplot的代稱是plt
# numpy 常用於數值/陣列運算, pandas 擅長資料格式的調整, matplotlib 擅長繪圖
import numpy as np
import matplotlib.pyplot as plt
# Python 的變數不須宣告, 可能是文字, 數值, 陣列, 甚至是物件, 對初學者來說這往往是最難接受的地方
# 主要是 Python 在大多數情況下, 可以由運算"猜"出你想要的型態, 我們由下列語法看看發生了什麼事吧
# w, b 是數值
w = 3
b = 0.5

# 這邊的 y_hat, 就沒有隨機的部分了, 也就是下圖中的紅色實線部分
y_hat = x_lin * w + b
plt.plot(x_lin, y, 'b.', label = 'data')
# 上面的 'b.' 是藍色點狀, 下面的 'r-' 是紅色線狀, label 是圖示上的名稱
plt.plot(x_lin, y_hat, 'r-', label = 'prediction')
plt.title("Assume we have data points (And the prediction)")
plt.legend(loc = 2)
plt.show()

# Python 的函數是另一個新手上手的困難點, 由def開頭, 依序是函數名稱 / 輸入值, 冒號(:)結尾
# 最難讓人習慣的是 Python 的函式與條件判斷, 前後都沒有大括弧(其他程式常見), 而是以四格空白縮排來取代
# 以本例來說, mean_absolute_error 這個函數的定義範圍到 return mae 為止, 因為中間都是縮排, 而 """ 是多行註解(井號是單行註解)
# 函數中, sum(), abs(), len() 都是 Python 原有的方法, 因此可以直接呼叫
def mean_absolute_error(y, yp):
    """
    計算 MAE
    Args:
        - y: 實際值
        - yp: 預測值
    Return:
        - mae: MAE
    """
    # MAE : 將兩個陣列相減後, 取絕對值(abs), 再將整個陣列加總成一個數字(sum), 最後除以y的長度(len), 因此稱為"平均絕對誤差"
    mae = MAE = sum(abs(y - yp)) / len(y)
    return mae

# 呼叫上述函式, 傳回 y(藍點高度)與 y_hat(紅線高度) 的 MAE
MAE = mean_absolute_error(y, y_hat)
print("The Mean absolute error is %.3f" % (MAE))

def mean_square_error(y,yp):
    mse=sum((y-yp)**2)/len(y)
    return mse

MSE=mean_square_error(y,y_hat)
print("The Mean square error is %.3f" % (MSE))



#%%

#!/usr/bin/env python
# coding: utf-8

# In[1]:


作業2：申論題目可直接將答案回覆在HW檔案裡面，Jupyter notebook可直接編輯文字。
請上 Kaggle, 在 Competitions 或 Dataset 中找一組競賽或資料並寫下：

資料:https://www.kaggle.com/c/titanic/overview
主題:Titanic: Machine Learning from Disaster
        
1. 你選的這組資料為何重要

預測哪些群組為在船難中最容易生存

2. 資料從何而來 (tips: 譬如提供者是誰、以什麼方式蒐集)

Kaggle competitions

3. 蒐集而來的資料型態為何

  結構化:PassengerId,Survived,Pclass,Age,SibSp,Parch,Fare
非結構化:Name,Sex,Ticket,Cabin,Embarked
註:
PassengerId:乘客座號
Survived:存活(1)、死亡(0)
Pclass:社會地位
Name:姓名
Sex:性別
Age:年齡
SibSp:船上兄弟姐妹/配偶人數
Parch:船上父母/小孩人數
Ticket:船票編號
Fare:票價
Cabin:艙號
Embarked:上船港口(C:Cherbourg,S:Southampton,Q:Queenstown)

4. 這組資料想解決的問題如何評估

此問題為分類問題(二分類)，可利用羅吉斯回歸


# In[2]:


作業3：申論題目可直接將答案回覆在HW檔案裡面，Jupyter notebook可直接編輯文字。

想像你經營一個自由載客車隊，你希望能透過數據分析以提升業績，請你思考並描述你如何規劃整體
的分析/解決方案：

1. 核心問題為何 (tips：如何定義 「提升業績 & 你的假設」)

定義:假設總收益超過上個月的10%，則認為提升業績

例:假設上個月業績為NT$10000，令這月的業績為X

Ho:X>=11000
H1:X<11000

2. 資料從何而來 (tips：哪些資料可能會對你想問的問題產生影響 & 資料如何蒐集)

每當乘客下車時，請他掃QRCODE填問卷送折價卷，再由這些製成一份資料進行分析

3. 蒐集而來的資料型態為何

  結構化:車費、司機好感度、等車時間、年齡、收入
非結構化:天氣(晴天、陰天、雨天)、性別、乘車目的(工作、遊玩)

4. 你要回答的問題，其如何評估 (tips：你的假設如何驗證)

車費為連續型，因此為回歸問題，先利用資料做回歸模型，再進行模型診斷，最後針對正係數最高的
幾個做策略
