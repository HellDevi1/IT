print u'Введите строку для реверса:'
st = list(raw_input())
st.reverse()
print u'Результат: \n' + "".join(st)

print u'Введите строку для сортировки:'
st_int = list(raw_input())
st_int.sort()
print u'Результат: \n' + ''.join(str(a) for a in st_int)