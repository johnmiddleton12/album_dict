# album dictionary

music = {'Travis Scott':  # Key
             {'Astroworld':
                  {'songs': ['Stargazing', 'Carousel', 'Sicko Mode',
                             'R.I.P. Screw', 'Stop Trying to Be God',
                             'No Bystanders', 'Skeletons', 'Wake Up',
                             '5% Tint', 'NC-17', 'Astrothunder', 'Yosemite',
                             'Can’t Say', 'Who? What!', 'Butterfly Effect',
                             'Houstonfornication', 'Coffee Bean'],
                   'year': 2018,
                   'platinum': True
                   },
                'Rodeo':
                    {'songs': ['Pornography', 'Oh My Dis Side', '3500', 'Wasted',
                                  '90210', 'Pray 4 Love', 'Nightcrawler', 'Piss on Your Grave',
                                  'Antidote', 'Impossible', "Maria I'm Drunk", 'Flying High',
                                  'I Can Tell', 'Apple Pie', 'Ok Alright', 'Never Catch Me'],
                    'year': 2015,
                    'platinum': True
                    }

              }
         }


#  TODO watch

def add_artist():
    print('You selected to add an artist')


def add_album():
    print('You selected to add an album')


def add_song():
    print('You selected to add a song')


def remove_artist():
    print('You selected to remove an artist')


def remove_album():
    print('You selected to remove an album')


def remove_song():
    print('You selected to remove a song')


def print_music():
    # print all parts of 'music' dict
    print('You selected to print the dictionary')
    for artists in music:
        print(artists)
        for albums in music[artists]:
            print(albums)
            print('Songs:', end = ' ')
            for i in music[artists][albums]['songs']:
                if i == music[artists][albums]['songs'][-1]:
                    print(i)
                else:
                    print(i, end = ', ')








def edit_album():
    # edit songs list, year, and platinum status
    print('You selected to edit an album')

def menu():
    # print menu options
    # take input for option
    # return input
    print('Option 0: Add artist')
    print('Option 1: Add album')
    print('Option 2: Add song')
    print('Option 3: Remove artist')
    print('Option 4: Remove album')
    print('Option 5: Remove song')
    print('Option 6: Print dictionary')
    print('Option 7: Edit an album')
    var = int(input('What option would you like to choose?: \n'))
    return var


def main():
    functions = [add_artist, add_album, add_song,
                 remove_artist, remove_album, remove_song,
                 print_music, edit_album]


    var = 0

    while var != 'exit':  # close for loop by making input asking if the user wants to continue or exit
        var = menu()
        functions[var]()


if __name__ == "__main__":
    main()
