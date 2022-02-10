# # 一次性读取所有内容 - read() 或者 reedlines()
# # with open('C:\\Users\\zhangxuan17\\Desktop\\data.txt','r') as f:
# #     data = f.read()
# #     print(data)

# # 按行读取
# # with open('C:\\Users\\zhangxuan17\\Desktop\\data.txt', 'r') as f:
# #     data = f.readlines()
# #     print(data)

# classmates = ["name1", "name2", "name3"]
# #len获取当前列表的元组个数
# print("当前列表中的元素个数1 = " + str(len(classmates))) 

# #append在当前列表的基础上追加元素
# classmates.append("name4") 
# classmates.append("name4")
# print("当前列表中的元素个数2 = " + str(len(classmates)))

# #count统计某个元素在列表中出现的次数
# count = classmates.count("name4") 
# print("count = " + str(count))

# #index统计某个元素的下标
# index = classmates.index("name4")
# print("index = " + str(index))

# # insert将某一元素插入到列表的某一位置
# classmates.insert(0, "name5")
# print(classmates)

# # pop移除列表中的一个元素（默认是最后一个）
# classmates.pop(0)
# print(classmates)

# # remove移除与列表中元素匹配的元素
# classmates.remove("name2")
# print(classmates) 

# #reverse 反转列表元素的顺序
# classmates.reverse()
# print(classmates)

# num1 = [2,1,4,6,5]
# num2 = ["11","22","33", "44"]
# num1.sort()
# num1.extend(num2)
# print("num1 = " + str(num1))
# print("num2 = " + str(num2))

# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]
# # 打印Apple:
# print(L[0][0])

# # 打印Python:
# print(L[1][1])

# # 打印Lisa:
# print(L[2][2])


#条件判断
# years = input("please input your birth: ")

# if int(years) > 1999:
#     print("00后")
# elif int(years) <= 1999:
#     print("00前") 
# else:
#     print("else")

# weight = 80.5
# height = 1.75

# bmi = weight/(height * height)
# if bmi < 18.5:
#     print("过轻")
# elif bmi < 25 and bmi > 18.5:
#     print("正常")
# elif bmi > 25 and bmi < 28:
#     print("过重")
# elif bmi > 28 and bmi < 32:
#     print("肥胖")
# else:
#     print("严重肥胖") 

# intervals = [[2,6],[1,3],[8,10],[15,18]]
# intervals.sort()
# print(intervals)

# 两数之和
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: