# Este programa reduce los duplicados en un string, colocando los elementos sin repetir en una lista aparte
# Tiene complejidad O(n), siendo n el size del input


s = 'AAAABBBCCDAABBB'
#s = 'ABBCcA'
#s = [1, 2, 3, 3, -1]

unique = []
last = ''

for c in s:
    if c != last:
        unique.append(c)
        last = c

print(unique)
