num = int(input("How many figures : ")) 
storage = []
result = []

# Erstellen eines Arrays von Benutzernummern
for i in range(1,num+1):
    a = int(input("Enter value" + str(i) + " : "))
    storage.append(a) # user enter

# Array sortieren
for m in range(len(storage)):
    b = min(storage)
    storage.remove(b)
    result.append(b) # user get
j = ' '.join(str(i) for i in result)
print(j)
