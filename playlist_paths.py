from os import getcwd, listdir
from os.path import isfile, join, exists, isdir
import fileinput
import string
import sys
import fnmatch

def paths():
    '''
    Converting filepaths in m3u playlists to relative filepaths for Linux.

    Assumesl the file structure is exactly the same once you get into the old iTunesMedia directory, so if you mess that up, you're screwed.

    Also, obviously, this only works on my playlists for now. Possible future work: generalize what you want to delete from the filepaths?
    '''
    folder = input('Where are the playlists? ')

    if not exists(folder):
        return 'directory not found at ' + folder
    if not isdir(folder):
        return folder + ' is not a directory'

    lists = [join(folder, f) for f in listdir(path=folder) if isfile(join(folder, f)) & fnmatch.fnmatch(f, '*.m3u')]

    if len(lists) == 0:
        return 'no .m3u files found in ' + folder

    to_del = 'C:\\Users\\ladyl\\Music\\iTunes\\iTunes Media'

    for p in lists:
        #print('file is ' + p)
        if '.m3u' in p:
            opened = open(p, encoding='cp1252')
            data = opened.read()
            opened.close()

            newdata = data.replace(to_del, '..')

            opened = open(p, mode='w', encoding='utf-8')
            opened.write(newdata)
            opened.close()

    return 'done! check your files!'
