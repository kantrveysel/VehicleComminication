When the start program is run, over TCP 127.0.0.1:50007 the following
Incoming Hex data
It contains content from 3 different sensors and is assigned an id number in the form of multiplication of sensor codes.
It is parsed with the code 1111011101.

ID 1111011101 First Sensor 1111011101 Second Sensor 1111011101 Third Sensor

It has a shaped structure.

ID -> It is the multiplication of the codes of the sensors in the content of the message.
For example: The id of a message containing the data of Brake (2) Speed (3) Acceleration (11) would be from 2x3x11 to 66.

The distribution of the data is from small code to large code.

Goal:
Sharing this incoming message and reading all messages continuously to ensure that the data of all sensors
It is updated and presented.

--- SENSOR CODES ---
2: Brake
3: Speed
5: Battery
7: Gas
11: Acceleration


##Developed For YTU Racing Support Team##
