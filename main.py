import camera
from time import sleep
import machine
import network
import socket
import usocket
#Pin del led de flash
led = machine.Pin(4, machine.Pin.OUT)
foto=1
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
a.listen(3)

def web_page():

  html =  """
    <body> 
        <img src="Cap1.jpg" />
    </body>
    """
  return html
while True:
    conn,addr = a.accept()
    print('Nueva conexion desde:  %s' % str(addr))
    request = conn.recv(1024)
    print('Solicitud = %s' % str(request))
    request = str(request)    
    if request.find('/capture'):
        nombre = "Cap"+str(foto)+".jpg"
        print (nombre)
        
        try:
            camera.init(0, format=camera.JPEG, fb_location=camera.PSRAM)
            
            #Establece el brillo
            camera.brightness(2)
            
            #Orientacion normal
            camera.flip(0)
            #Orientación normal
            camera.mirror (0)
            
            #Resolución
            camera.framesize(camera.FRAME_SXGA)
            #contraste
            camera.contrast(-2)
            
            #saturacion
            camera.saturation (2)
                   
            #calidad
            camera.quality(20)
            
            # special effects
            camera.speffect(camera.EFFECT_BW)
             
            # white balance
            camera.whitebalance(camera.WB_NONE)
            
            #Enciende flash
            led.value(1)
            
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
            
            sleep (1/48)
        except Exception as err:
        
            print ("Error= "+str (err))
            sleep (1/24)
    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()
