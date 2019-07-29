import cmath 
imagina = complex(0, 1)

N = 101
a = []
resultado = []
i = 0
j = 0

for i in range(N):
    a.append(50*cmath.exp(-0.025*i))
    resultado.append(complex(0))

im = 1

for i in range(int(-N/2), int(N/2), 1):
    resultado[im] = 0
    k = 1
    for j in range(int(-N/2), int(N/2), 1):
        resultado[im] = (resultado[im] + cmath.exp(imagina*cmath.pi*i*j/N)*a[k])
        k += 1
    im += 1

for i in range(N):
    a.append(1)

print(a)