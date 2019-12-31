# 載入可產生隨機變數的函式庫
import random
# 建立一個未存放號碼的串列
List = [0, 0, 0, 0, 0, 0]
# 透過迴圈產生六個號碼
for i in range(0, 6, 1):
    # 隨機產生1~49的任一整數
    number = random.randint(1, 49)
    # 將數字存放到矩陣中
    List[i] = number
# 列印出結果
print(List)