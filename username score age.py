def get_username():
    inp = input("Whats your name? ")
    num = input("Whats your age? ")
    return inp,num

def get_marks(msg):
    marks = input("how much did you score? ")
    return marks

def main():
    name, age = get_username()
    score = get_marks(name)
    print(name, age, score)

#main starts from here
main()
