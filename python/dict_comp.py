"""Quick function for comarping dicts element by element."""

LINE = f'\n{"-"*38}\n'

def dict_comp(a, b, a_name='dict_a', b_name='dict_b', pref=''):
    """Print non-equal key:value pairs (incl. nested dictionaries)."""
    if a.keys() != b.keys():
        raise KeyError('Dictionaries do not have matchine keys')
        
    if not pref:
        print(f'{LINE[1:]}{"Key": <32}Equal{LINE}')
        
    diffs = []
    
    for k in a.keys():
        if isinstance(a[k], dict):
            dict_comp(a[k], b[k], pref=k+'.')
        else:
            print(f'{pref + k: <32} {a[k] == b[k]}')

            if a[k] != b[k]:
                diffs.append((pref + k, a[k], b[k]))
    
    print(f'\n{LINE}\t\tDiffs{LINE}')
    for element_name, el_a, el_b in diffs:
        print(f'{a_name}.{element_name}:\t {el_a}{LINE}')
        print(f'{b_name}.{element_name}:\t{el_b}{LINE}')
