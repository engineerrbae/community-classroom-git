

# Exploring Data Types _ TechGig
import re


def checking():
    user_input = input("Enter input: ")
    try:
        check  = int(user_input)
        print("This input is of type Integer.")


    except ValueError:
        try:
            check = float(user_input)
            print("This input is of type Float.")
        except ValueError:
            try:
                regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
                if regex.search(user_input):
                    print("This is something else.")
                else:
                    
                    check = str(user_input)
                    print("This input is of type string.")
            except ValueError:
                print("This input is of type string.")

checking()
