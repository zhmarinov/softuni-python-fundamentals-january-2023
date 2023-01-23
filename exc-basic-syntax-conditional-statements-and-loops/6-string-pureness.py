numbers_of_strings = int(input())

for _ in range(numbers_of_strings):
    string = input()

    is_pure = True
    for ch in string:
        if ch == ',' or ch == '.' or ch == '_':
            is_pure = False

    if is_pure:
        print(f"{string} is pure.")
    else:
        print(f"{string} is not pure!")



