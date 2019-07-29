
def add_numbers(x,y,z):
    #write the body of this
    #function, similar to the block
    #of code we just saw. Hint:
    #don’t forget to use return
    total = 0
    for number in range(x,y,z):
        total = total + number
    print(total)
test1 = add_numbers(1,2,1)
print(test1)
test2 = add_numbers(1, 10 ,2)
print(test2)
test3 = add_numbers(1000, 5000,1)
print(test3)

