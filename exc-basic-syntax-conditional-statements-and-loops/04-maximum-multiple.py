# divisor = int(input())
# boundary = int(input())
# result = 0
# for n in range(1,boundary+1):
#     if n % divisor == 0:
#         result = n
#
# print(result)

divisor = int(input())
boundary = int(input())

for num in range(boundary, 0, -1):
    if num % divisor == 0:
        print(num)
        break
