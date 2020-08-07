inp = int(input("Enter the number :\n"))
if inp < 1:
    print("enter valid number..")
for i in range(2,inp):
    if inp%i == 0:
        print(inp,"is not prime number")
else:
    print(inp,"is a prime number")
print("Done!")