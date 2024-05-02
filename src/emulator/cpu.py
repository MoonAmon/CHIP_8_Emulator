import pygame
from src.emulator.peripherals.memory import *
from src.emulator.peripherals.screen import *
from src.emulator.peripherals.keyboard import *


class Chip8:
    def __init__(self):
        self.memory = Memory()
        self.registers = Registers()
        self.screen = Screen(64, 32, 10)
        self.keyboard = Keyboard()
        self.opcode_map = {
            0x00E0: self.clear_screen,
            0x00EE: self.return_subroutine,
            0x1000: self.jump_to_addr,
            0x2000: self.call_subroutine,
            0xB000: self.jump_to_V0_plus_addr,
            0x3000: self.skip_if_equal,
            0x4000: self.skip_if_not_equal,
            0x5000: self.skip_if_vx_equal_vy,
            0x9000: self.skip_if_vx_not_equal_vy,
            0x6000: self.load_byte_into_vx,
            0x7000: self.add_byte_into_vx,
            0x8000: self.load_vy_into_vx,
            0x8001: self.or_vx_vy,
            0x8002: self.and_vx_vy,
            0x8003: self.xor_vx_vy,
            0x8004: self.add_vx_vy,
            0x8005: self.sub_vx_vy,
            0x8006: self.shr_vx,
            0x8007: self.subn_vx_vy,
            0x800E: self.shl_vx,
            0XA000: self.load_i_addr,
            0xF055: self.load_i_vx,
            0xF065: self.load_vx_i
        }

    def execute_machine_lang_at_addr(self, NNN):
        pass

    def load_program(self, filename):
        with open(filename, "rb") as file:
            program = file.read()

        for i in range(0, len(program), 2):
            self.memory.memory[i + 0x200] = program[i]

    def load_vx_i(self, opcode):
        register_index_x = (opcode & 0x0F00) >> 8
        for i in range(register_index_x + 1):
            self.registers.V[i] = self.memory[self.registers.I + i]
        # Atualiza o registrador I para o endereço do próximo local de memória livre
        self.registers.I += register_index_x + 1

    def load_i_vx(self, opcode):
        register_index_x = (opcode & 0x0F00) >> 8
        for i in range(register_index_x + 1):
            self.memory[self.registers.I + i] = self.registers.V[i]
        # Atualiza o register I para o endereço do próximo local de memória livre
        self.registers.I += register_index_x + 1

    def load_i_addr(self, opcode):
        address = opcode & 0x0FFF
        self.registers.I = address

    def shl_vx(self, opcode):
        register_index_x = (opcode & 0x0F00) >> 8
        # Define VF para o bit mais significativo de Vx
        self.registers.V[0xF] = (self.registers.V[register_index_x] & 0x80) >> 7
        # Desloca Vx um bit para a esquerda
        self.registers.V[register_index_x] <<= 1
        # Garante que o resultado permaneça dentro de 8 bits
        self.registers.V[register_index_x] &= 0xFF

    def shr_vx(self, opcode):
        register_index_x = (opcode & 0x0F00) >> 8
        # Define VF para o bit menos significativo de Vx
        self.registers.V[0xF] = self.registers.V[register_index_x] & 0x1
        # Desloca Vx um bit para a direita
        self.registers.V[register_index_x] >>= 1

    def sub_vx_vy(self, opcode):
        register_index_x = (opcode & 0x0f00) >> 8
        register_index_y = (opcode & 0x00f0) >> 4
        self.registers.V[0xF] = 1 if self.registers.V[register_index_x] >= self.registers.V[register_index_y] else 0  # Set VF = NOT borrow
        self.registers.V[register_index_x] -= self.registers.V[register_index_y]
        self.registers.V[register_index_x] &= 0xFF

    def subn_vx_vy(self, opcode):
        register_index_x = (opcode & 0x0f00) >> 8
        register_index_y = (opcode & 0x00f0) >> 4
        self.registers.V[0xF] = 1 if self.registers.V[register_index_y] >= self.registers.V[register_index_x] else 0  # Set VF = NOT borrow
        self.registers.V[register_index_x] = self.registers.V[register_index_y] - self.registers.V[register_index_x]
        self.registers.V[register_index_x] &= 0xFF

    def add_vx_vy(self, opcode):
        register_index_x = (opcode & 0x0f00) >> 8
        register_index_y = (opcode & 0x00f0) >> 4
        result = self.registers.v[register_index_x] + self.registers.v[register_index_y]
        self.registers.V[0xF] = 1 if result > 0xFF else 0  # Set VF = carry
        self.registers.V[register_index_x] = result & 0xFF  # Mantém abaixo de 8 bits

    def xor_vx_vy(self, opcode):
        register_index_x = (opcode & 0x0F00) >> 8
        register_index_y = (opcode & 0x00F0) >> 4
        self.registers.V[register_index_x] ^= self.registers.V[register_index_y]

    def and_vx_vy(self, opcode):
        register_index_x = (opcode & 0x0F00) >> 8
        register_index_y = (opcode & 0x00F0) >> 4
        self.registers.V[register_index_x] &= self.registers.V[register_index_y]

    def or_vx_vy(self, opcode):
        register_index_x = (opcode & 0x0F00) >> 8
        register_index_y = (opcode & 0x00F0) >> 4
        self.registers.V[register_index_x] |= self.registers.V[register_index_y]

    def load_vy_into_vx(self, opcode):
        register_index_x = (opcode & 0x0F00) >> 8
        register_index_y = (opcode & 0x00F0) >> 4
        self.registers.V[register_index_x] = self.registers.V[register_index_y]

    def add_byte_into_vx(self, opcode):
        register_index = (opcode & 0x0F00) >> 8
        byte = opcode & 0x00FF
        self.registers.V[register_index] += byte

    def load_byte_into_vx(self, opcode):
        register_index = (opcode & 0x0F00) >> 8
        byte = opcode & 0x00FF
        self.registers.V[register_index] = byte

    def skip_if_vx_not_equal_vy(self, opcode):
        register_index_x = (opcode & 0x0F00) >> 8
        register_index_y = (opcode & 0x00F0) >> 4
        if self.registers.V[register_index_x] != self.registers.V[register_index_y]:
            self.registers.PC += 2

    def skip_if_vx_equal_vy(self, opcode):
        register_index_x = (opcode & 0x0F00) >> 8
        register_index_y = (opcode & 0x00F0) >> 4
        if self.registers.V[register_index_x] == self.registers.V[register_index_y]:
            self.registers.PC += 2

    def skip_if_not_equal(self, opcode):
        register_index = (opcode & 0x0F00) >> 8
        byte = opcode & 0x00FF
        if self.registers.V[register_index] != byte:
            self.registers.PC += 2

    def skip_if_equal(self, opcode):
        register_index = (opcode & 0x0F00) >> 8
        byte = opcode & 0x00FF
        if self.registers.V[register_index] == byte:
            self.registers.PC += 2

    def jump_to_v0_plus_addr(self, opcode):
        address = opcode & 0x0FFF
        self.registers.PC = self.registers.V[0] + address

    def call_subroutine(self, opcode):
        # Empilha o endereço atual do PC na pilha
        self.memory.stack[self.registers.SP] = self.registers.PC
        # Incrementa o ponteiro da pilha
        self.registers.SP += 1
        # Define o PC para o endereço nnn
        self.registers.PC = opcode & 0x0FFF

    def jump_to_addr(self, opcode):
        address = opcode & 0x0FFF
        self.registers.PC = address

    def execute_opcode(self, opcode):
        instruction = opcode & 0xF000
        if instruction in self.opcode_map:
            self.opcode_map[instruction](opcode)
        else:
            print(f"Unknown opcode: {opcode}")

        # Implementar logica

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

