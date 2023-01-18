def target_gpa():
    # Get current gpa
    gpa_points = float(input("Enter student's total gpa points:   "))
    units = float(input("Enter student's total units:  "))
    gpa = round((gpa_points/units), 2)
    print('\n')
    print("----Current GPA------")
    print("OVERALL GPA: ", gpa, "  gpa_points: ", gpa_points, "  units: ", units)
    print('\n')

    #find target gpa needed to be 3.0 or over
    key_letters = ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F']
    key_values = [16.00, 14.80, 13.20, 12.00, 10.80, 9.20, 8.00, 6.80, 5.20, 4.00, 2.8, 0.00]
    target_values = []

    new_courses_count = input("Enter number of new courses to add: ")
    first_unit = float(input("Enter the units for first course: "))
    second_unit = 0.0
    third_unit = 0.0

    if new_courses_count == '1':
        for i in range(len(key_values)):
            total_gpa_points = key_values[i] + gpa_points
            total_units = first_unit + second_unit + third_unit + units
            total_gpa = round((total_gpa_points / total_units), 2)

            # Only include passing grade and passing gpa
            if total_gpa >= 3.0 and key_values[i] >= 8.0:
                target_values.append(
                    [total_gpa, total_gpa_points, total_units, key_values[i]])

    if new_courses_count == '2':
        second_unit = float(input("Enter the units for second course: "))
        for i in range(len(key_values)):
            for j in range(len(key_values)):
                total_gpa_points = key_values[i] + key_values[j] + gpa_points
                total_units = first_unit + second_unit + third_unit + units
                total_gpa = round((total_gpa_points / total_units), 2)
                if total_gpa >= 3.0 and key_values[i] >= 8.0 and key_values[j] >= 8.0:
                    target_values.append(
                        [total_gpa, total_gpa_points, total_units, key_values[i], key_values[j]])

    if new_courses_count == '3':
        second_unit = float(input("Enter the units for second course: "))
        third_unit = float(input("Enter the units for the third course: "))
        for i in range(len(key_values)):
            for j in range(len(key_values)):
                for k in range(len(key_values)):
                    total_gpa_points = key_values[i] + key_values[j] + key_values[k] + gpa_points
                    total_units = first_unit + second_unit + third_unit + units
                    total_gpa = round((total_gpa_points/total_units), 2)
                    if total_gpa >= 3.0 and key_values[i] >= 8.0 and key_values[j] >= 8.0 and key_values[k] >= 8.0:
                        target_values.append([total_gpa, total_gpa_points, total_units, key_values[i], key_values[j], key_values[k]])

    print('\n')
    print("------------------------------ALL POSSIBLE SCENARIOS--------------------------")
    target_values = sorted(target_values)

    for k in range(len(target_values)):
        sem_gpa = 0
        target_one_index = key_values.index(target_values[k][3])
        target_one = key_letters[target_one_index]
        sem_gpa += target_values[k][3]

        if new_courses_count == '2' or new_courses_count == '3':
            target_two_index = key_values.index(target_values[k][4])
            target_two = key_letters[target_two_index]
            sem_gpa += target_values[k][4]

        if new_courses_count == '3':
            target_three_index = key_values.index(target_values[k][5])
            target_three = key_letters[target_three_index]
            sem_gpa += target_values[k][5]

        sem_gpa = round((sem_gpa/(first_unit + second_unit + third_unit)), 2)

        if new_courses_count == '1':
            print("NEW OVERALL GPA:  ", target_values[k][0], "    SEMESTER GPA: ", sem_gpa, "    first target: ", target_one)

        if new_courses_count == '2':
            print("NEW OVERALL GPA:  ", target_values[k][0], "     SEMESTER GPA: ", sem_gpa, "    first target: ", target_one, "    second target: ", target_two)

        if new_courses_count == '3':
            print("NEW OVERALL GPA:  ", target_values[k][0], "     SEMESTER GPA: ", sem_gpa, "    first target: ", target_one, "    second target: ", target_two, "  third target: ", target_three)

    if len(target_values) == 0:
        print("NOT POSSIBLE TO GET 3.0 OR ABOVE")


if __name__ == '__main__':
    import os
    user_input = '1'
    while user_input == '1':
        target_gpa()
        print('\n')
        user_input = input("Enter    1 to run/rerun      2 to exit: ")
        os.system('clear')