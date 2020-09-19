import serial
import mouse
import time

# communicate with Arduino Uno serial port
ser = serial.Serial('COM3', 9600, timeout=.1)
print("Give the program 3 seconds before it can start reading!")
time.sleep(3)
sensitivity = 16
duration = 0.05
# loop that reads from serial port
while True:
    #setup
    data = ser.readline()[:-2]  # the last bit gets rid of the new-line chars
    params = data.split()
    #parses string from into words, stores them in their respective variables
    #String format: mouseX, mouseY, mouse1_clicked, mouse2_clicked
    mouseX = (int(params[0].decode('utf-8'))-516) / sensitivity
    mouseY = ((int(params[1].decode('utf-8'))-516) / sensitivity) * -1
    mouse1_clicked = params[2].decode('utf-8')
    mouse2_clicked = params[3].decode('utf-8')
    #if statements time
    if  (mouse.is_pressed('left')):
        mouse.drag(mouseX, mouseY, absolute=False, duration=duration)
    else:
        if (mouse1_clicked == "M1_PRESSED"):
            mouse.click('left')
        if (mouse2_clicked == "M2_PRESSED"):
            mouse.click('right')
        mouse.move(mouseX, mouseY, absolute=False, duration=duration)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/