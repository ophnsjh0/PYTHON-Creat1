import re

def extraction():
    f = open('extraction.txt', 'r', encoding='UTF-8')
    s = f.read()
    korean = re.compile('[\u3131-\u3163\uac00-\ud7a3]+')   
    parse_korea_text = re.sub(korean, "", s)    
    parse_english_text = re.sub(r'[A-Z]|[a-z]', "", parse_korea_text)
    parse_special_text = re.sub('[=_#/?:$}"())]', "", parse_english_text)
    # print(split_text)
    ip_extraction = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}' , parse_english_text)
    ip = []
    for i in ip_extraction:
        m = i.split('.')
        # print(m)
        m[-1] = '0'
        r = '.'.join(m)
        ip.append(r)
    ip.sort()
    Set = set(ip)
    print(Set)
    r = open('result.txt', 'w')
    for i in Set:
        r.write('{0}\n'.format(i))
    r.close()

extraction()
print("done")
