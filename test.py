# 一次性读取所有内容 - read() 或者 reedlines()
# with open('C:\\Users\\zhangxuan17\\Desktop\\data.txt','r') as f:
#     data = f.read()
#     print(data)

# 按行读取
with open('C:\\Users\\zhangxuan17\\Desktop\\data.txt', 'r') as f:
    data = f.readlines()
    print(data)
    