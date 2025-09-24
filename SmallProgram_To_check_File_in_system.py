import os 
fname = input('Enter Your File Named: ')
if os.path.isfile(fname):
    print('File exist: ', fname)
    f = open(fname,'r')
    print('Content of file is: ')
    data = f.read()
    print(data)
else:
    print('File Not exist: ', fname)
