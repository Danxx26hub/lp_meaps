import os


def main():
    '''
    on my machine I would enter "formats"
    to start search.
    '''
    dirname = input('Please enter a directory to start searching\n')
    dirname = dirname.lower()
    iter_directory(dirname)


def iter_directory(dirname):
    '''
    walk given directory and only print files if they end in .pdf
    takes one argument "dirname" the directory name to start at.
    '''
    dir_find = os.walk(dirname, topdown=True)
    for root, dirs, files in dir_find:

        if files:
            print(f'found a pdf file : {files[0]}')
        else:
            continue


if __name__ == "__main__":
    main()
