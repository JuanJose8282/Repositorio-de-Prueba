#DIB003
#Entorno 3d con matplotlib

import matplotlib.pyplot as plt

#crea la figura 
fig = plt.figure()

#1 grafico en 3d (en la misma ventana)
#111= 1 fila, 1 columna, subplot numero 1
#ax = fig.add_subplot(111, projection='3d')

#2 graficos en 3d (en la misma ventana, en fila)
#12x= 2 filas, 1 columna, subplot numero x
#ax1 = fig.add_subplot(121, projection='3d')
#ax2 = fig.add_subplot(122, projection='3d')

#4 graficos en 3d (en la misma ventana, dos filas, dos columnas)
#22x= 2 filas, 2 columnas, subplot numero x
ax1 = fig.add_subplot(221, projection='3d')
ax2 = fig.add_subplot(222, projection='3d')
ax3 = fig.add_subplot(223, projection='3d')
ax4 = fig.add_subplot(224, projection='3d')

#los objetos se agregan a los axes

#muestra la figura
plt.show()
