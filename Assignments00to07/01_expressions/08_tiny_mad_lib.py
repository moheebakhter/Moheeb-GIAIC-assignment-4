SENTENCE_START : str = "Panaversity is fun. I Learned to program and used python to make my"

def main():
    adjective : str = input("\033[1;3mEnter an adjective and press enter:\033[0m")
    noun : str = input("\033[1;3mEnter a noun and press enter:\033[0m")
    verb : str = input("\033[1;3mEnter a verb and press enter:\033[0m")

    print( SENTENCE_START +  " " + adjective + " " + noun + " " + verb + ".")

if __name__ == "__main__":
    main()