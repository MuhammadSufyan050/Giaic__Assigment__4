def add_three_copies(myList, data):
    for i in range(3):
        myList.append(data)

def main():

    message = input("Enter a message to copy: ")
    myList = []
    print("Before list: ", myList)

    add_three_copies(myList, message)
    print("After list: ", myList)

if __name__ == "__main__":
    main()