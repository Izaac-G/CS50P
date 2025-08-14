def main():
    answer = input("What do you have to say? ")
    print(convert(answer))
    
def convert(text):
    return text.replace(':)','smile').replace(':(','frown')

main()
