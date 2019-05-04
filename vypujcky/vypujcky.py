with open('xkremece_vypujcky.txt', 'r') as f:
    with open('vypujcky.sql', 'w') as out:
        out.write('INSERT INTO `vypujcky` (`exemplare_id`, `datum_pujceni`, `vratit_do`, `osoby_id`, `skutecne_vraceno`, `poznamka`, `vypujcky_id`) VALUES \n')
        for line in f:
            out.write('(')
            data = line.split(',')
            if len(data) == 8:
                poznamka = data[5] + ',' + data[6]
                data[5] = poznamka
                data[6] = data[7]
                data.pop(7)
            for i in range(0, len(data)):
                data[i] = data[i].strip().rstrip()
                #print('Data: "' + data[i] + '"')
            print(data)
            for x in range(0, len(data)):
                if x == (len(data) - 1):
                    if data[x] == "":
                        out.write('NULL),\n')    
                    else:
                        out.write('"' + data[x] + '"),\n')
                else:
                    if data[x] == "":
                        out.write('NULL, ')
                    else:
                        out.write('"' + data[x] + '", ')