w = open('../static/resources/palavras_10.txt', 'w')

palavras_10 = [p for p in open('../static/resources/palavras.txt') if len(p.strip()) == 10]
for palavra in palavras_10:
    w.write(palavra)
