#coding:utf-8

#请问Python如何实现将列表：['a','a','b','a','b','c']输出为字典：{'a':3,'b':2,'c':1}?
#import sort as sort

# list_str = ["a","a","b","b","c","c"]
# d = {}
# d_key = set(list_str).sort()
# print(d_key)
# print(set(list_str))

resource = ['a', 'a', 'b', 'a', 'b', 'c']
dic = {}
for element in resource:
    result = dic.get(element, -1)
    if -1 == result:
        dic[element] = 1
        print(dic)
    else:
        dic[element] = dic[element] + 1
        print(dic)
