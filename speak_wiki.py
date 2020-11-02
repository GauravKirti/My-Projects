import wikipedia, pyttsx3
from tabulate import tabulate

def wiki_search(query):
    choice = wikipedia.search(query, results=5)
    choice_list = []
    for i in range(len(choice)):
        choice_list.append((i,choice[i]))
    print(tabulate(choice_list, headers=['Sl.No.','Articles']))
    option = input("Please enter Sl.No. of article you want to hear : ")
    return choice[int(option)]

if __name__ == '__main__':
    query = input("Please enter a keyword to search : ")
    keyword = wiki_search(query)
    page_object = wikipedia.page(keyword)
    converter = pyttsx3.init()
    converter.setProperty('rate', 100) 
    converter.setProperty('volume', 1) 
    sentence = input("Please Enter No.of sentences you want to hear : ")
    speech = wikipedia.summary(keyword, sentences=int(sentence))
    print(f"Reading the article : {page_object.original_title}")
    converter.say(speech)
    converter.runAndWait()