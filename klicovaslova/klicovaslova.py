with open('xkremece_klicova_slova.txt', 'r') as f:
    with open('klicovaslova.sql', 'w') as out:
        out.write('INSERT INTO `klicova_slova` (`knihy_id`, `vyrazy_id`) VALUES \n')
        for line in f:
            out.write('(')
            data = line.split(',')
            for i in range(0, len(data)):
                data[i] = data[i].strip().rstrip()
            print(data)
            for x in range(0, len(data)):
                if x == (len(data) - 1):
                    out.write('"' + data[x] + '"),\n')
                else:
                    out.write('"' + data[x] + '", ')