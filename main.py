import pygame

if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    image = pygame.Surface([50, 50])
    image = pygame.image.load('data/arrow.png')
    running = True
    while running:
        # внутри игрового цикла ещё один цикл
        # приема и обработки сообщений
        for event in pygame.event.get():
            if pygame.mouse.get_focused():
                pygame.mouse.set_cursor((0, 0), image)
            if event.type == pygame.QUIT:
                running = False

        # отрисовка и изменение свойств объектов
        # ...

        # обновление экрана
        pygame.display.flip()
    pygame.quit()