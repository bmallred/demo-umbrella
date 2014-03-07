"""
Simple test of the paintball marker.
"""

import unittest
from Paintball import Marker

class TestPaintball(unittest.TestCase):
    def setUp(self):
        self.marker = Marker()

    def test_fire(self):
        self.marker.loadHopper(1)
        self.marker.fire()
        self.assertEqual(0, self.marker.ammo)

    def test_semiBurst(self):
        self.marker.loadHopper(3)
        self.marker.semiBurst()
        self.assertEqual(0, self.marker.ammo)

    def test_fullBurst(self):
        self.marker.loadHopper(5)
        self.marker.fullBurst(4)
        self.assertEqual(1, self.marker.ammo)

        self.marker.fullBurst(10)
        self.assertEqual(0, self.marker.ammo)

    def test_refillAir(self):
        self.marker.refillAir()
        self.assertEqual(1.0, self.marker.co2)

if __name__ == "__main__": #pragma: no cover
    unittest.main()
