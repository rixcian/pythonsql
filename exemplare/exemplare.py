idExemplare = []
idKnih = []
idOsoby = []
poznamky = []
idOddeleni = []

with open('xkremece_exemplare.json', 'r') as f:
    #fcontent = f.readline()
    #print(fcontent)
    for line in f:
        #print(line, end='')
        line = line.strip()
        line = line.rstrip()
        if line == '"xkremece_exemplare":{':
            exemplare_id = f.readline().strip().rstrip()
            #value = ((len(vyrazy_id) - (len(vyrazy_id) - 11)*2))
            exemplare_id = exemplare_id.replace('"exemplare_id": ', '')
            exemplare_id = exemplare_id.replace(',', '')
            idExemplare.append(exemplare_id)
            print('ID exemplare: ' + exemplare_id)
            knihy_id = f.readline().strip().rstrip()
            knihy_id = knihy_id.replace('"knihy_id": ', '')
            knihy_id = knihy_id.replace(',', '')
            idKnih.append(knihy_id)
            print('ID knihy: ' + knihy_id)
            osoby_id = f.readline().strip().rstrip()
            osoby_id = osoby_id.replace('"osoby_id": ', '')
            osoby_id = osoby_id.replace(',', '')
            idOsoby.append(osoby_id)
            print('ID osoby: ' + osoby_id)
            poznamka = f.readline().strip().rstrip()
            poznamkaText = '"poznamka":'
            if poznamkaText in poznamka:
                poznamka = poznamka.replace('"poznamka": ', '')
                poznamka = poznamka.replace(',', '')
                poznamky.append(poznamka)
                print('poznamka: ' + poznamka)
                oddeleni_id = f.readline().strip().rstrip()
                oddeleni_id = oddeleni_id.replace('"oddeleni_id": ', '')
                oddeleni_id = oddeleni_id.replace(',', '')
                idOddeleni.append(oddeleni_id)
                print('ID oddeleni: ' + oddeleni_id + '\n')
            else:
                oddeleni_id = poznamka
                poznamka = 'NULL'
                poznamky.append(poznamka)
                print('poznamka: ' + poznamka)
                oddeleni_id = oddeleni_id.replace('"oddeleni_id": ', '')
                oddeleni_id = oddeleni_id.replace(',', '')
                idOddeleni.append(oddeleni_id)
                print('ID oddeleni: ' + oddeleni_id + '\n')

    with open('exemplare.sql', 'w') as out:
                out.write('INSERT INTO `exemplare` (`exemplare_id`, `knihy_id`, `osoby_id`, `poznamka`, `oddeleni_id`) VALUES \n')
                for i in range(0, len(idExemplare)):
                    if i == (len(idExemplare) - 1):
                        out.write('("' + idExemplare[i] + '", "' + idKnih[i] + '", "' + idOsoby[i] + '", "' + poznamky[i] + '", "' + idOddeleni[i] + '");')
                    else:
                        out.write('("' + idExemplare[i] + '", "' + idKnih[i] + '", "' + idOsoby[i] + '", "' + poznamky[i] + '", "' + idOddeleni[i] + '"),\n')
