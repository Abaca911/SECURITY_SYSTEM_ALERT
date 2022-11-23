# SECURITY_SYSTEM_ALERT

The purpose of the technical memo is to demonstrate how to implement a security 
system alert which detects motion and immediately takes a picture and sends it 
to your email address. This can be done using a coupleof components that can be 
easily purchased through Amazon.

## COMPONENTS REQUIRED 

1-Raspberry Pi 4
The Raspberry Pi is essentially used to power the whole system and will be used
to run the Python script that allows the security system to be ON.
2-PIR sensor (HC-SR501)
The PIR is a passive infrared sensor that will be used to detect whenever there
is motion. 
3-PiCam V2.1
The PiCam takes a picture every time motion is detected by the sensor.
4-Breadboard
The breadboard is used to connect the whole system together
5-Jumper wires (6x male to female)
The wires are used to connect both the PIR sensor and the Raspberry Pi to the 
breadboard.


## SET UP

### STEP 1

The first step would be to implement the circuit using all the above components.
You can visualize a picture of the set up here.

### STEP 2

GPIO23 will be used for the PIR sensor. In order to start a few requirements need 
to be set for the project to work properly. We will assume that the Raspberry Pi 
is already running and the camera is enabled in: 
Menu ->Preferences ->Raspberry Pi Configuration->Interface->Enable Camera. 

### STEP 3

In order to send notification when motion is detected, an email account needs to be 
set up. In the tutorial, a gmail account is used and some settings have to be changed. 
First of all, you need to enable IMAP on your gmail account. 

The following steps will guide you: 
*Sign in to your Gmail account by using a browser that is supported (Google Chrome, Firefox, Internet Explorer, or Safari).
*Choose or click the gear icon () on the top right.
*Choose Settings > Forwarding and POP/IMAP.
*Select Enable IMAP, and then choose Save Changes.

The SMTP (Simple MailTransfer Protocol) information of the sender email is also needed. 
Each email server has its own but as in this case, an gmail account is used the following informations will be used: 
GMAIL SMTP Port TLS: 587
GMAIL SMTP server address: smtp.gmail.com

Note: Yahoo and hotmail have different SMTP information. 
Google SMTP information can be seen here.

## AFTER SET UP

When running the code for the first time, an email to the user notifying him that a 
new connection has been established and he would have to enable access for the message
to be sent. For this part, it is recommended to create a different email as the code 
uses a third party to send the email.You can follow the next steps:
Step1: Click on “Check Activity” button
Step2: Click on “Yes, it was me”
Step3: Click on “Learn more”
Step4: Expand on “Less secure app access” is off for you account
Step5: Turn ON “Allow less secure apps”

ALL DONE!!!


