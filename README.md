# SmartFeeder

SmartFeeder nace como un proyecto de EMBS de la universidad nacional de Colombia para censar la población de aves presentes en el campus, este proyecto forma parte de DifEMB, la dependencia encargada de la divulgación, la investigación y la formación de nuestros voluntarios dentro del capítulo, por lo que empleamos herramientas sencillas, y baratas para que sean de fácil acceso; tales como un ESP32-CAM, al cual le instamos micropython para transmitir las imágenes que capture, y luego podamos procesar en un servidor, mediante IA, empleando como dataset para el entrenamiento de esta, el dataset de la app Merlin.

----
## 1. Pruebas con la ESP32-CAM

Tras intalar el firmware obtenido del usuario [lemariva](https://github.com/lemariva/micropython-camera-driver), usamos el siguiente código de pureba obtenido de [profe Tolocka](https://www.profetolocka.com.ar/2022/04/25/aprende-a-programar-la-esp32-cam-en-micropython-parte-2/)
```python
import camera
from time import sleep
import machine
#Pin del led de flash
led = machine.Pin(4, machine.Pin.OUT)
foto=1
while (True):
    nombre = "Cap"+str(foto)+".jpg"
    print (nombre)
    
    try:
        camera.init(0, format=camera.JPEG, fb_location=camera.PSRAM)
        
        #Establece el brillo
        camera.brightness(-1)
        
        #Orientacion normal
        camera.flip(0)
        #Orientación normal
        camera.mirror (0)
        
        #Resolución
        camera.framesize(camera.FRAME_XGA)
        #contraste
        camera.contrast(2)
        
        #saturacion
        camera.saturation (-2)
               
        #calidad
        camera.quality(10)
        
        # special effects
        camera.speffect(camera.EFFECT_NONE)
         
        # white balance
        camera.whitebalance(camera.WB_NONE)
        
        #Enciende flash
        #led.value(1)
        sleep (0.5)
        
        #Captura la imagen
        img = camera.capture()
        print ("Tamaño=",len(img))
        
        
        #Apaga flash
        led.value(0)
        
        #desactivar cámara
        camera.deinit ()
       
        #Guardar la imagen en el sistema de archivos
        imgFile = open(nombre, "wb")
        imgFile.write(img)
        imgFile.close()
        
        foto+=1
        
        sleep (1)
        
    except Exception as err:
    
        print ("Error= "+str (err))
        sleep (2)

#referencia: https://www.profetolocka.com.ar/2022/04/25/aprende-a-programar-la-esp32-cam-en-micropython-parte-2/
```
### imágenes de prueba

A continuación se muestra una imagen de prueba obtenida gracias al código mostrado anteriormente:
<image src="Cap4.jpg" alt="imagen de prueba">