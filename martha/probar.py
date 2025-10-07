import matplotlib.pyplot as plt
import numpy as np
from collections import deque
import time

# Cola para almacenar últimos 100 puntos
angles = deque(maxlen=100)
dists = deque(maxlen=100)

fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)

points, = ax.plot([], [], 'bo', markersize=4)

plt.ion()  # modo interactivo
plt.show()

for i in range(500):  # simular 500 lecturas
    # Generar punto aleatorio
    angle = np.deg2rad(np.random.rand() * 360)
    dist = np.random.rand() * 5

    # Guardar en la cola
    angles.append(angle)
    dists.append(dist)

    # Actualizar gráfico
    points.set_data(angles, dists)
    plt.draw()
    plt.pause(0.01)

plt.ioff()
plt.show()
