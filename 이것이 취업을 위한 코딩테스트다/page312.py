S = input()
result = 0
for i in S:
    if result == 0 or int(i) == 0:
        result = result + int(i)
    else:
        if result + int(i) > result * int(i):
            result = result + int(i)
        else:
            result = result * int(i)
print(result)

# input ex1)
# 02984
# output ex1)
# 576

# input ex2)
# 576
# output ex2)
# 210
