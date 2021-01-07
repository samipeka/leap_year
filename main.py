# alghoritm> on every year that is evenly divisible by 4 **except** every year that
# is evenly divisible by 100 **unless** the year is also evenly divisible by 400

year = int(input("Which year do you want to check? "))

year_calculation1_modulo = year % 4
year_calculation2_modulo = year % 100
year_calculation3_modulo = year % 400


if year_calculation1_modulo == 0:
    if year_calculation2_modulo == 0 and year_calculation3_modulo == 0:
        print ("Leap year.")
    elif year_calculation2_modulo > 0:
        print ("Leap year.")
    else:
        print("Not leap year.")
else:
    print("Not leap year.")
