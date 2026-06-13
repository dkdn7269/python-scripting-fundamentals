# strip whitespace and lowercase before any comparisons run
bank = str(input("Greeting: ")).strip().lower()

if bank.startswith("hello"):    # more specific check first — hello also starts with h
    print ("$0")
elif bank.startswith("h"):      # catches h greetings that aren't hello
    print ("$20")
else:                           # anything that doesn't start with h at all
    print ("$100")

