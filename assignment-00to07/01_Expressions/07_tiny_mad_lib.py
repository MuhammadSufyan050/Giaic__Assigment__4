sentence_start = "Panaversity is fun. I learned to program and used python to make my "

def main():

    adjective = input("\033[1;3m Enter an adjective and press enter: \033[0m")
    noun = input("\033[1;3m Enter a noun and press enter: \033[0m")
    verb = input("\033[1;3m Enter a verb and press enter: \033[0m")

    print(sentence_start + adjective + " " + noun + " " + verb + ".")

if __name__ == "__main__":
    main()