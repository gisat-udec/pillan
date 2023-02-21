### Prototipo 

**Objetivos:** 
* Construir sistema de comunicación escalable
    * Transmitir video desde CANSAT a estación
    * Enviar comandos desde estación a CANSAT

**Subsistemas:**
* Subsistema de comunicación con antenas 5.8GHz

Con adaptadores Wifi y drivers modificados es posible transmitir información con antenas típicas de 2.4GHz y 5GHz utilizadas en dispositivos Wifi, pero sin necesidad de establecer un vínculo entre el punto de acceso y el cliente (SSID y clave), sino que el punto de acceso envía paquetes de manera abierta como si se tratara de señales de radio o televisión por antena, y cualquier cliente que este escuchando el mismo canal puede recibir los paquetes. Esta alternativa de operación se conoce como [wifibroadcast](https://befinitiv.wordpress.com/wifibroadcast-analog-like-transmission-of-live-video-data/) y fue propuesta en un principio por _befinitiv_ para la transmisión de video en drones.

Las placas Raspberry Pi incluyen un conector dedicado para cámaras por interfaz CSI, y en su procesador gráfico tienen un modulo de codificación de video h.264 por hardware, lo que las hace ideales para el propósito de transmitir video por wifi.

El proyecto [wfb-nb](https://github.com/svpcom/wfb-ng) incluye una implementación de este sistema con la particularidad de que permite la comunicación entre un Raspberry Pi Zero W y cualquier notebook convencional, reduciendo significativamente los costos del primer prototipo puesto que ya se tiene ese Raspberry. El único hardware que comprar son los [adaptadores wifi](https://github.com/svpcom/wfb-ng/wiki/WiFi-hardware) y una [cámara CSI](https://www.raspberrypi.com/documentation/accessories/camera.html) compatible con la RPi Zero W.

Una vez funcional, se puede escalar comprando mejores [antenas direccionales](https://www.google.com/search?q=wifi+directional+antennas&tbm=isch) que permitan largas distancias y mejores cámaras en caso de ser necesario.


* Subsistema de orientación de antena en estación

Para poder transmitir la señal de video en largas distancias como el estimado de 1 km de altura a la que debe llegar el CANSAT, es necesaria una antena  direccional apuntada de manera relativamente precisa desde la estación en tierra.

Orientar de manera automática la antena para que siga el recorrido es posible gracias a que se puede obtener la posición del CANSAT por medio de sus sensores, de los que para este subsistema destacan el **barómetro**, **GPS** y el **IMU** (Inertial measurement unit). Agregando un segundo GPS a la estación en tierra se obtienen coordenadas GPS diferenciales entre la estación y el CANSAT lo que permite dirigir el ángulo **azimutal** de la antena. La altitud se estima con las lecturas de presión del barómetro y también es verificado por GPS para ajustar el angulo de **elevación** de la antena. El IMU entrega aceleración de acuerdo a un sistema de referencia ajustado a la tierra y se pueden obtener cambios en la posición integrando dos veces, si bien esta lectura sera muy propensa a errores a lo largo del tiempo de todas formas sirve para complementar.

El movimiento mismo de la antena es controlado por dos **servos**, que controlen el ángulo azimutal y la elevación. El error de los movimientos debido a la falta de precisión en los servos puede ser compensado con un segundo IMU instalado en la antena.

Este subsistema requiere más análisis para verificar si es posible o o si es siquiera necesario construirlo. Se conocen como _Antenna Tracking System_