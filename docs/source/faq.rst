FAQ
===

No questions yet.

Troubleshooting
===============

Arduino not connecting to OpenMV
--------------------------------

If your Arduino is not connecting to OpenMV, either because OpenMV is loading forever, or because the cursor is flickering between loading and a pointer, you should reset your board. Do this by double tapping the button on top of the Arduino. This will reset the board.

.. image:: images/rp2040_white_button.jpeg
   :height: 80
   :alt: RP2040 white button

Wait for OpenMV to update. When OpenMV updates, it should offer to load the latest firmware. Agree and load the firmware, and hopefully the Arduino will connect.

If this doesn't work, it's probably because your code has a frequently repeating while loop which keeps the Arduino occupied. Keep trying to reset the board by double pressing the top button, or open Finder or FileExplorer, open the board's external drive, and replace its main.py (your code) with a basic main.py such as :download:`blink_LED.py <../../tests/installation_check/blink_LED.py>`. This should enable the Arduino to connect.

If you still cannot get the Arduino to connect, it could be a problem on your computer. Try changing the port you're using to connect to the Arduino.

Strange problems with code which was just working
-------------------------------------------------

When you run in laptop mode from OpenMV, sometimes the code gives you errors the first 2 times you try to run. We're not sure why this happens, but these errors always go away after the third attempt.

If when running in solo mode, the Arduino behaves strangely when running code which you know works, it could be because you are out of storage. This will not happen until your code files are at least 30 KB in total!!! If your code files are not 30 KB or larger in total, what you're experiencing is an ordinary bug. If you suspect that you make be out of storage, try to shrink your code by removing comments and making functions more efficient. Every character counts, because it's the storage of your .py files which is running out. Try removing excess newlines or whitespace.

Issues
------

Found a bug? Create an issue on GitHub. Submit `here <https://github.com/Bram-Hub/NanoNav/issues>`_ with as much information as you can provide
about the context of the bug.
