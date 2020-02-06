def get_len(obj):
    return f'({len(obj)if hasattr(obj, "__len__") else "na"})'

def obj_props(obj, name=''):
    return f'{name+get_len(obj):<20} \t type: {type(obj)}'


def list_inspect(lst, space='|'):
    'Recursivly inspect the elements of a list'
    assert isinstance(lst, list)
    
    for i, elm in enumerate(lst):
        
        if isinstance(elm, dict):
            print(f'{space}i={i}({len(elm)})')
            dict_inspect(elm, space+'\t|')
            
        elif isinstance(elm, list):
            print(f'{space}i={i}({len(elm)})')
            list_inspect(elm, space+'\t|')
        else:
            print(f'{space}{obj_props(elm)}')
            
    
def dict_inspect(dictionary, space='|'):
    'Recursivly inspect the elements of a dictionary'
    assert isinstance(dictionary, dict)
    
    for key, elm in dictionary.items():
        
        if isinstance(elm, dict):
            print(f'{space}{key+get_len(elm):<20}')
            dict_inspect(elm, space+'\t|')

        elif isinstance(elm, list):
            print(f'{space}{key+get_len(elm):<20}')
            list_inspect(elm, space+'\t|')
            
        else:
            print(f'{space}{obj_props(elm, key)}')
