from bs4 import BeautifulSoup

columns = ["osoby_id", "login", "jmeno", "prijmeni", "heslo", "email", "oddeleni_id"]

html_doc = open('xkremece_osoby.html')

soup = BeautifulSoup(html_doc, 'html.parser')

trtags = soup.find_all('tr')

with open('osoby.sql', 'w') as out:
    out.write('INSERT INTO `osoby` (`osoby_id`, `login`, `jmeno`, `prijmeni`, `heslo`, `email`, `oddeleni_id`) VALUES \n')
    for person in trtags:
        personDataTags = person.findChildren('td')
        personDataList = list(personDataTags)
        print("Osoba:")
        out.write('(')
        for dataIndex in range(0, len(personDataList)):
            #print(type(personDataList[dataIndex].string))
            if isinstance(personDataList[dataIndex].string, str):
                print("  " + columns[dataIndex] + ": " + personDataList[dataIndex].string)
                if dataIndex == (len(personDataList) - 1):
                    out.write('"' + personDataList[dataIndex].string + '"')
                else:
                    out.write('"' + personDataList[dataIndex].string + '", ')
            else:
                if dataIndex == (len(personDataList) - 1):
                    out.write('NULL')
                else:
                    out.write('NULL, ')
                #print("  " + columns[dataIndex] + ": " + "")
        out.write('), \n')
        #print("Person:")
        #print("  ID:", mylist[0].string)
        #ids.append(mylist[0].string)
        #print("  Value:", mylist[1].string)
        #values.append(mylist[1].string)
        #print("  Login:", mylist[2].string)