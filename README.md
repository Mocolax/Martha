Proyecto Martha
Requisitos Previos
Sistema Operativo

    Ubuntu 22.04 (recomendado)

Instalación de ROS 2 Humble

Sigue la guía oficial de instalación de ROS 2 Humble:

🔗 Documentación oficial de ROS 2 Humble
Verificación de la Instalación

Después de instalar ROS 2 Humble, verifica que esté correctamente configurado:
bash

source /opt/ros/humble/setup.bash
ros2 --version

Instalación del Proyecto Martha
Descarga del Repositorio

Clona el repositorio del proyecto:
bash

mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
git clone https://github.com/Mocolax/martha.git
cd martha

Instalación de Dependencias

Una vez dentro del directorio del proyecto, instala los paquetes necesarios:
bash

# Actualizar lista de paquetes
sudo apt update

# Instalar dependencias (ajusta según tu proyecto)
rosdep install -i --from-path src --rosdistro humble -y

Configuración del Entorno

Configura y construye el proyecto:
bash

# Navegar al workspace
cd ~/ros2_ws

# Construir el proyecto
colcon build --packages-select martha

# Configurar el entorno
source install/setup.bash

Uso del Proyecto

Para ejecutar el proyecto Martha:
bash

# Ejecutar Martha (ajusta el nombre del paquete y launch file)
ros2 launch martha martha_launch.py

# Alternativamente, si quieres ejecutar un nodo específico:
# ros2 run martha martha_node
