#!/usr/bin/python
#--*-- coding:UTF-8 -*--

from math import sqrt
from itertools import permutations
import time

#### 输入一个集合，将集合转为一个包含2位数字的集合list1 、包含3位数字的集合list2
def convNum2List(num):
    strlist = list(str(num)) ### 将数字转换为单个字符组成的list
    strlist *= 3     ### 将每个字符都重复3次 ，因为组成的3位数有可能重复
    list2 = chkValue(list(permutations(strlist,2)))  ### 生成包含2位数字的字符集合
    list3 = chkValue(list(permutations(strlist,3)))  ### 生成包含3位数字的字符集合
          
    
   # print "list2: ",list2
   # print "list3: ", list3
    return list2,list3


### 判断list 中的元素是否有效，去掉以0开头的数值，同时，将字符list转换成int类型的list,此外，需要将结果去重
def chkValue(param):
    res = []  ### int 类型的 list
    for item in param:
        if item[0] != '0':
          res.append(convChrList2Int(item))

    uniq = set(res) ### 结果去重
    return list(uniq)  ### 转为list类型


### 将字符list转换成int ###
def convChrList2Int(param):
    str = ""
    value =  int(str.join(param))
    return value


### 将数字转换为字符的set集合 
def getSet(value):
    strlist = list(str(value))
    return set(strlist)

### 判断集合s2是否包含于s1 
def chkSetRelation(s1,s2):
    if s1&s2 == s2 :
 	 return True
    else:
         return False


#### 格式化输出 默认长度为6位 ,默认的占位字符为.
def formatOutput(str,flag = 0 , length = 6, chr = ".",roffset = 1):   #### flag : 对齐方式 0表示右对齐 ，1表示左对齐，2表示中间对齐
      resStr = ""
      if flag == 0 :
          resStr = str.rjust(length,chr)   
      elif flag == 1:
          resStr = str.ljust(length,chr)
      else:
          resStr = (str.ljust((roffset + len(str)) , chr)).rjust(length,chr)
 
      return resStr

#### 计算两个数相乘，得到的中间结果 
def getCalcPro(setInput,i3 ,i2):  ### i3 表示长度为3的整数，i2表示长度为2的整数
    d1 = i2%10    ## 个位数的数值
    d2 = i2/10    ## 十位数上的数值
    m1 = i3 * d1  ## 个位与被乘数相乘
    m2 = i3 * d2  ## 十位与被乘数相乘
    result = i3 * i2
    localstr = ""

    s1 = getSet(m1)
    s2 = getSet(m2)
    if chkSetRelation(setInput,s1) and chkSetRelation(setInput,s2):
        localstr += formatOutput(str(i3), chr = " ") + "\n"
        localstr += formatOutput(str(i2), chr = " ") + "\n"
        localstr += formatOutput(str(m1), chr = " ") + "\n"
        localstr += formatOutput(str(m2),2, chr = " ") + "\n"
        localstr += formatOutput("-",length = 10 , chr = "-") + "\n"
        localstr += formatOutput(str(result), chr = " ") + "\n"

    return localstr


#### 计算3位数*2位数，是否满足竖式的要求  
def chkCalcStr(inputNum,lst2,lst3):
     setInput = getSet(inputNum)  ### 输入数的字符集合
     cnt = 0            ### 解的个数
     resStr = ""        ### 最后的竖式输出表达式
     resList = []       ### 存储哪些值可以被拆分

     for i in lst3:  ### 3位数字的list
         for j in lst2:  ### 2位数字的list
            curRes = i * j
            multiSet = getSet(curRes)   ### 求乘积的set集合
            if chkSetRelation(setInput,multiSet) : ### 如果乘积的set集合包含在输入数值的集合中，则进一步判断乘积过程中的每一个步骤是否都满足竖式的要求
                 curStr = getCalcPro(setInput,i,j)
                 if curStr != None and len(curStr) > 0:
                      cnt += 1
                      prefix  = "序号：" + str(cnt) + "\n" 
                      surfix = "\n"
                      resStr += prefix + curStr + surfix
                      resList.append(curRes)

     resStr += "\n 您输入的数值为: " + str(inputNum)
     resStr += "\n 符合条件的总数: " + str(cnt) 
     resStr += "\n 分别为: " + str(resList)
     return resStr

############ 主程序  ##################

inputNum = raw_input()
starttime =  time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
print "start time :" ,starttime

if not inputNum.isdigit() : 
    print "输入错误" ,type(inputNum)
else:
    lst1,lst2 = convNum2List(inputNum)
    str = chkCalcStr(inputNum,lst1,lst2)
    print str

endtime =  time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print "end time :" ,endtime

