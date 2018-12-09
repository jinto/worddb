import requests
from bs4 import BeautifulSoup


def ndic(word):
    dic = []
    res = requests.get("https://endic.naver.com/search.nhn?sLn=en&query="+word)
    soup = BeautifulSoup(res.text, 'html.parser')
    for header in soup.find_all("div", {"class": "word_num"}):
        found = header.select(".fnt_k05")
        if len(found) == 0:
            continue
        dic.append(found[0].text.strip())
    return dic


for fname in ['level_basic.txt', 'level_mid.txt', 'level_high.txt']:
    dic = open(fname.replace('level', 'ndic'), 'w')

    dic.write("#--\n")
    dic.write("# 이 파일은 프로그램에 의해 생성되는 파일입니다.\n")
    dic.write("# python mkdic.py\n")
    dic.write("# 하시면 됩니다.\n")
    dic.write("# 저작권침해 가능성이 있어, 앞부분만 공유합니다.\n")
    dic.write("#--\n")

    with open(fname) as f:
        for line in f:
            line = line.rstrip()
            print(line)
            dic.write(f"\n{line}\n")

            ret = ndic(line)
            for r in ret:
                if line not in r:
                    dic.write(f"\t{r}\n")
            dic.flush()
