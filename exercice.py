#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math


def average(a: float, b: float, c: float) -> float:
    moyenne = (a+b+c)/3
    return moyenne


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    radian = (angle_degs+angle_mins/60+angle_secs)/3600*2*math.pi/360
    return radian


def to_degrees(angle_rads: float) -> tuple:
    angle = (angle_rads*360)/(2*math.pi)
    degrees, minutes, seconds = math.floor(angle), math.floor(angle/60), math.floor(angle/3600)
    return degrees, minutes, seconds


def to_celsius(temperature: float) -> float:
    celsius = 5*(temperature-32)/9
    return celsius


def to_farenheit(temperature: float) -> float:
    farenheit = (9*temperature/5)+32
    return farenheit


def main() -> None:
    print(f"Moyenne des nombres 2,1; 4,3; 6,5: {average(2.1, 4.3, 6.5)}")

    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")

    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()

