import json, pyttsx3
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word , data.keys())) > 0 :
        print("Did you mean %s instead: " %get_close_matches(word, data.keys())[0])
        decide = input("Press 'y' for YES or 'n' for NO: ")
        if decide == "y":
            return data[get_close_matches(word , data.keys())[0]]
        elif decide == "n":
            return("Sorry! No match found")
        else:
            return("You have entered wrong input please enter just 'y' or 'n' : ")
    else:
        print("Sorry! No match found")

if __name__ == '__main__':
    converter = pyttsx3.init()
    converter.setProperty('rate', 100) 
    converter.setProperty('volume', 1) 
    choice = 'y'
    while choice=='y':
        word = input("Enter the word you want to search: ")
        output = translate(word)
        if type(output) == list:
            for item in output:
                print(item)
                converter.say(item)
                converter.runAndWait()
        else:
            print(output)
            converter.say(output)
            converter.runAndWait()
        choice = input("Do you want to search again? (y/n): ")