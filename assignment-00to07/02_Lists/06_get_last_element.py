def get_last_element(lst):
    if lst:
        print("First element:", lst[-1])

def get_lst():
    lst = []

    element = input("Enter an element to add to the list: ")
    while element != "":
        lst.append(element) 
        element = input("Enter an element to add to the list: ")

    return lst 

def main():
    lst = get_lst()
    get_last_element(lst)

if __name__ == "__main__":
    main()
