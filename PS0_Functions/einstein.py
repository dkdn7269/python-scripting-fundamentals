def main(): #define the main function
    m = int(input("m:")) # get mass from user, convert string to int for math
    c = 300000000 # speed of light in m/s stored as a variable
    E = m * c ** 2 # E = mc² — ** is exponentiation (c to the power of 2)
    print (E) # print the energy in joules

main() # run the program
