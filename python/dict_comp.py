"""Quick function for comarping dicts element by element."""

LINE = '\n\n' + '-'*20 + '\n\n'

def dict_comp(a, b, pref=''):
    """Print non-equal key:value pairs (incl. nested dictionaries)."""
    if a.keys() != b.keys():
        raise KeyError('Dictionaries do not have matchine keys')

    for k in a.keys():
        if isinstance(a[k], dict):
            dict_comp(a[k], b[k], pref=k+'.')
        else:
            print(pref + k, ' equal ', a[k] == b[k])

            if a[k] != b[k]:
                print(LINE, a[k], LINE, b[k], LINE)
