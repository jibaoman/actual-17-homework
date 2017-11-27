#coding=utf-8
import random


#定义三个变量，number0表示最大值，number1表示次大值，number2为中间变量临时存储次大值
#初始化number0和number1的值为0


#使用for循环生成5组int型数字用于比较大小
for i in range(5):
  number=random.randint(0,1000)
  if(i==0):
    number0=number #定义变量number0表示最大值
    number1=number #定义变量number1number1表示次大值
  print "第",i+1,"组随机数字是：",number 
  if(number>=number0):
    number0=number
  elif(number<=number1):
    number1=number
  print "第",i+1,"次比较后的结果是：最大值是",number0, "最小值是",number1
  print "----------------------------------------------------"
  print " "
