import pygame
from src.emulator.peripherals.memory import *
from src.emulator.peripherals.screen import *


class Chip8:
    def __init__(self):
        self.memory = Memory()
        self.registers = Registers()
        self.screen = Screen(64, 32, 10)
        self.opcode_map = {
            0x00E0: self.clear_screen,
            0x00EE: self.return_subroutine,

        }

    def load_program(self, filename):
        with open(filename, "rb") as file:
            program = file.read()

        for i in range(0, len(program), 2):
            opcode = program[i] << 8 | program[i + 1]
            print(format(opcode, '04x'))

    def execute_machine_lang_at_addr(self, NNN):
        pass

    def return_subroutine(self):
        # Decrementa o ponteiro da pilha
        self.registers.SP -= 1
        # Define o contador de programa para o endereço no topo da pilha
        self.registers.PC = self.memory.stack[self.registers.SP]

    def clear_screen(self):
        self.screen.clear()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.draw()

        pygame.quit()




chip8 = Chip8()
chip8.load_program('FILTER.ch8')

