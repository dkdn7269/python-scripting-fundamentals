def convert(happysadface):      # def = define a reusable function called convert, takes one string as input
    return happysadface.replace(":)", "🙂").replace(":(", "🙁")    # replace emoticons with emoji, chained left to right

def main(): #define the main function, handles all input and output
    happysadface = input()  # get user input as string
    print(convert(happysadface))    # pass it to convert(), print the returned result


main() # run the program
