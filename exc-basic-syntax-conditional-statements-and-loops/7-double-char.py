# while True:
#     string = input()
#     if string == 'End':
#         break
#
#     if string == 'Softuni':
#         continue
#
#     converted_string = ''
#     for ch  in string:
#         converted_string += 2 * ch
#     print(converted_string)

while True:
    string = input()
    if string == 'End':
        break

    if string == 'SoftUni':
        continue

    for ch in string:
        print(f'{ch}{ch}', end='')
    print()

