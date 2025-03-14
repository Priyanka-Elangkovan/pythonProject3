# Create a program that "I will give you a number (from USer input and print tables for it )"
# 1. F{} string format concept
# 2. User input -- 10,100,-1,2,3.14
# 3. 9x1=9 until 10.

Var1 = int(input("Please enter the number you want the tables on :"))
i=1
while(i< 11):
    Var2 = Var1*i
    print(f"{Var1} * {i} = {Var2}")
    i= i+1

## Create a program, take 2 inputs from the user num1 and num2 and output dshould be
## Max, Pow, Sub,
# Format with the F{""}

print("Starting with the second task")
a = input("Please enter the two number with a comma separator :" )
n= a.partition(",")
Num1=int(n[0])
Num2=int(n[2])
Mx = max(Num1, Num2)
print(f"Max of the two numbers {Mx}")

pw = Num1 ** Num2
print(f"Power of the two numbers {pw}")

sb = Num1 - Num2
print(f"Subration results of the two numbers {sb}")
