# album dictionary

music = {'Artist 1':
              {'Album 1':
                   {'songs': ['song1', 'song2'],
                    'year': 1974,
                    'platinum': True
                    }
               }
          }
#  TODO watch

def add_artist():
    pass

def add_album():
    pass

def add_song():
    pass

def remove_artist():
    pass

def remove_album():
    pass

def remove_song():
    pass

def print_music():
    # print all parts of 'music' dict
    pass

def edit_album():
    # edit songs list, year, and platinum status
    pass

def menu():
    # print menu options
    # take input for option
    # return input

def main():

    var = input('Enter name:\n')
    print('Your name is {}'.format(var))
    print('Newport')

    functions = [add_artist, add_album, add_song,
                 remove_artist, remove_album, remove_song,
                 print_music, edit_album]

    var = 0

    while var != 'exit':
        var = menu()
        functions[var]()



#TODO do this here

if __name__ == "__main__":
    main()
