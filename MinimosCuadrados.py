import random as rd
import math as mt
import numpy as np
import random as rd
import copy as cp
import matplotlib.pyplot as plt

P = [[1, 20.214],
[2, 18.413],
[3, 15.754],
[4, 14.125],
[5, 14.024],
[6, 13.226],
[7, 15.458],
[8, 14.547],
[9, 14.754],
[10, 13.536],
[11, 12.425],
[12, 10.543],
[13, 10.058],
[14, 9.135],
[15, 7.698],
[16, 5.564],
[17, 4.213],
[18, 3.896],
[19, 6.012],
[20, 7.894],
[21, 10.214],
[22, 12.266],
[23, 15.124],
[25, 16.989],
[26, 19.014],
[27, 21.254],
[28, 22.887],
[29, 24.364],
[30, 25.898]]

n = len(P)
X = list()
Y = list()
C = 0.000001
for i in range(n):
   X.append(P[i][0])

for i in range(n):
   Y.append(P[i][1])

def Segmented_Least_Squares():
  M = [10000000]*(n)
  M[0] = 0
  E = [0]*n
  for i in range(n): 
    E[i] = [0]*n

  A = [0]*n
  for i in range(n): 
    A[i] = [0]*n

  B = [0]*n
  for i in range(n): 
    B[i] = [0]*n
    
  for j in range(1, n):
    for i in range(j):
      E[i][j], A[i][j], B[i][j] = SEE(i, j)

  I = list()
  J = list()
  for j in range(1,n):
    for i in range(j):
      if i == 0:
        optant = 0
      else:
        optant = M[i] 
      if M[j] > (E[i][j] + C + optant):
        M[j] = (E[i][j] + C + optant)
        z=i
    I.append(z)
    J.append(j)
    print(f"i={z},j={j}")


  
  return M, A, B, I, J

def SEE(i, j):
  nseg = (j-i)+1
  a = obtenera(i, j, nseg)
  b = obtenerb(i, j, nseg, a)
  for i in range(j):
    see = (Y[i] -a*X[i]-b)**2 
  return see, a, b

def obtenera(i, j, nseg):
  a = (nseg*sumaXY(i, j)-(sumaX(i, j)*sumaY(i, j)))/((nseg*sumaX2(i, j))-(sumaX(i, j))**2)
  return a

def obtenerb(i, j, nseg, a):
  b = (sumaY(i, j) - a*sumaX(i, j))/nseg
  return b

def sumaX(i, j, sumaX = 0):
  for z in range(i,j+1):
    sumaX = sumaX + X[z]
  return sumaX

def sumaY(i, j, sumaY = 0):
  for z in range(i,j+1):
    sumaY = sumaY + Y[z]
  return sumaY

def sumaX2(i, j, sumaX2 = 0):
  for z in range(i,j+1):
    sumaX2 = sumaX2 + (X[z])**2
  return sumaX2

def sumaXY(i, j, sumaXY = 0):
  for z in range(i,j+1):
    sumaXY = sumaXY + (X[z]*Y[z])
  return sumaXY


def Graficapuntos():
  plt.scatter(X, Y, color='red', marker='o')  # 'o' representa círculos como marcadores

  # Agregar etiquetas y título
  plt.xlabel('Eje X')
  plt.ylabel('Eje Y')
  plt.title('Gráfico de Puntos')

  for i in range(m-1):
    print(f'i={index[i]},i+1={index[i+1]}')
    x = np.linspace(X[index[i+1]], X[index[i]], 10)  
    y = x*A[index[i+1]][index[i]]+B[index[i+1]][index[i]]
    # Graficar la recta
    plt.plot(x, y, color='blue')
  # Mostrar el gráfico
  plt.show()
'''
  x1 = np.linspace(X[0], X[5], 22)  
  y1 = x1*A[0][5]+B[0][5]
  # Graficar la recta
  plt.plot(x1, y1, color='blue')

  x2 = np.linspace(X[5], X[6], 22)  
  y2 = x2*A[5][6]+B[5][6]
  # Graficar la recta
  plt.plot(x2, y2, color='blue')

  x3 = np.linspace(X[6], X[17], 22)  
  y3 = x3*A[6][17]+B[6][17]
  # Graficar la recta
  plt.plot(x3, y3, color='blue')
 
  x4 = np.linspace(X[17], X[28], 22)  
  y4 = x4*A[17][28]+B[17][28]
  # Graficar la recta
  plt.plot(x4, y4, color='blue')
'''

  

OPT, A, B, I, J= Segmented_Least_Squares()

index = list()
index.append(28)
num = 28
while True:
  num = I[num-1]
  index.append(num)
  if num == 0:
    break
m = len(index)

Graficapuntos()
print(SEE(5,6))