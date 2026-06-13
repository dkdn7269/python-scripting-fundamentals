# strip whitespace and lowercase so inputs like '  42  ' or 'FoRtY TwO' still match
life = (input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")).strip().lower()

# check all three accepted answers — each needs its own == comparison with or
if life == "42" or life == "forty-two" or life == "forty two":
    print ("Yes")
else:       # only two outcomes so else covers everything else
    print ("No")

