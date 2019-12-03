# Nested data in lists and dictionaries

mix_list = ['strings', 98, ['more strings', [1, 2, 'important']]]
print(type(mix_list[1])) #Int (98)

## Extract certain chunk of list
internal_list = mix_list[2]
print(internal_list)

## Extract specific items within lists within lists

print(internal_list[1] [2]) #3rd item within the 2nd item of the list


embeded_dict = {
    'Status': 'Operational',
    'Keys': ['Car Keys', 'Boat Keys', 'Mansion Keys', 'Dog House Keys'],
    'Staff': {
        'Julio Cesar': {
            'Name': 'Julius',
            'Last_Name': 'Caesar',
            'Birthdate': '100 BC',
            'Job': 'Roman Dictator'
        },
        'Adolf Hitler': {
            'Name': 'Adolf',
            'Last_Name': 'Hitler',
            'Birthdate': '1889',
            'Job': 'Dictator'
        }
    }
}

print(embeded_dict['Keys'][1], embeded_dict['Keys'][2])
print(embeded_dict['Staff']['Julio Cesar'])
print(embeded_dict['Staff']['Adolf Hitler']['Last_Name'], embeded_dict['Staff']['Adolf Hitler']['Birthdate'], embeded_dict['Staff']['Adolf Hitler']['Job'])
