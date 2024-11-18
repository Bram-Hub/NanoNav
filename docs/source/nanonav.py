
"""
Skeleton file for documentation docstrings
"""

from ble_advertising import advertising_payload
import bluetooth
from machine import Pin, PWM, ADC, freq
import machine
from micropython import const
import rp2

import time



class BLE:
    """
    A helpful wraper around the MicroPython BLE service functions.

    :param ble: The bluetooth object to use for BLE communication (leave as default unless you know why it should be different).
    :type ble: bluetooth.BLE
    :param name: The name of the device to advertise (default: "NANO RP2040").
    :type name: str
    """
    def __init__(self, ble=bluetooth.BLE(), name="NANO RP2040"):
        pass

    def send(self, value):
        """
        Send value to the bluetooth characteristic.

        :param value: The value to send.
        :type value: int, bytes, or str
        :raise ValueError: If the value is not int, bytes, or str.
        """
        pass

    def read(self):
        """
        Return the current value of the bluetooth characteristic, or None if an error occurred.

        :type as_type: str
        :return: The value of the characteristic.
        :rtype: int, None
        """
        pass

    def on_connected(self):
        """
        You may create this method in a subclass of BLE to be called once the BLE connection is established.
        """
        pass

    def on_disconnected(self):
        """
        You may create this method in a subclass of BLE to be called once the BLE connection is lost.
        """
        pass

class NanoBot:
    """
    Interact with Arduino and peripheral hardware for movement and sensing.

    :param saturated_speed: The maximum duty cycle to use for the motors. This is a percentage of max speed the motor can supply from 0-100. If you find that your NanoBot is driving too fast or not driving fast enough, try changing this value.
    """
    def __init__(self, saturated_duty=33, *args, **kwargs):

        # turn ir sensor pin on (inactive because it's active low)
        self.ir_right_sensor = Pin(28, Pin.OUT)
        self.ir_right_sensor.on()

        time.sleep(0.5)

        # ir sensors
        self.ir_left_sensor = ADC(Pin(29, Pin.IN))
        self.ir_right_sensor = ADC(Pin(28, Pin.IN))

        # initialize frequency
        machine.freq(100000000)

        # initialize motors
        m1pin1 = Pin(4)
        m1pin2 = Pin(5)
        m2pin1 = Pin(18)
        m2pin2 = Pin(17)

        self.m1pwm1 = PWM(m1pin1)
        self.m1pwm2 = PWM(m1pin2)
        self.m2pwm1 = PWM(m2pin1)
        self.m2pwm2 = PWM(m2pin2)

        # initialize motor constants
        self.max_duty = 65535 # constant
        self.saturated_duty = saturated_duty * self.max_duty / 100 # choice for max speed
        assert(0 <= self.saturated_duty <= self.max_duty)
        self.turn90ticks = 120
        self.turn_error = 5
        self.block_delay = 1550

        # PID controller constants
        self.battery_scaling = 1.05
        self.kp = 0.8 * self.battery_scaling
        self.ki = 0.08 * self.battery_scaling
        self.kd = 0.04 * self.battery_scaling

        # initialize encoder variables
        self.encpins = (15, 25, 7, 27)
        self.enc1p1 = Pin(self.encpins[0], Pin.IN)
        self.enc1p2 = Pin(self.encpins[1], Pin.IN)
        self.enc2p1 = Pin(self.encpins[2], Pin.IN)
        self.enc2p2 = Pin(self.encpins[3], Pin.IN)

        self.enc1 = 0
        self.enc2 = 0
        self.enc1dir = 1
        self.enc2dir = 1

        # add interrupt callbacks to track encoder ticks
        self.enc1p1.irq(lambda pin: self.enc_pin_high(self.encpins[0]), Pin.IRQ_RISING)
        self.enc1p2.irq(lambda pin: self.enc_pin_high(self.encpins[1]), Pin.IRQ_RISING)
        self.enc2p1.irq(lambda pin: self.enc_pin_high(self.encpins[2]), Pin.IRQ_RISING)
        self.enc2p2.irq(lambda pin: self.enc_pin_high(self.encpins[3]), Pin.IRQ_RISING)

        self.setup()

    def enc_pin_high(self, pin):
        if pin == self.encpins[0] or pin == self.encpins[1]:
            if self.enc1p1.value() == 1 and self.enc1p2.value() == 1:
                self.enc1 += 1 * self.enc1dir
            elif self.enc1p1.value() == 1:
                self.enc1dir = 1
            else:
                self.enc1dir = -1
        if pin == self.encpins[2] or pin == self.encpins[3]:
            if self.enc2p1.value() == 1 and self.enc2p2.value() == 1:
                self.enc2 += 1 * self.enc2dir
            elif self.enc2p1.value() == 1:
                self.enc2dir = -1
            else:
                self.enc2dir = 1

    def calc_duty(self, duty_100):
        return int(duty_100 * self.max_duty / 100)

    def m1_forward(self, speed):
        """
        Set Motor 1 to turn forward at speed.

        :param speed: The speed to turn Motor 1 forward at. This is a percentage of max speed from 0-100.
        :type speed: int or float
        """
        pass

    def m1_backward(self, speed):
        """
        Set Motor 1 to turn backward at speed.

        :param speed: The speed to turn Motor 1 backward at. This is a percentage of max speed from 0-100.
        :type speed: int or float
        """
        pass

    def m2_forward(self, speed):
        """
        Set Motor 2 to turn forward at speed.

        :param speed: The speed to turn Motor 2 forward at. This is a percentage of max speed from 0-100.
        :type speed: int or float
        """
        pass
        
    def m2_backward(self, speed):
        """
        Set Motor 2 to turn backward at speed.

        :param speed: The speed to turn Motor 2 backward at. This is a percentage of max speed from 0-100.
        :type speed: int or float
        """
        pass

    def stop(self):
        """
        Turn off all motors.
        """
        pass

    def ir_left(self):
        """
        Return true if the left IR sensor detects white.

        :rtype: boolean
        """
        pass

    def ir_right(self):
        """
        Return true if the right IR sensor detects white.

        :rtype: boolean
        """
        pass

    def get_enc1(self):
        """
        Return the current encoder 1 count.

        :return: The value of the encoder 1.
        :rtype: int
        """
        
    def get_enc2(self):
        """
        Return the current encoder 2 count.

        :return: The value of the encoder 2.
        :rtype: int
        """

    def set_enc1(self, value):
        """
        Set the current encoder 1 count. This is useful if you want to zero its value.
        
        :param value: The new value to set the encoder 1 count to.
        :type value: int
        """
        
    def set_enc2(self, value):
        """
        Set the current encoder 2 count. This is useful if you want to zero its value.
        
        :param value: The new value to set the encoder 2 count to.
        :type value: int
        """
