#All required libraries
from email.mime.multipart import MIMEMultipart
from subprocess import call 
import email.mime.application
from picamera import PiCamera
import RPi.GPIO as GPIO
from time import sleep
import datetime
import smtplib
import random 
import time
import os

#setting up the Pir sensor on GPIO23 and the creating an instance of camera
PIR    = 23
GPIO.setwarnings(False)  
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR, GPIO.IN)
camera = PiCamera()

#Creating the credentials for the sender and the receiver
from_email_addr = 'sender_email@gmail.com'
from_email_password = 'password'
to_email_addr = 'receiver_email@gmail.com'

def check():
    try:
        while True:
            # Wait for 1 second
            time.sleep(1)
            # If motion is detected by the PIR sensor the function the camera start  streaming for 5
            # seconds and a picture is taken and saed in the appropriate folder.
            if GPIO.input(PIR) == 1:
                #Print "Motion detected" on the console
                print("Motion detected")
                camera.start_preview()
                sleep(5)
                camera.capture('Pick your own directory')
                camera.stop_preview()
                 
                #Create the Message to be sent with the subject specified
                msg = MIMEMultipart()
                msg[ 'Subject'] = 'PERSON DETECTED!!!'
                msg['From'] = from_email_addr
                msg['To'] = to_email_addr
                
                # Picture attachment
                # Retrieve the picture taken and make it an attachment to the sender email.
                Captured = 'Pick your own directory'
                fp=open(Captured,'rb')
                att = email.mime.application.MIMEApplication(fp.read(),_subtype=".jpg")
                fp.close()
                att.add_header('Content-Disposition','attachment',filename='image' + datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S') + '.jpg')
                msg.attach(att)
                # Print "attach successful" to the console
                print("attach successful")

                #send Mail to the receiver 
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(from_email_addr, from_email_password)
                server.sendmail(from_email_addr, to_email_addr, msg.as_string())
                server.quit()
                # Print "Email sent" to the console
                print('Email sent')
            
            else:
                # Print "No motion detected" to console when motion is not detected every 5 seconds
                print("No motion detected")
                sleep(5)
            # Wait 3 seconds to check for motion
            time.sleep(3)
              
    except KeyboardInterrupt:
        GPIO.cleanup()


def main():
    check()
if __name__ == "__main__": 
    main()
