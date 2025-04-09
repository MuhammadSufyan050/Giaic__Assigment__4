def get_first_element(lst):
    if lst:
        print("First element:", lst[0])

def get_lst():
    lst = []

    element = input("Enter an element to add to the list (leave empty to stop): ")
    while element != "":
        lst.append(element) 
        element = input("Enter an element to add to the list (leave empty to stop): ")

    return lst 

def main():
    lst = get_lst()
    get_first_element(lst)

if __name__ == "__main__":
    main()
