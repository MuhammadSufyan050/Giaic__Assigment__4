max_length = 3

def shorten(lst):

    while len(lst) >= max_length:
        last_element = lst.pop()
        print(last_element)

def get_list():
    lst = []
    element = input("Enter an element to add to the list: ")

    while element != "":
        lst.append(element)
        element = input("Enter an element to add to the list: ")
    return lst

def main():

    lst = get_list()
    shorten(lst)

if __name__ == "__main__":
    main()