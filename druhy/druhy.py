from bs4 import BeautifulSoup

html_doc = open('xkremece_druhy.html')

soup = BeautifulSoup(html_doc, 'html.parser')

trtags = soup.find_all('tr')

ids = []
values = []

# filling lists (ids, values) by values
for tr in trtags:
    tdtags = tr.findChildren('td')
    mylist = list(tdtags)
    if len(mylist) > 0:
        print("Item:")
        print("  ID:", mylist[0].string)
        ids.append(mylist[0].string)
        print("  Value:", mylist[1].string)
        values.append(mylist[1].string)

# INSERT INTO `druh` (`druhy_id`, `nazev`) VALUES ('6', 'DVD'), ('7', 'Video')

with open('druhy.sql', 'w') as out:
    out.write('INSERT INTO `druhy` (`druhy_id`, `nazev`) VALUES \n')
    for index in range(0, len(ids)):
        if index == (len(ids) - 1):
            out.write('("' + ids[index] + '", "' + values[index] + '")')
        else:
            out.write('("' + ids[index] + '", "' + values[index] + '"), \n')
