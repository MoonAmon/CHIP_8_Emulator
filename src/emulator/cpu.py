from peripherals.memory import *

class Chip8:
    def __init__(self, memory, registers):
        self.memory = memory
        self.registers = registers
        self.opcode_map = {
            0x0NNN: self.execute_machine_lang_at_addr,
            0x00E0: self.clear_screnn,
            0x00EE: self.return_subroutine,

        }

    def execute_machine_lang_at_addr(self, NNN):
        pass


    def clear_screen(self):
        pass