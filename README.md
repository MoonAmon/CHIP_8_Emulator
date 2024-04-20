# Emulador de Chip-8

## Sobre o Projeto
Este é um emulador do Chip-8, uma arquitetura de computador simples usada para aprender conceitos básicos de emulação. O projeto permite carregar programas Chip-8 e executá-los em um ambiente de emulação, exibindo gráficos, manipulando entrada e simulando o comportamento do Chip-8.

## Recursos Principais
- **Emulação Completa**: Implementa a arquitetura do Chip-8, incluindo memória, registradores, ciclo de instruções, e gráficos.
- **Gráficos Monocromáticos**: Suporta display de 64x32 pixels para renderização de sprites.
- **Entrada de Teclado**: Mapeia o teclado hexadecimal do Chip-8 para um teclado QWERTY.
- **Carregamento de ROMs**: Permite carregar programas do Chip-8 para emulação.
- **Temporizadores**: Inclui suporte para delay timer e sound timer.

## Divisão do Projeto em Módulos
- **CPU**: Responsável por buscar, decodificar e executar as instruções.
- **Memória**: Gerencia a memória do Chip-8 tem 4 KB, onde os porgramas são carregados e executados.
- **Registradores**: Implementa os registradores Vx, I, e os temporizadores DT e ST.
- **Entrada/Teclado**: Simula a entrada do teclado hexadecimal original.
- **Display/Grafico**: Responsável pelo renderização gráfica do Chip-8.
- **Instruções**: Implementa a lógica para cada instrução do conjunto do Chip-8.

