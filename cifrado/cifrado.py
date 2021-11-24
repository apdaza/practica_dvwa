from collections import Counter

def corrimiento(caracter):
    if caracter == "_":
        return "_"
    else:
        return original[corrido.index(caracter)]

original = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
corrido = ['D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C']


m = ["HLWWGWHGHBDQOHLGSWW_UHGO",
     "OQLRLDOHU__WLQDDUHRSDOLR",
     "_VQ_F__E_OLHJF__HAVD_XU_"]

m1 = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]     

temp = ""

for i in range(len(m1)):
    for j in range(len(m1[i])):
        temp += m1[i][j]

print(temp)

temp1 = ""
for c in temp:
    temp1 += corrimiento(c)

print(temp1)
