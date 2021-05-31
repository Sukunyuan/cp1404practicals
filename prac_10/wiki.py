import wikipedia
get_input = input("Please enter the title/phrase: ")
while get_input != "":
    try:
        web = wikipedia.page(get_input, auto_suggest=False)
        print(web.title)
        print(web.url)
        print(web.summary)
        get_input = input("Please enter the title/phrase: ")
    except:
        get_input = input("Please enter the title/phrase: ")