# custom-functions/my_functions.py

# TODO: define temperature conversion function here
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
# TODO: define gradebook function here
def numeric_to_letter_grade(score):
    if score < 60:
        return "F"
    elif score < 70:
        return "D"
    elif score < 80:
        return "C"
    elif score < 90:
        return "B"
    else:
        return "A"

if __name__ == "__main__":

    # def celsius_to_fahrenheit(c):
    #     return (c * (9/5)) + 32

    print("--------------------")
    print("CUSTOM FUNCTIONS EXERCISE...")
    print("--------------------")

    c = 0
    print("THE CELSIUS TEMP IS:", c, "DEGREES")

    f = celsius_to_fahrenheit(c)
    print("THE FAHRENHEIT EQUIVALENT IS:", f, "DEGREES")



    print("--------------------")

    # def numeric_to_letter_grade(score):
    #     return ()
    score = float(input("Please input a grade from 0 to 100: "))
    # print(type(score))
    # score = float(score)
    #todo: ensure the provided input value is valid before passing it into the function below)
    print("THE NUMERIC SCORE IS:", score)
    grade = numeric_to_letter_grade(score)
    print("THE LETTER-GRADE EQUIVALENT IS:", grade)

    #if your function needs a variable, pass in that variable as a parameter
    #prefer to pass in y if our function needs it
    #other_func(x,y) vs other_func(x)