import unittest
from src.emulator.cpu import Chip8
from src.emulator.peripherals.memory import Memory
from src.emulator.peripherals.screen import Screen
from src.emulator.peripherals.memory import Registers


class TestChip8(unittest.TestCase):
    def setUp(self):
        self.memory = Memory()
        self.register = Registers()
        self.screen = Screen(64, 32, 10)
        self.chip8 = Chip8(self.memory, self.register, self.screen)

    def test_clear_screen(self):
        # Set some pixels on the screen
        for x in range(64):
            for y in range(32):
                self.screen.set_pixel(x, y, 1)

        # Execute the clear screen instruction
        self.chip8.clear_screen()

        # Check that all pixels are off
        for x in range(64):
            for y in range(32):
                self.assertEqual(self.screen.get_pixel(x, y), 0)


if __name__ == '__main__':
    unittest.main()