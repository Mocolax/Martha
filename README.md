# Proyecto Martha

## Requisitos Previos

### Sistema Operativo
- Ubuntu 22.04 (recomendado)

---

## Instalación de ROS 2 Humble

Sigue la guía oficial de instalación de ROS 2 Humble:  
🔗 [Documentación oficial de ROS 2 Humble](https://docs.ros.org/en/humble/Installation.html)

### Verificación de la Instalación

Después de instalar ROS 2 Humble, verifica que esté correctamente configurado.  
Añade al final del archivo `~/.bashrc` lo siguiente:

```bash
sudo nano ~/.bashrc

# Añadir estas líneas al final
source /opt/ros/humble/setup.bash
source ~/ros2_ws/install/setup.bash

Instalación del Proyecto Martha
Descarga del Repositorio

Clona el repositorio del proyecto:

mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
git clone https://github.com/Mocolax/martha.git
cd martha

Configuración del Entorno

Configura y construye el proyecto:

# Navegar al workspace
cd ~/ros2_ws

# Construir el proyecto
colcon build --packages-select martha

# Configurar el entorno
source install/setup.bash

# Dar permisos al puerto
sudo chmod 777 /dev/ttyACM1

Uso del Proyecto

Para ejecutar el proyecto Martha:

# Ejecutar Martha (ajusta el nombre del paquete y launch file si es necesario)
ros2 launch martha martha_setup.launch.py

Alternativamente, si quieres ejecutar un nodo específico:

ros2 run martha martha_node
