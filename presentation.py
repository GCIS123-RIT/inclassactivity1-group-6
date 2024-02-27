#slide 5    
l = 0 
while l <5:
    print("hi")
    l = l + 1
print ("bye")

# explaination of the while loop code 
count = 0 #start count from 0 
while count < 5: # condition of while loop
    print("Count is:", count)
    count += 1 


# the code shows the while loops condition, count < 5 tells us that
# if the variable is less than 5 its true  and will continue executing
# if its false, it will terminate 

# examples  
x=1
while(x<=10):
     print(x, end=' ')
     x=x+1

x=0
while(x< 10):
    x=x+1
    if  x>=6 and x<=8:
        continue
        
    print(x, end=' ')


# break and continue 
count = 0 
while True: 
    count += 1
    if count == 3:
        continue
    print("count is:", count)

count = 0 
while True: 
    print("count is:", count)
    count += 1
    if count == 5: 
        break 



