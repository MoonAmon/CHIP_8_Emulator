import time
import random
import sys
from src.emulator.cpu import *
from src.emulator.peripherals.screen import *



def tick_emulator():
    pass


def handle_emulator_error(e):
    pass


def main(romfile, speed):
    emulator = Chip8()
    gui = Screen(64, 32, 10)

    load_program(romfile)
