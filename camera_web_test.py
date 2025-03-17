import camera
from time import sleep
import machine
import network
import socket
import usocket
"""
ssid = 'Bidipi'
password = 'michi111'
wlan = network.WLAN(network.STA_IF)

wlan.active(True)
wlan.connect(ssid, password)

while wlan.isconnected() == False:
    pass

print('Conexion con el WiFi %s establecida' % ssid)
print(wlan.ifconfig())

a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
a.bind(('', 80))
a.listen(3)"""
#Pin del led de flash
led = machine.Pin(4, machine.Pin.OUT)
foto=1
def web_page():

  html =  """
    <body> 
        <img src="Cap1.jpg" />
    </body>
    """
  return html

while (True):
    nombre = "Cap"+str(foto)+".jpg"
    print (nombre)
    
    try:
        camera.init(0, format=camera.JPEG, fb_location=camera.PSRAM)
        
        #Establece el brillo
        camera.brightness(0)
        
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
        led.value(1)
        sleep (0.5)
        
        #Captura la imagen
        img = camera.capture() ####
        print ("Tamaño=",len(img))
        
        
        #Apaga flash
        led.value(0)
        
        #desactivar cámara
        camera.deinit ()
       
        #Guardar la imagen en el sistema de archivos
        imgFile = open(nombre, "wb")
        imgFile.write(img)
        imgFile.close()
        
        #sumar fotos
        #foto+=1
        
        sleep (2)
        #borrar la imagen
    except Exception as err:
    
        print ("Error= "+str (err))
        sleep (2)
