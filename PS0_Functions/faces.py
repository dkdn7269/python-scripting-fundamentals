def convert(happysadface):
    return happysadface.replace(":)", "🙂").replace(":(", "🙁")

def main():
    happysadface = input()
    print(convert(happysadface))


main()
