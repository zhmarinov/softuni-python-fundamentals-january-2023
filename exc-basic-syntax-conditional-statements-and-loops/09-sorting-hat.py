while True:
    student_names = input()
    if student_names == 'Welcome!':
        print("Welcome to Hogwarts.")
        exit()
    elif student_names == 'Voldemort':
        print("You must not speak of that name!")
        exit()

    len_counter = len(student_names)

    if len_counter < 5:
        print(f"{student_names} goes to Gryffindor.")
    if len_counter == 5:
        print(f"{student_names} goes to Slytherin.")
    if len_counter == 6:
        print(f"{student_names} goes to Ravenclaw.")
    if len_counter > 6:
        print(f"{student_names} goes to Hufflepuff.")



