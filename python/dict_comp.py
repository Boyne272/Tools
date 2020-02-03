"""Quick function for comarping dicts element by element."""


def dict_comp(a, b, pref=''):
    """Print non-equal key:value pairs (incl. nested dictionaries)."""
    if a.keys() != b.keys():
        raise KeyError('Dictionaries do not have matchine keys')

    for k in a.keys():
        if isinstance(a[k], dict):
            dict_comp(a[k], b[k], pref=k+'.')
        elif a[k] == b[k]:
            print(pref + k, 'Not equal:')
            print(a[k], b[k], '\n\n')
