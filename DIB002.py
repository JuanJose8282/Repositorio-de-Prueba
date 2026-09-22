#DIB002
#Entorno 3d con matplotlib

import matplotlib.pyplot as plt

#crea la figura y el eje 3d
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#limites de los ejes
ax.set_xlim(-3,3)
ax.set_ylim(5, 7)
ax.set_zlim(-1, 4)

#etiquetas
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

#titulo
ax.set_title('TITULO')

#muestra todas las labels
#ax.legend()

#quitar los ejes
#ax.set_axis_off()

#muestra la figura
plt.show()
