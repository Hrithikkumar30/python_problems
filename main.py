# User will input (2numbers).Write a program to swap the numbers
# a = int(input('number a'))
# b = int(input('number b'))
# c = a
# a=b
# b= c
# print("After swapping", "value of A is:", a, "\n" )
# print("After swapping","value of B is:",b)



# Write a program that will give you the sum of 3 digits

# num=int(input('enter 3 digit number'))

# sum = 0

# for i in str(num):
#     sum+=int(i)
# print(sum)



# Write a program that will reverse a four digit number.Also it checks whether the reverse is true.

# num = (int(input('enter 4 digit number')))
# rev=0
# while num>0:
#     rev=(rev*10)+(num%10); #adding each last digit at end
#     num=num//10
    
    
# print(rev)


# Write a program that will tell whether the number entered by the user is odd or even.

# def number (n):
#     if n %2==0:
#         print('even')
#     else:
#         print('odd')
# number(5)



# Write a program that will tell whether the given year is a leap year or not.

# def year(n):
#     if(n%100==0 or n%4==0 ):
#         print("leap year")
#     else:
#         print('not leap')
# year(300)

# Write a program to find the euclidean distance between two coordinates

# def coordiates(x1,y1 , x2,y2):
#     dist = abs((((x1-x2)**2)+((y1-y2)**2)))
#     final = dist**(1/2)
#     print(final)
# coordiates(1,2,2,1)



# Angle between hour and minute hand
# M=0
# H=0
# def time(H , M):
    
    
#     M = M//5
#     angle = abs((H-M)*30)
#     print(angle)
    
# time(7,45)
    
    


    
# Write a program that will determine weather when the value of temperature and humidity is provided by the user.

# def weather_condition(Temp , Hum):
   
    
#     if Temp >= 30 and Hum>=90:
#         print('Hot and Humid')
#     elif Temp >= 30 and Hum<90:
#         print('Hot')
#     elif Temp < 30 and Hum>=90:
#         print('Cool and Humid')
#     else :
#         print('Cool')
# weather_condition(Temp=int(input('Enter the temperature')) , Hum=int(input('Enter the Humidity')))

    
# # # Write a program that will take three digits from the user and add the square of each digit.
# def number(n):
#     sum =0
#     n = int(n)
#     while n >0:
#         rem = n%10
#         sum += (rem**2)
#         n=int(n//10)
#     print(sum)
        
# number(123)


# Write a program that will check whether the number is armstrong number or not.

def armstrong(num):
    num1=num
    sum=0
    while num>0:
        rem = num%10
        sum+=rem**3
        num=num//10
        
    if num1==sum:
            print('its a armstrong number')
    else:
            print("it's not a armstrong number")
armstrong(370)