import time


class Delay:
    def __init__(self):
        self.value = 0

    def update(self):
        if self.value > 0:
            self.value -= 1
            time.sleep(1/60)


class Sound(Delay):
    def __init__(self):
        super().__init__()
        self.beep_sound = pygame.mixer.Sound() # Implementar .wav do beep

    def update(self):
        super().update()
        if self.value > 0:
            # Implementar som
            pass