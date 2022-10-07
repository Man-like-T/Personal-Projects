def replaceWord():
    #A funtion to replace a word in a sentence(string) with another

    str = 'I want to replace these word word word'
    to_replace = input('Enter the word to be replaced: ')
    replacement = input('Enter the replacement word: ')
    print(str.replace(to_replace,replacement))

replaceWord()