FAQ
===

No questions yet.

Troubleshooting
===============

Why are the wheels of my robot spinning at full speed after I stop my program?
-------------------------------------------------------------------------------

This behavior is expected because of `how Pulse Width Modulation (PWM) works <https://learn.sparkfun.com/tutorials/pulse-width-modulation/all>`_. If you stop your program with your motors on at any speed, there is a chance that the program will terminate with your motor spinning HIGH. The Arduino will continue its last instruction, making the motor spin at full speed until the next time you run code. To avoid this, call ``robot.stop()`` before the program ends, or flip the "Driver Enable" switch off to disable the motor hardware (remember to turn it back on when you want to spin the motors again!).


Arduino not connecting to OpenMV
--------------------------------

If your Arduino is not connecting to OpenMV, either because OpenMV is loading forever, or because the cursor is flickering between loading and a pointer, you should reset your board. Do this by double tapping the button on top of the Arduino. This will reset the board.

.. image:: images/rp2040_white_button.jpeg
   :height: 80
   :alt: RP2040 white button

Wait for OpenMV to update. When OpenMV updates, it should offer to load the latest firmware. Agree and load the firmware, and hopefully the Arduino will connect.

If this doesn't work, it's probably because your code has a frequently repeating while loop which keeps the Arduino occupied. Keep trying to reset the board by double pressing the top button, or open Finder or FileExplorer, open the board's external drive, and replace its main.py (your code) with a basic main.py such as :download:`blink_LED.py <../../tests/installation_check/blink_LED.py>`. This should enable the Arduino to connect.

If you still cannot get the Arduino to connect, it could be a problem on your computer. Try changing the port you're using to connect to the Arduino.

IR sensor has both LEDs lit regardless of sensor state
------------------------------------------------------

We've noticed a problem with some of the boards where the right IR sensor has both LEDs on, regardless of whether the sensor is in front of a white or black surface:

.. image:: images/ir_2_lights_on.jpeg
    :height: 80
    :alt: IR sensor with 2 lights on
    
If you're noticing this, add

.. code-block:: python

    from machine import Pin

to your import statements and add the line 

.. code-block:: python

    Pin(28, Pin.OUT).on()

after your imports and before ``robot = NanoBot()``.

Strange problems with code which was just working
-------------------------------------------------

When you run in laptop mode from OpenMV, sometimes the code gives you errors the first 2 times you try to run. We're not sure why this happens, but these errors always go away after the third attempt.

If when running in solo mode, the Arduino behaves strangely when running code which you know works, it could be because you are out of storage. This will not happen until your code files are at least 30 KB in total!!! If your code files are not 30 KB or larger in total, what you're experiencing is an ordinary bug. If you suspect that you make be out of storage, try to shrink your code by removing comments and making functions more efficient. Every character counts, because it's the storage of your .py files which is running out. Try removing excess newlines or whitespace.

Issues
------

Found a bug? Create an issue on GitHub. Submit `here <https://github.com/Bram-Hub/NanoNav/issues>`_ with as much information as you can provide
about the context of the bug.
