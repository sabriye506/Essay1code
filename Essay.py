class Essay:
    word = ""
    sentence = ""

    essay = input("enter a sentence: ")
    words = essay.split()
    Number = len(words)
    print("The user entered: ", essay, sep=" ")
    print("The word count of the essay is: ", Number, sep=" ")
