"""
Given a time in the format of hour and minute, calculate the angle of the hour and minute hand on a clock.
"""


def calcAngle(h, m):
    return abs(0.5 * ((60 * h) % 720 + m) - 6 * m)


if __name__ == "__main__":
    print(calcAngle(3, 30))
    # 75
    print(calcAngle(12, 30))
    # 165
