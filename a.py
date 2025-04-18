# l=[1,2,3,4,5]
# for i in l:
#     #print(l)
#     print(i)

# range(stop)
# for i in range(101):
#     print(i)
# range(start,stop)
# for i in range(1,101):
#     print(i)
# range(start,stop,step)
# for i in range(0,101,2):
#     print(i) 
#print even numbers from 2 to 20 
# for i in range(2,21,2):
#     print(i)
#wap to print mult of number given by user 
# num=int(input("enter the number:"))
# for i in range(1,11):
#     prod=i*num
#     print(prod)

#wap to print number in reverse from 10 to 1 
# for i in range(1,11):
#     print(i)
# print("-------------------")
# for i in range(10,0,-1):
#     print(i)

#if i want to add a condition 
#wap to print even numbers from 1 to 10 
# for i in range(1,21):
#     # print(i)
#     if(i%2==0):
#         print(i,"hey its even number") 
    
# for i in range(1,21):
#     print(i)

    # print(i)
    # if(i%2==0):
    #     print(i,"hey its even number")
        # break
        # continue 

#wap to print 1 to 10 when encounters 5 it should skip 
#output: 1 2 3 4 6 7 8 9 10 
# for i in range(1,11):
#     if(i==5):
#         continue
#     print(i)

#wap if it is a positive number t should print if it is a negative number it should continue and if it is a zero it should break 
num=[1,3,5,-1,7,9,0,11]
for n in num:
    if n==0:
        print("zero found,stopping the loop")
        break 
    if n<0:
        print("negative number is found,skipping")
        continue 
    
    print(n)