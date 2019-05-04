import xml.etree.ElementTree as ET

root = ET.parse('xkremece_knihy.xml').getroot()

columns = ["isbn", "nazev", "pocet_stran", "rok_vydani", "misto_vydani", "nakladatel", "vydani", "edice", "autor", "druhy_id", "jazyky_id"]

with open('knihy.sql', 'w') as out:
    out.write('INSERT INTO `knihy` (`knihy_id`, `isbn`, `nazev`, `pocet_stran`, `rok_vydani`, `misto_vydani`, `nakladatel`, `vydani`, `edice`, `autor`, `druhy_id`, `jazyky_id`) VALUES \n')
    for type_tag in root.findall('xkremece_knihy'):
        out.write('("' + type_tag.get('knihy_id') + '", ')
        value = type_tag.get('knihy_id')
        print(value)
        childs = list(type_tag)
        childsTagNames = []
        for child in childs:
            print("  Tag:", child.tag, " Value:", child.text)
            childsTagNames.append(child.tag)
        for i in range(0, len(columns)):
            try:
                tagIndex = childsTagNames.index(columns[i])
                if i == (len(columns) - 1):
                    out.write('"' + childs[tagIndex].text + '"), \n')
                else:
                    out.write('"' + childs[tagIndex].text + '", ')
            except ValueError as e:
                if i == (len(columns) - 1):
                    out.write('NULL), \n')
                else:
                    out.write('NULL, ')
        #print("Edice:", childsTagNames.index("edice"))