# Python3 code for extended version
# of power function that can work
# for float x and negative y

def power(x, y):
    print("\nYou called power:", x, y)
    if y == 0:
        print(x, y, "Return 0")
        return 1
    print("Calling power...", x, int(y/2))
    temp = power(x, int(y / 2))
    print("temp ->", temp)

    if y % 2 == 0:
        print(x, y, "Return 1 : ", temp * temp)
        print("\n")
        return temp * temp
    else:
        if y > 0:
            print(x, y, "Return 2 : ", x * temp * temp)
            print("\n")
            return x * temp * temp
        else:
            print("Return 3 : ", (temp * temp) / x)
            print("\n")
            return (temp * temp) / x


# Driver Code
a, b = 7, 6
print('%.6f' % (power(a, b)))

# This code is contributed by Smitha Dinesh Semwal.