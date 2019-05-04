vyrazy = []
texty = []

with open('xkremece_vyrazy.json', 'r') as f:
    #fcontent = f.readline()
    #print(fcontent)
    for line in f:
        #print(line, end='')
        line = line.strip()
        line = line.rstrip()
        if line == '"xkremece_vyrazy":{':
            vyrazy_id = f.readline().strip().rstrip()
            #value = ((len(vyrazy_id) - (len(vyrazy_id) - 11)*2))
            vyrazy_id = vyrazy_id.replace('"vyrazy_id": ', '')
            vyrazy_id = vyrazy_id.replace(',', '')
            vyrazy.append(vyrazy_id)
            print('ID vyrazu: ' + vyrazy_id)
            text = f.readline().strip().rstrip()
            text = text.replace('"text": ', '')
            texty.append(text)
            print('Text: ' + text + '\n')
    
    with open('vyrazy.sql', 'w') as out:
                out.write('INSERT INTO `vyrazy` (`vyrazy_id`, `text`) VALUES \n')
                for i in range(0, len(vyrazy)):
                    if i == (len(vyrazy) - 1):
                        out.write('("' + vyrazy[i] + '", "' + texty[i] + '");')
                    else:
                        out.write('("' + vyrazy[i] + '", "' + texty[i] + '"),\n')