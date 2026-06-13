def main(): # def = define the main function, handles all input and output
    dollars = dollars_to_float(input("How much was the meal? ")) # get meal cost, pass to dollars_to_float()
    percent = percent_to_float(input("What percentage would you like to tip? ")) # get tip %, pass to percent_to_float()
    tip = dollars * percent # calculate tip amount
    print(f"Leave ${tip:.2f}") # print result formatted to 2 decimal places

def dollars_to_float(d): # define a function that takes the meal cost string as input
    return float(d.replace("$", "")) # strip the $ sign, then convert string to float


def percent_to_float(p): # def = define a function that takes the tip percentage string as input
    return float(p.replace("%", "")) / 100 # strip the % sign, convert to float, divide by 100 to get decimal


main()  # run the program
