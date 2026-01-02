LINE-FOLLOWING & OBSTACLE-AVOIDING ROBOT (PID CONTROLLED)
========================================================

This project implements a PID-controlled line-following robot with obstacle
detection, LED feedback, and manual start/stop control using buttons.
The program follows an event-based architecture suitable for embedded
robotics platforms.

--------------------------------------------------------
FEATURES
--------------------------------------------------------
- PID-based line following
- Front obstacle detection with emergency stop
- Side obstacle detection with LED feedback
- Random LED color generation using a timer
- Button-controlled robot start and stop
- White surface detection with recovery rotation
- Motor speed limiting for safety

--------------------------------------------------------
CONTROL OVERVIEW
--------------------------------------------------------

1. START / STOP CONTROL
- Forward Button  → Starts the robot
- Backward Button → Stops the robot

2. LINE FOLLOWING (PID CONTROL)
The robot follows a line using two ground sensors.

Error calculation:
error = left_ground_sensor - right_ground_sensor

PID control equation:
PIDValue = (P * kp + I * ki + D * kd) / 100

Motor control:
Left motor  = base_speed + PIDValue
Right motor = base_speed - PIDValue

Motor values are limited between -500 and 500.

3. OBSTACLE DETECTION
- Front proximity sensor (> 400):
  → Robot stops and plays a sound
- Left or right proximity sensor (> 100):
  → LEDs change color

4. WHITE SURFACE DETECTION
If both ground sensors detect white, the robot rotates in place
to recover the line.

--------------------------------------------------------
LED FEEDBACK SYSTEM
--------------------------------------------------------
A timer generates a random value every 3 seconds and maps it
to an LED color.

Random Value → LED Color
1  → White
2  → Red
3  → Green
4  → Blue
-1 → Cyan
-2 → Magenta
-3 → Yellow
-4 → Black
0  → Green

--------------------------------------------------------
PID PARAMETERS
--------------------------------------------------------
kp = 50
kd = 10
ki = 0

--------------------------------------------------------
HARDWARE REQUIREMENTS
--------------------------------------------------------
- Differential drive robot
- 2 ground sensors
- 5 horizontal proximity sensors
- Motor drivers with speed control
- RGB LEDs
- Sound module
- Forward and backward buttons

--------------------------------------------------------
AUTHOR
--------------------------------------------------------
Sanchit Acharya
Robotics & AI Engineer
University of Hertfordshire
RobotCup STRIDE Team

--------------------------------------------------------
LICENSE
--------------------------------------------------------
MIT License
