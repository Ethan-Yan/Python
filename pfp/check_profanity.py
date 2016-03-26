##error

import urllib.request

def read_text():
    quotes = open('D:\ds\Python\pfp\movie_quotes.txt')
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.request.urlopen('http://www.wdyl.com/profanity?q=' + text_to_check)
    output = connection.read()
    #print(output)
    connection.close()
    if 'true' in output:
        print('Profanity Alert!!')
    elif 'false' in output:
        print('This documrnt has no curse words!')
    else:
        print('Could not scan the document properly.')
    
read_text()
