kp = 50
kd = 10
ki = 0
preverror = 0
P = 0
I = 0
D = 0
robot_onoff = False
timer_period[0] = 3000
@onevent
def button_forward():  # if button forward is pressed, start the robot
    global robot_onoff
    robot_onoff = True
@onevent
def button_backward(): # if button forward is pressed, start the robot
    global robot_onoff 
    robot_onoff = False
@onevent
def timer0(): # this runs every 3 second
    global x 
    x = math_rand() // 7000 # generates random x value between -4 and 4
def led_lights():  # this functions sets the led value to a random color
    global x, leds_top
    if x == 1:
        leds_top = WHITE
    elif x == 2:
        leds_top = RED
    elif x == 3:
        leds_top = GREEN
    elif x == 4:
        leds_top = BLUE
    elif x == -1:
        leds_top = CYAN
    elif x == -2:
        leds_top = MAGENTA
    elif x == -3:
        leds_top = YELLOW
    elif x == -4:
        leds_top = BLACK
    elif x == 0:
        leds_top = GREEN
        
def robot_stop(): # stops the robot
    global motor_left_target, motor_right_target 
    motor_left_target = 0
    motor_right_target = 0

@onevent
def motor(): # this a pre-defined fucntion that runs at set frequecny
    global motor_left_target, motor_right_target, robot_onoff
    if robot_onoff == True:
        if prox_horizontal[0] > 100 or prox_horizontal[4] > 100: #detects obstacles on left and right
            led_lights() # calls led_lights
        if prox_horizontal[2] > 400: # detects object infront of robot and stops it
            robot_stop() 
            nf_sound_system(0)
        else:
            if prox_ground_delta[0] > 550 and prox_ground_delta[1] > 550: # if both detects white rotate the robot
                motor_left_target = 200
                motor_right_target = -200
            else:
                PID()
    else:
        motor_left_target = 0
        motor_right_target = 0
        
def PID():
    global threshold, motor_left_target, motor_right_target, kp, kd, ki, preverror, P, I, D, error, PIDValue
    
    error = prox_ground_delta[0] - prox_ground_delta[1]  # if error is positive line is on right
    P = error
    I = I + error
    D = error - preverror
    
    PIDValue = (P * kp) // 100 + (I * ki) // 100 + (D * kd) // 100 # this is the stearing value of the robot
    preverror = error
    

    motor_left_target = 370 + PIDValue #setting the value of left motor
    motor_right_target = 370 - PIDValue #setting the value of right motor
    
    # if motor vlaues exceeds 500 or -500 it sets it back to the limit
    if motor_left_target > 500: motor_left_target = 500
    if motor_left_target < -500: motor_left_target = -500
    if motor_right_target > 500: motor_right_target = 500
    if motor_right_target < -500: motor_right_target = -500
    

