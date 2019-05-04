import json

with open('xkremece_jazyky.json', 'r') as file:
    data = file.read().replace('\n', '')

j = json.loads(data)

with open('jazyky.sql', 'w') as out:
    out.write('INSERT INTO `jazyky` (`jazyky_id`, `nazev`) VALUES \n')
    for i in range(1, len(j) + 1):
        index = 'xkremece_jazyky' + str(i)
        jazyk = j[index]['nazev']
        if i == len(j):
            out.write('("' + str(i) + '", "' + jazyk + '")')
        else:
            out.write('("' + str(i) + '", "' + jazyk + '"), \n')