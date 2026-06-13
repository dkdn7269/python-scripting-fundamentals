def main(): # define the main function
    time = input("What time is it? ") # get time as a string e.g. '7:30'
    hours = convert(time) # pass to convert() which returns a float e.g. 7.5

    if 7.0 <= hours <= 8.0:  # chained comparison — both endpoints included
        print("breakfast time")
    elif 12.0 <= hours <= 13.0:
        print("lunch time")
    elif 18.0 <= hours <= 19.0:
        print("dinner time")

# no else — if no meal window matches, print nothing at all

def convert(time): #define a function that takes the time string and converts it to a float
    hours, minutes = time.split(":") # split '7:30' into '7' and '30'
    return int(hours)+ int(minutes) / 60 # 30 minutes = 30/60 = 0.5, so 7:30 becomes 7.5

if __name__ == "__main__": # only runs main() if this file is executed directly
    main()

