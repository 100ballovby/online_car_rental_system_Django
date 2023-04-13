with open('dump.json', 'r', encoding='utf-16') as f:
    data = f.read()
    newdata = open('new_dump.json', 'w', encoding='utf-8')
    newdata.write(data)
    newdata.close()

