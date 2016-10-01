def revers(l):
    l.reverse()
    return l

def sortir(q):
    q.sort()
    return q

print u'Введите строку для реверса:'
st = list(raw_input())
print u'Результат: \n' + "".join(revers(st))

print u'Введите строку для сортировки:'
st_int = list(raw_input())
print u'Результат: \n' + ''.join(str(a) for a in sortir(st_int))