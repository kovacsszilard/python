from typing import List

a: str='Karakterláncok kezelése'
print(a)
print(a[1])
print(a[2:])
print(a[2:9])

#strint hossza:
print(len(a))

# Strint darabolása:

darabolt: List[str]=a.split('á') # á nem kerül bele
print(darabolt)