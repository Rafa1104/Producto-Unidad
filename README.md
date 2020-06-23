# TARJETAS DE DESARROLLO

## 1. PLANTEAMIENTO


## 2. OBJETIVOS
### **Objetivo General**
Describir todos los componentes electrónicos y conectores de las tarjetas de desarrollo: ARDUINO UNO, MICRO BIT, RASPBERRY PI mediante el uso de las siguientes plataformas que son: MICRO BIT, TINKER CAD y CREATED WITHCODE, para entender el lenguaje de programación empleado en la elaboración de aplicaciones de las tarjetas de desarrollo. 

### **Objetivos específicos**
- Entender el funcionamiento de cada una de nuestras tarjetas de desarrollo para poder ser empleadas de manera correcta en un circuito lógico.

- Explicar el lenguaje de programación empleado para el desarrollo de aplicaciones en las tarjetas de desarrollo para Micro bit, Arduino uno y Raspberry pi.


## 3. ESTADO DEL ARTE


## 4. MARCO TEORIÓCO
### ARDUINO 
Arduino es una plataforma de hardware de código abierto, basada en una placa de circuito impreso que contiene un microcontrolador de marca ATMEL que cuenta con entradas y salidas, analógicas y digitales, en un entorno de desarrollo que está basado en el lenguaje de programación procesing. El dispositivo conecta el mundo físico con el mundo virtual, o el mundo analógico con el digital controlando, sensores, alarmas, sistemas de luces, motores, y actuadores. (Tapia & Manzano, 2013)

Hay muchas otros microcontroladores y plataformas disponibles para la computación física donde las funcionalidades y herramientas son muy complicadas de programar, Arduino simplifica el proceso de trabajar con microcontroladores, ofrece algunas ventajas y características respecto a otros sistemas. (Tapia & Manzano, 2013)

**Ventajas del Uso de Arduino**

Según (Enríquez, 2009), las siguientes son las ventajas de usar una placa Arduino:
Barato: Las placas Arduino son relativamente baratas comparadas con otras plataformas microcontroladoras. La versión menos cara del módulo Arduino puede ser ensamblada a mano, e incluso los módulos de Arduino pre ensamblados cuestan menos de 50$.

Multiplataforma: El software de Arduino se ejecuta en sistemas operativos Windows, Macintosh OSX y GNU/Linux. La mayoría de los sistemas microcontroladores están limitados a Windows.

Entorno de programación simple y claro: El entorno de programación de Arduino es fácil de usar para principiantes, pero suficientemente flexible para que usuarios avanzados puedan aprovecharlo también. Para profesores, está convenientemente basado en el entorno de programación Processing, de manera que estudiantes aprendiendo a programar en ese entorno estarán familiarizados con el aspecto y la imagen de Arduino.

Código abierto y software extensible: El software Arduino está publicado como herramientas de código abierto, disponible para extensión por programadores experimentados. El lenguaje puede ser expandido mediante librerías C++, y la gente que quiera entender los detalles técnicos pueden hacer el salto desde Arduino a la programación en lenguaje AVR C en el cual está basado. De forma similar, puedes añadir código AVR-C directamente en tus programas Arduino si quieres.

Código abierto y hardware extensible: El Arduino está basado en microcontroladores ATMEGA8 y ATMEGA168 de Atmel. Los planos para los módulos están publicados bajo licencia Creative Commons, por lo que diseñadores experimentados de circuitos pueden hacer su propia versión del módulo, extendiéndolo y mejorándolo. Incluso usuarios relativamente inexpertos pueden construir la versión de la placa del módulo para entender cómo funciona y ahorrar dinero.

**Descripción de la Placa Arduino**
![](https://github.com/Rafa1104/Producto-Unidad/blob/master/img/placa-arduino-uno.jpg) 
![](https://github.com/Rafa1104/Producto-Unidad/blob/master/img/arduino%20uno%20partes.jpg)

1. Conector USB: proporciona la comunicación para la programación y la toma de
datos, también provee una fuente de 5VDC para alimentar al Arduino, pero de
baja corriente por lo que no sirve para alimentar motores de gran potencia.

2. Regulador de voltaje de 5V: se encarga de convertir el voltaje ingresado por el
plug 3, en un voltaje de 5V regulado necesario para el funcionamiento de la
placa y para alimentar circuitos externos.

3. Plug de conexión para fuente de alimentación externa: Es el voltaje que se
suministra que debe ser directo y estar entre 6V y 18V o hasta 20V,
generalmente se debe tener cuidado de que el terminal del centro del plug quede
conectado a positivo ya que algunos adaptadores traen la opción de intercambiar
la polaridad de los cables.

4. Puerto de conexiones: Es constituido por 6 pines de conexión con las funciones
de RESET que permite resetear el microcontrolador al enviarle un cero lógico.
Pin 3.3V provee una fuente de 3.3VDC para conectar dispositivos externos como
en la protoboard por ejemplo. Pin 5V es una fuente de 5VDC para conectar
dispositivos externos. Dos pines GND que permite la salida de cero voltios para
dispositivos externos. Pin Vin, este pin está conectado con el dispositivo del
plug 3 por lo que se usa para conectar la alimentación de la placa con una
fuente externa de entre 6 y 12VDC en lugar del plug 3 o la alimentación por el
puerto USB. 

5. Puertos de entradas análogas: lugar donde se conectan las salidas de los
sensores análogos. Estos pines solo funcionan como entradas recibiendo voltajes
entre cero y cinco voltios directos. 

6. Microcontrolador ATmega 328: Implementado con los Arduino uno en la versión SMD
del arduino UNO R2 se usa el mismo microcontrolador pero en montaje
superficial, en este caso las únicas ventajas son la reducción del peso y ganar
un poco de espacio.

7. Botón Reset: permite resetear el microcontrolador haciendo que reinicie el
programa.

8. Pines de programación ICSP: Son usados para programar microcontroladores en
protoboard o sobre circuitos impresos sin tener que retirarlos de su sitio. 

9. Led ON: Enciende cuando el Arduino está encendido.

10. Leds de Recepción y Transmisión: Se encienden cuando la tarjeta se comunica con
el PC. El Tx indica transmisión de datos y el Rx recepción.

11. Puertos de conexiones de pines de entradas o salidas digitales: La
configuración como entrada o salida debe ser incluida en el programa. Cuando se
usa la terminal serial es conveniente no utilizar los pines como cero (Rx) y
uno (Tx). Los pines 3, 5 y 6 están precedidos por el símbolo ,
lo que indica que permiten su uso como salidas controladas por ancho de pulso
PWM.

12. Puerto de conexiones 5 entradas o salidas adicionales: Las salidas 9, 10 y 11
permiten control por ancho de pulso; la salida 13 es un poco diferente pues
tiene conectada una resistencia en serie lo que permite conectar un led
directamente entre ella y tierra. Finalmente hay una salida a tierra GND y un
pin AREF que permite ser empleado como referencia para las entradas análogas. 

13. Led pin 13: Indica el estado en que se encuentra.

14. Pines de programación ISCP: Son usados para programar microcontroladores en
protoboard o sobre circuitos impresos sin tener que retirarlos de su sitio. 

15. Chip de comunicación: Permite la conversión de serial a USB.

### Micro:Bit
BBC micro: bit es una pequeña tarjeta programable de 4x5 cm diseñada para que aprender a programar sea fácil, divertido y al alcance de todos.
Gracias a la gran cantidad de sensores que incorpora, sólo con la tarjeta se pueden llevar a cabo centenares de proyectos. BBC micro: bit también es una plataforma IoT (Internet of Things), lo que la hace muy interesante para usuarios avanzados. Y es Open Source, por supuesto. Tanto el hardware como el software de “micro:bit” es de código abierto.

La tarjeta micro:bit dispone de:
- 25 LEDs programables individualmente.
- 2 botones programables.
- Pines de entrada y salida.
- Sensor de Luz y Temperatura.
- Sensores de movimiento (acelerómetro y brújula).
- Comunicación inalámbrica, vía Radio y Bluetooth.
- USB y Conector para batería externa.
![](https://github.com/Rafa1104/Producto-Unidad/blob/master/img/microbit.png)

Tiene un entorno de programación gráfico propio: MakeCode de Microsoft, un sencillo editor gráfico online muy potente y gratuito que posibilita introducirnos en el mundo de la programación de forma intuitiva a través del lenguaje de programación visual o de bloques. Con él aprendemos a pensar como un programador sin caer en los molestos errores de sintaxis. MakeCode es, sin duda, una herramienta a tener muy en cuenta por nuestros profesores.
A continuacion se muestra un cuadro con todas las funcionalidades que posee esta tarjeta de desarrollo: 
![](https://github.com/Rafa1104/Producto-Unidad/blob/master/img/Componentes%20Microbit.png)

### Raspberry Pi
Raspberry Pi es un computador de bajo coste que llegó con la idea de revolucionar el sector educativo y que, en muy poco tiempo, se ha convertido, junto a Arduino, en un exponente del hardware libre y en la base de un buen número de proyectos.

Raspberry Pi es una placa computadora (SBC) desarrollada en Reino Unido por la Fundación Raspberry Pi, con el objetivo de estimular la enseñanza de ciencias de la computación en las escuelas.

![](https://github.com/Rafa1104/Producto-Unidad/blob/master/img/Componnetes%20Pi.jpg)

Con unas dimensiones de placa de 8.5 por 5.3 cm, en el modelo B de la Raspberry Pi , nos encontramos con unas características muy interesantes. su corazón nos encontramos con un chip integrado Broadcom BCM2835, que contiene un procesador ARM11 con varias frecuencias de funcionamiento y la posibilidad de subirla (overclocking) hasta 1 GHz sin perder la garantía, un procesador gráfico VideoCore IV, y distintas cantidades de memoria RAM.

Las últimas Raspberry Pi cuentan con 512 MB de memoria. Todo ello equivale en la práctica a un ordenador con unas capacidades gráficas similares a la XBOX de Microsoft y con la posibilidad de reproducir vídeo en 1080p.

En la placa de la Raspberry Pi nos encontramos además con una conexión. En cuanto a vídeo se refiere, también cuenta con una salida de vídeo compuesto y una salida de audio a través de un minijack.

La Raspberry Pi posee una conexión ethernet 10/100 y, si bien es cierto que podría echarse en falta una conexión Wi-Fi, gracias a los dos puertos USB incluidos podremos suplir dicha carencia con un adaptador Wi-Fi USB de terceros si lo necesitamos. Los puertos tienen una limitación de corriente, por lo que si queremos conectar discos duros u otro dispositivos tendrémos que pensar en hacerlo a través de un hub USB con alimentación.
Clasificacion de los pines:
![](https://github.com/Rafa1104/Producto-Unidad/blob/master/img/GPIO-Pinout-Diagram-2.png)
![](https://github.com/Rafa1104/Producto-Unidad/blob/master/img/Raspberry%20Pi%20pines.jpg)


## 5. DIAGRAMAS
### ***Arduino UNO***
- **Diagrama Esquemático**
#### ***Boton-LED***
![](https://github.com/Rafa1104/Producto-Unidad/blob/master/img/Boton%20-%20LEDs.png)
#### ***Sensor-LED***
![](https://github.com/Rafa1104/Producto-Unidad/blob/master/img/Sensor%20-%20LEDs.png)
#### ***Maestro-Esclavo***
![](https://github.com/Rafa1104/Producto-Unidad/blob/master/img/maestro-esclavo.jpg)

### ***Mirco:bit***
- **Diagrama Esquemático**
#### *Contador de Pasos*
![](https://github.com/Rafa1104/Producto-Unidad/blob/master/img/diagrama%20micro.png)
#### *Registro*
![](https://github.com/Rafa1104/Producto-Unidad/blob/master/img/diagrama%20micro.png)
#### *Mela's Heart*
![](https://github.com/Rafa1104/Producto-Unidad/blob/master/img/diagrama%20micro%202.png)

### ***Raspberry Pi***
- **Diagrama Esquemático**



## 6. LISTA DE COMPONENTES
| **COMPONENTE** | **DESCRIPCIÓN** |
| :---: | :---: |
| Computadora | Sistema Operativo *Windows 10* |
| Internet | Simluacion de tajetas de desarrollo |
| Arduino UNO | Es una placa electrónica basada en el microcontrolador ATmega328. Cuenta con 14 entradas/salidas digitales, de las cuales 6 se pueden utilizar como salidas PWM (Modulación por ancho de pulsos) y otras 6 son entradas analógicas. Además, incluye un resonador cerámico de 16 MHz, un conector USB, un conector de alimentación, una cabecera ICSP y un botón de reseteado. |
| Raspberry Pi 3 model B | Es una placa computadora de bajo coste desarrollada en el Reino Unido por la Fundación Raspberry pi, con el objetivo de estimular la enseñanza de la informática en las escuelas. |
| LEDs | Un diodo emisor de luz. |
| Pulsador | Es un operador eléctrico que, cuando se oprime, permite el paso de la corriente eléctrica y, cuando se deja de oprimir, lo interrumpe. |
| Fotoresistencia | Es un componente electrónico cuya resistencia se modifica, (normalmente disminuye) con el aumento de intensidad de luz incidente. |
| Cables | es un cable con un conector en cada punta, que se usa normalmente para interconectar entre sí los componentes en una placa de pruebas. |
| ProtoBoard | Es una placa de pruebas en los que se pueden insertar elementos electrónicos y cables con los que se arman circuitos sin la necesidad de soldar ninguno de los componentes. |


## 7. MAPA DE VARIABLES
| **VARIABLE** | **TIPO** | **DESCRIPCIÓN** |
| :---: | :---: | :---: |
| | | |
| | | |
| | | |

## 8.EXPLICACIÓN DEL CODIGO FUENTE
### ***ARDUINO UNO***
- **BOTON-LED**
- **FOTORESISTENCIA-LED**

### ***MICRO:BIT***
- **CONTADOR DE PASOS**
- **RESGISTRO**

### ***RASPBERRY Pi***



## 9. DESCRIPCIÓN DE PREREQUISITOS Y CONFIGURACIÓN
Si queremos trabjar con las tarjetas de desarrollo de forma física, hay que tener en cuenta que la Raspberry Pi necesita una memoria microSD para lo cual nos ayuda a cargar el sistema opertaivo que nos va a servir para poder programar con python en el entorno del raspberry y se necesita conectar a un monitor, teclado y mouse para poder visualizar lo que estamos haciendo.

En el Arduino no necesita un prerequisito o programa secundario, ya que la plcac cuenta con todo lo necesario para ejecutar los progrmas, pero si es necesario otros componentes dependiendo de lo que estemos desarrollando.

Microbit es una placa que en si tiene una variasión de sensores que nos permite el desarrollo para diferentes cosas, como tambien para juegos, mientras que las otras dos placas no nos permiten una interacción total con la placa, microbit nos ayuda a desarrollar juegos para niños, con la utilización de las entradas que nos ofrece esto.

En las plataformas para la simualcion no se necesita un prerequisito solo que tenga una conexión de internet en el caso de tinkercard y en la pagina de microbit. Para el Raspberry se necesita por otra parte instalar un emulador que nos permita ver el codigo y lo que se efectua.

## 10. APORTACIONES
### ***ARDUINO UNO***
- **Maestro-Esclavo**

### ***MICRO:BIT***
- **Melas' Heart**

### ***RASPBERRY Pi***

## 11. CONCLUSIONES
Se ha descrito todos los componentes electrónicos y conectores de las tarjetas de desarrollo: ARDUINO UNO, MICRO BIT, RASPBERRY PI mediante el uso de las siguientes plataformas que son: MICRO BIT, TINKER CAD y CREATED WITHCODE, para entender el lenguaje de programación empleado en la elaboración de aplicaciones de las tarjetas de desarrollo.

Hemos entendido el funcionamiento de cada una de nuestras tarjetas de desarrollo para poder ser empleadas de manera correcta en un circuito lógico.

Se explico el lenguaje de programación empleado para el desarrollo de aplicaciones en las tarjetas de desarrollo para Micro bit, Arduino uno y Raspberry pi.


## 12. RECOMENDACIONES


## 13. CRONOGRAMA

![](https://github.com/Rafa1104/Producto-Unidad/blob/master/img/Cronograma.jpeg)

## 14. BIBLIOGRAFIA
- Arduino, S. A. (2015). Arduino. Arduino LLC.

- Badamasi, Y. A. (2014, September). The working principle of an Arduino. In 2014 11th 
international conference on electronics, computer and computation (ICECCO) (pp. 1-4). IEEE.

- Ball, T., Protzenko, J., Bishop, J., Moskal, M., de Halleux, J., Braun, M., ... & Riley, C. (2016, May). Microsoft touch develop and the BBC micro: bit. In 2016 IEEE/ACM 38th International Conference on Software Engineering Companion (ICSE-C) (pp. 637-640). IEEE.

- Pi, R. (2015). Raspberry pi 3 model b. online].(https://www. raspberrypi. org.


## 15. ANEXOS
### 15.1 Manual de Usuario

