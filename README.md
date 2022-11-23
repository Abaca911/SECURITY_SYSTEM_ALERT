# SECURITY_SYSTEM_ALERT

The purpose of the technical memo is to demonstrate how to implement a security 
system alert which detects motion and immediately takes a picture and sends it 
to your email address. This can be done using a couple of components that can be 
easily purchased through Amazon.

## COMPONENTS REQUIRED 

1-Raspberry Pi 4

2-PIR sensor (HC-SR501)

3-PiCam V2.1

4-Breadboard

5-Jumper wires (6x male to female)

## SET UP

### STEP 1

The first step would be to implement the circuit using all the above components.
You can visualize a picture of the set up [here](https://github.com/Abaca911/SECURITY_SYSTEM_ALERT/blob/734fced8802ac8687e5ac98bef797a579d7ec332/Figures/Fritzing_Circuit_SetUp.png).

### STEP 2

GPIO23 will be used for the PIR sensor. In order to start a few requirements need 
to be set for the project to work properly. We will assume that the Raspberry Pi 
is already running and the camera is enabled in: 

```
Menu ->Preferences ->Raspberry Pi Configuration->Interface->Enable Camera. 
```

### STEP 3

In order to send notification when motion is detected, an email account needs to be set up.
First of all, you need to enable IMAP on your account. 

1- Sign in to your account by using a browser that is supported (Google Chrome, Firefox, Internet Explorer, or Safari).

2- Choose or click the gear icon () on the top right.

3- Choose Settings > Forwarding and POP/IMAP.

4- Select Enable IMAP, and then choose Save Changes.

The SMTP (Simple MailTransfer Protocol) information of the sender email is also needed. Each email server has its own but 
as in this case, an gmail account is used the following informations will be used: 

- GMAIL SMTP Port TLS: 587
- GMAIL SMTP server address: smtp.gmail.com

Note: Yahoo and hotmail have different SMTP information. 

A screenshot of GMAIL SMTP information can be seen [here](https://github.com/Abaca911/SECURITY_SYSTEM_ALERT/blob/dc3aacd351ff6e41164abbc231cd29117b13e2fb/Figures/Gmail_SMTP_information.png).

## AFTER SET UP

When running the code for the first time, an email to the user notifying him 
that a new connection has been established and he would have to enable access 
for the message to be sent. For this part, it is recommended to create a different 
email as the code uses a third party to send the email.

1. Click on “Check Activity” button
2. Click on “Yes, it was me”
3. Click on “Learn more”
4. Expand on “Less secure app access” is off for you account
5. Turn ON “Allow less secure apps”
