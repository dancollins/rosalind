def fasta(iterator):
    '''
    Extracts DNA strings in FASTA format, yielding the name and the string
    itself.
    '''
    name = None
    data = ''
    for line in iterator:
        if '>' in line:
            if data:
                yield name, data
            name = line.rstrip()[1:]
            data = ''
        else:
            data += line.rstrip()

    # Following EOF, we need to flush out the last string
    yield name, data
