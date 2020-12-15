import time

with open('input') as f:
    input_list = f.read().split('\n')

print(input_list)

t1 = time.time()
for num1 in input_list:
    for num2 in input_list:
        for num3 in input_list:
            if int(num1) + int(num2) + int(num3) == 2020:
                print("{} + {} + {} gives {}. Answer: {}".format(num1,num2,num3,int(num1)+int(num2)+int(num3),int(num1)*int(num2)*int(num3)))
print((time.time() - t1)*1000)