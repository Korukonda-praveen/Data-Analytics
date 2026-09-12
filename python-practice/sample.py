'''
print('hello my name is praveen')
a=20
b=30
print(a+b)

Tokens=keywords,varables,operator,punctuartions,literls
varables should not start with spaces,numbers,
len->return the number of items in a collection


'''
batch= ['pfs-06','da-06']
#print(batch) # output:['pfs-06', 'da-06']

#print(type(batch))# output:<class 'list'> type is used for to show which datatypes is used 

#batch.append('praveen') # append is used to add one value in the list

#print(batch) # output: ['pfs-06', 'da-06', 'praveen']

#batch.extend(['jayakumar','asha'])# extend is used to add more than one values

#print(batch)# output:['pfs-06', 'da-06', 'praveen', 'jayakumar', 'asha']

#print(len(batch)) # output:5

#batch.insert(0,'sai') # insert given value at specific index

#print(batch) # output:['sai', 'pfs-06', 'da-06', 'praveen', 'jayakumar', 'asha']

#batch.insert(-1,'python')#value before index using -ve

#print(batch)# output:['sai', 'pfs-06', 'da-06', 'praveen', 'jayakumar', 'python', 'asha']

#indexing-->[]--> index starts at 0 ends at len(obj)-1
#also in reverse manner it is -1 to len(obj)
#print(batch[0]) output:sai /it will give the first value present in the list
#print(batch[9]) indexerror--> length is only 7 we are accesing extra
# Slicing--> group of values[start:end] # start is included,end is excluded
#print(batch[2:5])['da-06', 'praveen', 'jayakumar']
#strinding-->[start:end:step]
#print(batch[::3]) output:['sai', 'praveen', 'asha'] #it skips 2 elements from start
#print(batch[1:5:2]) output:['pfs-06', 'praveen'] / first perform batch[1:5]--then skip 1 element


batch=['sai', 'pfs-06', 'da-06', 'praveen', 'jayakumar', 'python', 'asha']
#tryout-->such kind

#print(batch[:7:4]) #output: sai jayakumar
#print(batch[7::4])
#print(batch[1::5])
#print(batch[1:7:-2])
#print(batch[-1:-4:-1])   
#print(batch[])