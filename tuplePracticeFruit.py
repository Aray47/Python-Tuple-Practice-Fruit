import sys

def main():
    tuplePartOne()
    dictPartTwo()
    userPartThree()
    userPartFour()

def tuplePartOne():
    print("\nPart One: ")
    tup1=('physics', 'chemistry', '1997', '2000')
    for t in tup1:
        print(t)

def dictPartTwo():
    print("\nPart Two: ")
    fruit = {
        "Apple":"Red",
        "Banana":"Yellow",
        "Orange":"Orange",
        "Ladybugs":"Spotted"
    }
    for key,val in fruit.items():
        print(key,"=>", val)

def userPartThree():
    print("\nPart 3")
    fruit = {
        "Apple":"Red",
        "Banana":"Yellow",
        "Orange":"Orange",
        "Ladybugs":"Spotted"
    }
    userInput = input("Type a fruit to see if a color exists in our dictionary!\n")
    if userInput.isalpha():
        for key,val in fruit.items():
            if userInput.lower() == key.lower():
                print(userInput,"matches", val)
    else:
        print("Colors have alphabetical characters. Try again!")

def userPartFour():
    print("\nPart 4: ")
    fruit = {
        "Apple":"Red",
        "Banana":"Yellow",
        "Orange":"Orange",
        "Ladybugs":"Spotted"
    }
    userInput = input("Type a color to see if a fruit exists in our dictionary!\n")
    if userInput.isalpha():
        for key,val in fruit.items():
            if userInput.lower() == val.lower():
                print(userInput,"matches", key)
    else:
        print("Colors have alphabetical characters. Try again!")


if __name__ == '__main__':
  sys.exit(main())