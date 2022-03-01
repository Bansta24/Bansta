#Система координат линейной функции

x1=int(input('x1:')) #первая координата
y1=int(input('y1:'))

x2=int(input('x2:'))# вторая координата
y2=int(input('y2:'))

k = int((y1 -y2 ) / (x1 - x2)) # кофициент угла

print(k)
b = int(y2 - k * x2)
print(b)
print(f'y={k}x+{b}')