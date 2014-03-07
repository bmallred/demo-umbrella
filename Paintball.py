"""
Simple class for the paintball marker.
"""

class Marker():
    """
    A paintball marker.
    """

    def __init__(self):
        self.ammo = 0
        self.co2 = 1.0

    def fire(self):
        # Check to see if we can even fire.
        if self.ammo == 0 or self.co2 == 0.0:
            return

        self.ammo -= 1
        self.co2 -= 0.01

    def semiBurst(self):
        for round in range(0, 3):
            self.fire()

    def fullBurst(self, seconds):
        for second in range(0, seconds):
            self.fire()

    def loadHopper(self, ammo):
        self.ammo += ammo

    def refillAir(self):
        self.co2 = 1.0
