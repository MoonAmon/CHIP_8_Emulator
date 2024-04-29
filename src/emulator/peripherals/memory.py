
MEMORY_SIZE = 4096


class Memory:
    def __init__(self):
        self.memory = [0] * MEMORY_SIZE
        self.stack = [0] * 16 # Adiciona Pilha

    def push_stack(self, value):
        self.stack.append(value)

    def pop_stack(self):
        return self.stack.pop()


class Registers:
    def __init__(self):
        self.V = [0] * 16  # Registers V0 to VF
        self.I = 0  # Index Registers
        self.DT = 0  # Delay timer
        self.ST = 0  # Sound timer
        self.PC = 0x200  # Program counter, starts at 0x200
        self.SP = 0  # Stack pointer

    def reset(self):
        self.V = [0] * 16
        self.I = 0
        self.DT = 0
        self.ST = 0
        self.PC = 0x200
        self.SP = 0

    def set_register(self, register, value):
        self.V[register] = value

    def get_register(self, register):
        return self.V[register]


memory_test = Memory()

print(memory_test.memory)
