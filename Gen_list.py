import time

# Generowanie listy za pomocą pętli for .. in
start_time = time.time()
lista1 = []
for i in range(1000000):
    lista1.append(i)
end_time = time.time()
print("Czas wykonania pętli for .. in:", end_time - start_time)

# Generowanie listy za pomocą pętli while
start_time = time.time()
lista2 = []
i = 0
while i < 1000000:
    lista2.append(i)
    i += 1
end_time = time.time()
print("Czas wykonania pętli while:", end_time - start_time)

# Generowanie listy za pomocą pętli for .. in wewnątrz deklaracji listy
start_time = time.time()
lista3 = [i for i in range(1000000)]
end_time = time.time()
print("Czas wykonania pętli for .. in wewnątrz deklaracji listy:", end_time - start_time)
