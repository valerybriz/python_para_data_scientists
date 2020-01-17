import datetime
import time
import logging
 
logging.basicConfig(
            level=logging.DEBUG,
            filename='miscript.log',
            filemode='w'
        )

def main_action():
    while True: # para que se ejecute indeterminadamente
        with open('echo.txt', 'a') as fh: #vamos a abrir un archivo y escribir en el 
            fh.write("{}\n".format(datetime.datetime.now())) #lo que escribiremos es la hora actual
        logging.info("time stored")
        time.sleep(60) # vamos a pausar el script por 20 segundos y luego se ejecutará de nuevo
 
main_action()