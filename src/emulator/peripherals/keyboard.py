import sys
import pygame


class Keyboard:
    def __init__(self):
        self.key_map = {
            pygame.K_1: 1,
            pygame.K_2: 2,
            pygame.K_3: 3,
            pygame.K_4: 0xC,
            pygame.K_q: 4,
            pygame.K_w: 5,
            pygame.K_e: 6,
            pygame.K_r: 0xD,
            pygame.K_a: 7,
            pygame.K_s: 8,
            pygame.K_d: 9,
            pygame.K_f: 0xE,
            pygame.K_z: 0xA,
            pygame.K_c: 0xB,
            pygame.K_v: 0xF
        }

    def get_key(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.type in self.key_map:
                    return self.key_map[event.key]
        return None
