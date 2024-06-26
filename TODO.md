# Todo List para Implementação do Chip-8

## 1. Setup Inicial

- [X]  Criar estrutura de projeto
- [X]  Configurar ambiente de desenvolvimento
- [X]  Definir estrutura de dados para o estado do Chip-8 (memória, registradores, stack, etc.)

## 2. Implementação do Loop Principal

- [ ]  Desenvolver loop principal de execução
- [ ]  Implementar sistema de temporizadores (delay e sound timers)

## 3. Implementação de Opcodes

### 3.1 Instruções de Controle de Fluxo

- [X]  00E0 - CLS (Clear the display)
- [X]  00EE - RET (Return from a subroutine)
- [X]  1nnn - JP addr (Jump to location nnn)
- [X]  2nnn - CALL addr (Call subroutine at nnn)
- [X]  Bnnn - JP V0, addr (Jump to location nnn + V0)

### 3.2 Instruções de Condição

- [X]  3xkk - SE Vx, byte (Skip next instruction if Vx == kk)
- [X]  4xkk - SNE Vx, byte (Skip next instruction if Vx != kk)
- [X]  5xy0 - SE Vx, Vy (Skip next instruction if Vx == Vy)
- [X]  9xy0 - SNE Vx, Vy (Skip next instruction if Vx != Vy)

### 3.3 Instruções de Atribuição e Matemática

- [X]  6xkk - LD Vx, byte (Set Vx = kk)
- [X]  7xkk - ADD Vx, byte (Set Vx = Vx + kk)
- [X]  8xy0 - LD Vx, Vy (Set Vx = Vy)
- [X]  8xy1 - OR Vx, Vy (Set Vx = Vx OR Vy)
- [X]  8xy2 - AND Vx, Vy (Set Vx = Vx AND Vy)
- [X]  8xy3 - XOR Vx, Vy (Set Vx = Vx XOR Vy)
- [X]  8xy4 - ADD Vx, Vy (Set Vx = Vx + Vy, set VF = carry)
- [X]  8xy5 - SUB Vx, Vy (Set Vx = Vx - Vy, set VF = NOT borrow)
- [X]  8xy6 - SHR Vx {, Vy} (Set Vx = Vx SHR 1)
- [X]  8xy7 - SUBN Vx, Vy (Set Vx = Vy - Vx, set VF = NOT borrow)
- [X]  8xyE - SHL Vx {, Vy} (Set Vx = Vx SHL 1)

### 3.4 Instruções de Memória

- [X]  Annn - LD I, addr (Set I = nnn)
- [X]  Fx55 - LD [I], Vx (Store registers V0 through Vx in memory starting at location I)
- [X]  Fx65 - LD Vx, [I] (Read registers V0 through Vx from memory starting at location I)
- [ ] CXNN - Vx = rand() & NN (Set VX to the result of a bitwise AND operation on a random number and NN)
- [ ] DXYN - draw(Vx, Vy, N) (Draws a sprite at coordinate (VX, VY) with a height of N pixels)
- [ ] FX1E - I += Vx (Adds VX to I. VF is not affected)
- [ ] FX29 - I = sprite_addr[Vx] (Sets I to the location of the sprite for the character in VX)
- [ ] FX33 - set_BCD(Vx) (Stores the BCD representation of VX in memory locations I, I+1, I+2)

### 3.5 Instruções de Teclado e Temporizadores
- [ ] EX9E - if (key() == Vx) (Skips the next instruction if the key stored in VX is pressed)
- [ ] EXA1 - if (key() != Vx) (Skips the next instruction if the key stored in VX is not pressed)
- [ ] FX07 - Vx = get_delay() (Sets VX to the value of the delay timer)
- [ ] FX0A - Vx = get_key() (A key press is awaited, and then stored in VX)
- [ ] FX15 - delay_timer(Vx) (Sets the delay timer to VX)
- [ ] FX18 - sound_timer(Vx) (Sets the sound timer to VX)


## 4. Input Handling

- [ ]  Implementar sistema de entrada para teclado

## 5. Output Handling

- [ ]  Implementar sistema de saída para display

## 6. Debugging e Testes

- [ ]  Escrever testes unitários para cada opcode
- [ ]  Testar o emulador com programas Chip-8 existentes

## 7. Documentação

- [X]  Documentar o projeto

## 8. Otimização

- [ ]  Otimizar o loop principal
- [ ]  Refinar tratamento de entradas e saídas

## 9. Embalagem e Distribuição

- [ ]  Preparar o projeto para distribuição
- [ ]  Criar executáveis para diferentes sistemas operacionais
