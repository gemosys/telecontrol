#
# Telecontrol by Gemo
#

import picamera
import time
import schedule


def main():
    schedule.every().day.at("08:00").do(job)
    schedule.every().day.at("10:00").do(job)

def takepic():
    try:
        print ('Tomando imagen...')
        with picamera.PiCamera() as camara:
            camara.resolution = (640, 480)
            time.sleep(3)
            camara.annotate_text = datetime.datetime.now().strftime('%d-%m-%Y %H:%M')
            camara.capture('foto.jpg')
            camara.close()
        print ('Fin foto')
        return True
    except:
        return False

if __name__ == "__main__":
    main()
