# print("Hello world")
# a=2
# b=3.2
# c=a+b
# print(type(c))
# a=10
# print (type(a))
# b=2.3
# print(type(b))
# c='abscdfg'
# e=[1,2,3,4,5]
# print(type(e))
# num1=input('please enter the first number')
# num2=input('please enter the secnd number')
# print(num1,num2)
# print(type(num1))
# print(type(num2))
# bill_total=194
# discount1=10
# if bill_total>100:
#     print("Bill is greater than 100")
#     bill_total=bill_total-discount1
# print("Total bill:"+str(bill_total))
# bill_total=95
# discount1=10
# if bill_total>100:
#     print("Bill is greater than 100!")
#     bill_total=bill_total-discount1
# else:
#     print("Bill is less than 100")
#     print("Total bill:"+str(bill_total))
#     http_status=200
#     match http_status:
#         case 200|201:
#             print('Success')
#         case 400:
#             print('Not Found')
#         case 500|501:
#             print('Servor Error')
        
#         case _:
#             print('Unknown')
# for i in range(10):

    # print('Looping..',i)
# favorite=['creme brulee','apple pie','churrors','tiramisu','choclate cake']
# for desserts in favorite:
#       print(' favourite' ,desserts)

# favourites=['creme brulee','apple pie','churrors','tiramisu','choclate cake']
# count=0
# while count<len(favourites):
#     print('one of my favourite dessets is',favourites[count])
#     count+=1;  
# for x in range(3):
#     print(x)
#     for y in range(3):
 #         print(y)
bill=input('please enter the bill')
print(bill)
tax_rate=input('please enter the tax_rate')
print(tax_rate)
def calculate_tax(bill,tax_rate):
    return (bill*tax_rate)/100.0
print('Total Tax:'  , calculate_tax(175.00,15))






            
            





