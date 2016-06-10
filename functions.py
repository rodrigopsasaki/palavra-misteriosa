def match(p1, p2):
    if not p1:
        return True
    else:
        if p2:
            if p1[0] == p2[0] or p1[0] == u'':
                return match(p1[1:], p2[1:])
            else:
                return False

def palavras_possiveis(letras):
    print letras
    palavras  = open('static/resources/palavras_10.txt').read().split('\n')
    print len(palavras)
    return (palavra for palavra in palavras if match(letras, palavra))
