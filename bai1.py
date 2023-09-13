print ("xin chao")
a = 1
print(a)
a = 'Hello World'
print(a)
a = [1, 2, 3]
print(a)
a = [1.2,'Hello','W', 2]
print(a)

x = 2
a = 1 < x < 3 # True
print(a)
a = 10 < x < 20 # False
print(a)
a = 3 > x <= 2 # True
print(a)
a = 2 == x < 4 # True
print(a)
#if else
b = 10
if (b>0) :
    print("b la so nho hon 0")
elif (b < 0):
    print("b la so nho hon 0")
elif (b==1) :
    print(b)
else:
    print("no")
#for... in
for x in "banana":
      print(x)
      
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
#while
count = 0
while (count < 9):
    print ('The count is:', count)
    count = count + 1
print ("Good bye!")
# ham
def sum(a, b):
    return (a+b)
print (sum(4, 6))
#chuoi
str1 = "Hello"
str2 = 'world'
print (str1[0])
print (str2[0])
# noi chuoi
str = str1 + " " + str2
print (str)
#trich chuoi
print (str[0:4])
print (str[:4])
print (str[-3:])
print (str[6:-3])
#do dai cua chuoi
count = len(str)
print(count)
#tim thay the chuoi
str = 'Hello world'
newstr = str.replace('Hello','Bye')
print (newstr)
#tim chuoi con
str = 'Hello world'
print (str.find('world'))
print (str.find('Bye'))
#tach chuoi
print (str.split(' '))
#xu ly chuoi
str3 = "//space//"

s1 = str3.strip('/')
print(s1)
s1 = str3.lstrip('/')
print(s1)
s1 = str3.rstrip('/')
print(s1)

str1 = 'Hello world'
print (str1.split(' '))
#list
numbers = [1, 2, 3, 4, 5]
names = ['Marry','Peter']
print (numbers[0])

print (numbers[-3])

print (names[1])
#/kiem tra su ton ai cua 1 pahn tu
mylist = ['a','b','c']
print ('a' in mylist)
print ('b' not in mylist)

#trich mang con
numbers = ['a','b','c','d']
print (numbers[:2])
print (numbers[-2:])
#xoa phan tu trong mang
numbers = [1, 2, 3, 4, 5]
del numbers[0]
print (numbers)
#noi mang 
a = [1, 2]
b = [1, 3]
print (a + b)
#them phan tu vao mang
numbers = [1, 2, 3]
numbers.append(4)
print (numbers)
#lay phan tu cuoi mang
numbers = [1, 2, 3]
mynumber = numbers.pop()
print (mynumber)
print (numbers)
#tim 1 gia tri tong mang
aList = [123,'xyz','zara','abc'];
print ("Index for xyz : ", aList.index('xyz'))
print ("Index for zara : ", aList.index('zara'))
#dao nguoc gia tri cua mang
numbers = [1, 2, 3, 4]
numbers.reverse()
print (numbers)
#sắp xếp thứ tụ các phần tử
aList = [123,'xyz','zara','abc','xyz']
aList.sort()
print ("List : ", aList)
#Tuple
mytuple = ('x','y','z')
print (mytuple)
#dictionary

#them 1 phan tu
user = {'name': 'Jone','age': 30}
user['country'] = 'Vietnam'
print (user)
#đường dẫn đến load module
import  math
import random
#lấy danh sách thuộc tính cảu module
dir(math)
#khai báo su dung module
import mymath
num1 = 1
num2 = 2
print ('Tong hai so la: ', mymath.cong(num1, num2))
#package module
import mypack.mymodule1
#class
#khai báo 1 class
class Person:
    name = "lethanhdat";
    age = 22;
    male = True
#mở file
f1 = open('D:\HK1-2023-2024\phat trien he thong tich hop\ptthth\bai2.py','r')

#doc noi dung tu file
data = f1.read();
#ghi noi dung vao file
f1.write('Attack detected')
#đong file
f1.close()
#đoi ten
os.rename('bai2.py','test_new.txt')
#xóa file
os.remove('bai2.py')
#tạo thu muc
import os
os.mkdir('test')
#xoa thu muc
import os
os.rmdir('test')
#doc noi dung thu muc
import os
allfiles = os.listdir('/root/downloads')
print (allfiles)
#xu ly hinh anh
#cài đat pil mo file
from PIL import Image
im = Image.open("photo.jpg")
#ghi file
im.save('photo_new.jpg','JPEG')
#tạo thumbnails
from PIL import Image
im = Image.open('photo.jpg')
im.thumbnail((100, 100))
im.save('photo_thumbnail.jpg','JPEG')
#json
#load file tu in ternet
import urllib2
import json
response = urllib2.urlopen('https://api.github.com/users/voduytuan/repos')
data = json.load(response)
print (data)
#parsing json data
import json
mystring = '{"a":1,"b":2,"c":3,"d":4,"e":5}'
data = json.loads(mystring)
print (data)
#Encoding json data
import json
mydata = {
'name': 'John','age': 10
}
jsonstring = json.dumps(mydata)
print (jsonstring)