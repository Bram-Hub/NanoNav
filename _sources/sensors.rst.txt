.. _Sensors:

Sensors
=======
Using the IR sensors on NanoNav.

Introduction
------------
To best interact with its environment, your NanoNav kit comes with infrared sensors that can be used for detecting how reflective the surface under it is.

Quick Example
-------------

.. code-block:: python

    from nanonav import NanoBot
    import time

    # Create a NanoBot object
    robot = NanoBot()

    while True:
        # Repeatedly print the IR sensor values
        print(f'left: {robot.ir_left()}    right: {robot.ir_right()}')
        time.sleep(0.5)

Note that this code snippet uses `print` which means it will only
work while connected to a computer.

Calibration
-----------
Initially, and if you ever notice the IR sensors not detecting the white line correctly,
you may need to calibrate the sensors. The below video (for a very similar IR sensor model)
shows how to do this.

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/fHBPYWRgEH8?si=n_tW8sT_w2ZMGEE9" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Usage
-----

.. automethod:: nanonav.NanoBot.ir_left
.. automethod:: nanonav.NanoBot.ir_right
