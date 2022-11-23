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

Menu ->Preferences ->Raspberry Pi Configuration->Interface->Enable Camera. 


