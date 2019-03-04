SUFFIXES = ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']

def approximate_size(size):
    '''Convert a file to humn-readalble form.'''
    multiple = 1024
    for suffix in SUFFIXES:
        size /= multiple
        if size < multiple:
            return f'{size} {suffix}'
    raise ValueError('number too large')

