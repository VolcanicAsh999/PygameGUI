import pygame

__all__ = ['ScreenHandler']

class ScreenHandler:
    def __init__(self, screen):
        self._screen = screen

    def wait_for_click(self, func=(lambda: ..., ())):
        click = ()
        while click == ():
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click = (event.button, event.pos)
                elif event.type == pygame.QUIT:
                    pygame.quit()
            func[0](*func[1])
        return click

    def draw_text(self, pos, text, size=20, color='black', font='default'):
        if font != 'default':
            text = pygame.font.Font(font+'.ttf', size).render(text, 1, pygame.Color(color))
        else:
            text = pygame.font.SysFont(font, size).render(text, 1, pygame.Color(color))
        self._screen.blit(text, pos)
