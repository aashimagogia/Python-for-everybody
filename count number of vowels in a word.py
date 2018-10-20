#COUNT_NUMBER_OF_VOWELS_IN_A_NAME

li=['a','e','i','o','u']

name=input('Enter Name-')

no=0

for x in name:
    
    if(x in li):
        
        no+=1

print('No of vowels equals',no)
