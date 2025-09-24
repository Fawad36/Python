# F = open('abc.txt', 'r')
# # data = F.read()
# # print(data)

# print(F.readable())  #* if data in file then it will be true if not then it can be False;


# CreateFile = open('Fawad.txt' , 'w')
# CreateFile.write('fawad khannnnn')  #* that Overide data into file  if data already has present in File
# print(CreateFile)


#*.......................................... For reading The data in a file 

# F = open('Fawad.txt','r')
# data = F.read()
# print(data)

#*.......................................... Append data and then read it 

# with open('Fawad.txt','a') as f:
#     chars_written = f.write('Hello i am fawad from madyan swat \n append dosnot overide data into a file ')
# with open('Fawad.txt','r') as r:
#     all_txt = r.read()
#     print(all_txt)



#?......................................
# f = open('Write_Some_data.txt','w')
# data = f.write('fawad \njawad\n waqas\n  imad\n talha\n')

# print(data)


# ? to print charcter like    
# f = open('Write_Some_data.txt')
# data = f.read(12)
# print(data)
# f.close


# #? to print line by line   end = ''   no for new line 
# f = open('Write_Some_data.txt','r')

# print(f.readline(), end='')
# print(f.readline(),end='')
# print(f.readline())
# print(f.readline())
# print(f.readline())

# f.close





# #? ..................................................
# f = open('Write_Some_data.txt','r')
# list = f.readlines()
# print(list)
# f.close




#?,...................................................................
# f = open('Write_Some_data.txt','r')
# list = f.readlines()
# for line in list:
#     print(line,end='')
# f.close




#?...................................................................

# with open('Fawad.txt', 'w') as f:
#     f.write('fawad\n') 
#     f.write('jawad\n')
#     f.write('waqas\n')
#     f.write('talha\n')
#     print('isfilecloed',f.close)
# print('is file cloed', f.close)

#*.................................................................

with open('Fawad.txt','r') as f:
    print(f.tell())
    print(f.read(3))
    print(f.tell())






