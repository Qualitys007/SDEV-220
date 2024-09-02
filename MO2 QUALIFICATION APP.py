#""" Author: Damon Akinyemi
# App name: Acedmic Program Qualification Checker: 
#Description:
# This script accepts student names and GPAs and checks if the student qualifies
#for the Dean's List or Honor Roll. The program continues to accept input until
    #the user enters 'quit' as the last name.
    
   # - Dean's List: GPA of 3.5 or higher
    #- Honor Roll: GPA of 3.25 or higher



def check_qualification(gpa):
    if gpa >= 3.5:
        return "Dean's List"
    elif gpa >= 3.25:
        return "Honor Roll"
    else:
        return None

def main():
    while True:
        last_name = input("Enter the student's last name (or 'quit' to quit): ")
        if last_name.upper() == 'quit':
            print("Exiting the program...")
            break

        first_name = input("Enter the student's first name: ")
        try:
            gpa = float(input("Enter the student's GPA: "))
        except ValueError:
            print("Invalid input. GPA should be a number.")
            continue

        qualification = check_qualification(gpa)

        if qualification:
            print(f"{first_name} {last_name} has made the {qualification}!")
        else:
            print(f"{first_name} {last_name} did not qualify for the Dean's List or Honor Roll.")

if __name__ == "__main__":
    main()
