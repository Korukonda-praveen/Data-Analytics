
'''
bmi_data={
    'height':[],
    'weight':[],
}
count=0
while count<5:
    try:
        
        height=int(input('Enter your choice\n1.ms\n2.cms\n3.feet\n'))
        if height==1:
            input_=float(input('enter the height in ms:'))
            height=input_
        elif height==2:
            input_=int(input('enter the height in cms:'))
            height=input_/100
        elif height==3:
            input_=float(input('enter the  height in feet:'))
            height=input_/3.281
        else:
            print('invaild input')

        weight=int(input('enter the weight in kgs:'))
        bmi_data['height'].append(height)
        bmi_data['weight'].append(weight)
        if (height>0 and height<2) and (weight>0 and weight<200):
            bmi=weight/(height**2)
            if bmi<18.5:
                print("underweight")
            elif bmi<=24.9:
                print("normal")
            elif bmi<=29.9:
                print('overweight')
            elif bmi>30:
                print('obesity')
            
        else:
            print('invaild enter')
        
        count+=1
  
    except Exception as e:
        print(e)
print(bmi_data)
'''




#file handlin--> create file make some changes over files
#we will use open(),with()-->txt.files
#we have different modes--> 'r','w','a','r+'

#file = open('page.txt', 'r')
#print(file)
#file = open('page.txt', 'r')
#print(file.read())

#file =open('sample.txt', 'w')
#file.write('hello world')
#file.close() once the file is closed then only the data is written to file
#print(file)

#we can use with keyword
#with open('sample.txt','w')as file:
    #print(file) in this case we already sample.txt file the content is overriding
    #file.write('khatam tata bye bye good bye\n')
    #file.write('hello world')
    #no need for usage of close() content will be directly

#data=['codegnan' ,'python' ,'da' , 'vizag']
#with open ('qw.txt','w')as file:
    #file.writelines(data) # this can directly insert the data from the list

# 'a'--> will create a new file,if file is already existitng content will be added instead of overriding
'''
with open('qw.txt','a') as f:
    f.write('\n today we are having a webianr realted to voice agent')
'''
#'r+'-->performs both read and write operations
'''
with open('qw.txt','r+')as f:
    print(f.read())
    f.write("\n ok bye")
'''