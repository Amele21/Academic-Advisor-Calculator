# Author: Adrian Melendrez

def target_gpa():
    """Calculates target gpa for student"""
    # Menu

    print("---------Current Student Data---------")
    # Get current student data
    cur_data = current_data_helper()
    cur_gpa = float(cur_data[0])
    cur_units = float(cur_data[1])
    print("GPA points: ", cur_gpa, "   units: ", cur_units)

    # total new courses
    new_courses_count = int(input("Enter total number of new courses you are going to add: "))
    print('\n')

    # Get new data for student and calculate overall gpa
    add_new_gpa_helper(new_courses_count, cur_gpa, cur_units)

    print("Goodbye")


def current_data_helper():
    """Get current data from student"""
    gpa = input("Enter student's total gpa points:   ")
    units = input("Enter student's total units:  ")
    return [gpa, units]


def add_new_gpa_helper(new_courses_count, cur_gpa, cur_units):
    """New added gpa"""
    exit_cal = 'n'
    while exit_cal == 'n':
        key_letters = ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F']
        key_values = [16.00, 14.80, 13.20, 12.00, 10.80, 9.20, 8.00, 6.80, 5.20, 4.00, 2.8, 0.00]
        total_value_calculation = 0
        total_new_units = 0

        if new_courses_count >= 1:
            print("---------First Course to be added---------")
            input_one_letter = str(input("Enter letter grade in uppercase followed by symbol (ex: B+, A, F):    "))
            input_one_units = float(input("Enter the total units for this course: "))
            letter_one_index = key_letters.index(input_one_letter)
            data_one = key_values[letter_one_index]
            total_new_units += input_one_units
            total_value_calculation += data_one
            print("Letter: ", input_one_letter, "   GPA points: ", data_one, "   units: ", input_one_units)
            print('\n')

        if new_courses_count >= 2:
            print("---------Second course to be added---------")
            input_two_letter = str(input("Enter letter grade in uppercase followed by symbol (ex: B+, A, F):    "))
            input_two_units = float(input("Enter the total units for this course: "))
            letter_two_index = key_letters.index(input_two_letter)
            data_two = key_values[letter_two_index]
            total_new_units += input_two_units
            total_value_calculation += data_two
            print("Letter: ", input_two_letter, "   GPA points: ", data_two, "   units: ", input_two_units)
            print('\n')

        if new_courses_count == 3:
            print("---------Third course to to be added---------")
            input_three_letter = str(input("Enter letter grade in uppercase followed by symbol (ex: B+, A, F):    "))
            input_three_units = float(input("Enter the total units for this course: "))
            letter_three_index = key_letters.index(input_three_letter)
            data_three = key_values[letter_three_index]
            total_new_units += input_three_units
            total_value_calculation += data_three
            print("Letter: ", input_three_letter, "   GPA points: ", data_three, "   units: ", input_three_units)
            print('\n')

        # Calculate total data by adding new data to the current data
        total_gpa = total_value_calculation + cur_gpa
        total_units = total_new_units + cur_units
        gpa = round((total_gpa / total_units), 2)
        sem_gpa = round((total_value_calculation / total_new_units), 2)
        prev_gpa = round((cur_gpa/cur_units), 2)
        print("------------------Total GPA points and units with new data------------------")
        print("OVERALL:  GPA:          ", gpa, "    GPA points: ", total_gpa, "      units: ", total_units)
        print("SEMESTER: GPA:          ", sem_gpa, "    GPA points: ", total_value_calculation, "      units: ", total_new_units)
        print("PREVIOUS OVERALL GPA:   ",prev_gpa, "   GPA points: ", cur_gpa, "      units: ", cur_units)
        print('\n')

        exit_cal = input("Exit?  y for yes    n for no    option: ")
        print('\n')


target_gpa()
