# 載入可產生隨機變數的函式庫
import random
# 建立兩個空串列
List = []
Output = []
# 將List串列依序擺進1~49的數字
for i in range(0, 49, 1):
    List.append(i+1)
# 產生六個號碼並放置Output串列中
for j in range(0, 6, 1):
    # 隨機篹生0~48任一數字，以作為挑選數字之用
    ID = random.randint(0, 48)
    # 挑選數字，並放進Output這一個串列
    Output.append(List[ID])
# 列印出結果
print(Output)