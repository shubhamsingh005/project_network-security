#python program to generate md5 of string data

import hashlib
 
string=input("Enter the string : \n")#taking input from the user 

hashed_string=(hashlib.md5(string.encode('utf-8')).hexdigest())#converting the string into md5 hased form 

print("The md5 of string is " ,hashed_string)