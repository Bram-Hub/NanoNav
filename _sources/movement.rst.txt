.. _Movement:

Movement
=========
Working with NanoNav's motors.

Introduction
------------

To complete the Wumpus challenge, NanoBot will have to navigate the board by moving and turning. It does this by sending power to the motors, which then turn the wheels. Speed of the motors is controlled by the amount of power you send. However, because most microcontrollers can only send LOW or HIGH voltage (0V or 3.3V in the Arduino's case), power is controlled by a process called Pulse Width Modulation (PWM), which is explained in more detail `here <https://learn.sparkfun.com/tutorials/pulse-width-modulation/all>`_ if you're interested.

Sensors called encoders are used to track the rotation of the motors accurately. Encoders track rotation in ticks. You can read more `here <https://howtomechatronics.com/tutorials/arduino/rotary-encoder-works-use-arduino/>`_ if you're interested, but all you have to know is that a positive change in ticks corresponds to a forward rotation of the motor, and a negative change to a backward rotation of the motor.

You don't have to use encoders in your solution, though they do provide greater accuracy.


Quick Example
-------------

.. code-block:: python

    from nanonav import NanoBot
    import time

    # Create a NanoBot object
    robot = NanoBot()

    # Move forward for 2 seconds
    robot.m1_forward(30)
    robot.m2_forward(30)
    time.sleep(2)

    # Stop
    robot.stop()
    time.sleep(2)

    # Move backward for 2 seconds
    robot.m1_backward(30)
    robot.m2_backward(30)
    time.sleep(2)

    # Stop
    robot.stop()
    
Usage
-----

.. autoclass:: nanonav.NanoBot
    :members:
    :exclude-members: ir_left, ir_right

