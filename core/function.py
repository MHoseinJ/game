import pygame
import numpy as np
pygame.mixer.init()

def play_beep(frequency=1000, duration=200):
    sample_rate = 44100
    n_samples = int(sample_rate * duration / 1000)
    buf = np.zeros((n_samples, 2), dtype=np.int16)
    amplitude = 32767
    for s in range(n_samples):
        t = float(s) / sample_rate
        val = int(amplitude * np.sin(2 * np.pi * frequency * t))
        buf[s][0] = val
        buf[s][1] = val
    sound = pygame.sndarray.make_sound(buf)
    sound.play()

def draw_objects(Size, List, screen, color, shadow, addPos=0):
    for x in List:
        shadow_surface = pygame.Surface((Size + 10, Size + 10), pygame.SRCALPHA)
        pygame.draw.rect(shadow_surface, shadow, [5, 5, Size, Size])
        screen.blit(shadow_surface, (x[0] - 5, x[1] + 5))

    for x in List:
        pygame.draw.rect(screen, color, [x[0], x[1], Size, Size])

def draw_object(Size, pos, screen, color, shadow):
    if not isinstance(shadow, bool):
        shadow_surface = pygame.Surface((Size[0] + 10, Size[1] + 10), pygame.SRCALPHA)
        pygame.draw.rect(shadow_surface, shadow, [5, 5, Size[0], Size[1]])
        screen.blit(shadow_surface, (pos[0] - 5, pos[1] + 5))
    pygame.draw.rect(screen, color, [pos[0], pos[1], Size[0], Size[1]])

def starter_tick():
    global slow
    slow = True
    return pygame.time.get_ticks()

def save_screenshot(screen):
    import time
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    pygame.image.save(screen, f"screenshot_{timestamp}.png")
    print(f"screenshot was saved: screenshot_{timestamp}.png")

def draw_char(screen, ch, pos, color, size=22):
    import core.loader as loader
    ch = ch.upper()
    if ch not in loader.font:
        return
    font = loader.font[ch]
    pixel_size = max(1, size // 6)
    for y, row in enumerate(font):
        for x, bit in enumerate(row):
            if bit == '1':
                pygame.draw.rect(screen, color,
                                 pygame.Rect(pos[0] + x * pixel_size,
                                             pos[1] + y * pixel_size,
                                             pixel_size, pixel_size))

def draw_text(screen, text, pos, color, size=22, spacing=4):
    x, y = pos
    for ch in text:
        if ch == ' ':
            x += size // 2
        else:
            draw_char(screen, ch, (x, y), color, size)
            x += size + spacing

def get_text_width(text, size=22, spacing=2):
    return len(text) * (size + spacing) - spacing

def generate_checkered_ground(size, width, height):
    return [(x, y) for y in range(0, height, size) for x in range(0, width, size)]

def Controller(state, snake_velocity, SNAKE_SPEED, screenshut, WINDOW_SIZE):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return "quit", snake_velocity, screenshut
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if state == "running":
                    play_beep()
                    state = "paused"
                elif state == "paused":
                    state = "running"
            if state == "running":
                if event.key == pygame.K_UP and snake_velocity[1] == 0:
                    snake_velocity = [0, -SNAKE_SPEED]
                elif event.key == pygame.K_DOWN and snake_velocity[1] == 0:
                    snake_velocity = [0, SNAKE_SPEED]
                elif event.key == pygame.K_LEFT and snake_velocity[0] == 0:
                    snake_velocity = [-SNAKE_SPEED, 0]
                elif event.key == pygame.K_RIGHT and snake_velocity[0] == 0:
                    snake_velocity = [SNAKE_SPEED, 0]
                elif event.key == pygame.K_s:
                    screenshut = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                if event.pos[0] < WINDOW_SIZE[0] and event.pos[1] < WINDOW_SIZE[1]:
                    state = "running" if state == "paused" else "paused"
            elif event.button == 1 and state == "running":
                mx, my = event.pos
                cx, cy = WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2
                dx, dy = mx - cx, my - cy
                if abs(dx) > abs(dy):
                    if dx > 0 and snake_velocity[0] == 0:
                        snake_velocity = [SNAKE_SPEED, 0]
                    elif dx < 0 and snake_velocity[0] == 0:
                        snake_velocity = [-SNAKE_SPEED, 0]
                else:
                    if dy > 0 and snake_velocity[1] == 0:
                        snake_velocity = [0, SNAKE_SPEED]
                    elif dy < 0 and snake_velocity[1] == 0:
                        snake_velocity = [0, -SNAKE_SPEED]
    return state, snake_velocity, screenshut

def handle_state(screen, state, loader, WINDOW_SIZE, clock, snake, SNAKE_SPEED, apple, tickRate, startTick):
    if state == "paused":
        text = "PAUSED"
        text_width = get_text_width(text, size=22, spacing=2)
        x = (WINDOW_SIZE[0] - text_width) // 2
        y = WINDOW_SIZE[1] // 2
        draw_text(screen, text, [x, y], loader.white, 22, 2)
        draw_text(screen, "game version: " + loader.gameVersion, [10, WINDOW_SIZE[1] + 5], loader.white, 15, 2)
        pygame.display.update()
        clock.tick(60)
        return state, snake, tickRate, startTick, True

    if state == "gameover":
        text = "GAME OVER"
        text_width = get_text_width(text, size=22, spacing=2)
        x = (WINDOW_SIZE[0] - text_width) // 2
        y = WINDOW_SIZE[1] // 2
        draw_text(screen, text, [x, y], loader.white, 22, 2)
        pygame.display.update()
        for freq in [840, 720, 600, 480]:
            play_beep(freq)
            pygame.time.delay(190)
        pygame.time.delay(1500)
        snake = [[WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2]]
        tickRate = 5
        startTick = starter_tick()
        apple["available"] = False
        state = "paused"
        return state, snake, tickRate, startTick, True

    return state, snake, tickRate, startTick, False

def apple_spawn(apple, SNAKE_SIZE, WINDOW_SIZE, snake):
    import random
    if not apple["available"]:
        apple["pos"] = [
            random.randint(0, WINDOW_SIZE[0] // SNAKE_SIZE - 1) * SNAKE_SIZE,
            random.randint(0, WINDOW_SIZE[1] // SNAKE_SIZE - 1) * SNAKE_SIZE
        ]
        apple["available"] = True
        while apple["pos"] in snake:
            apple["pos"] = [
                random.randint(0, WINDOW_SIZE[0] // SNAKE_SIZE - 1) * SNAKE_SIZE,
                random.randint(0, WINDOW_SIZE[1] // SNAKE_SIZE - 1) * SNAKE_SIZE
            ]
    return apple

def window_setup():
    WINDOW_SIZE = [400, 400]
    screen = pygame.display.set_mode([WINDOW_SIZE[0], WINDOW_SIZE[1] + 30])
    pygame.display.set_caption("Snake Game")
    icon_surface = pygame.Surface((32, 32), pygame.SRCALPHA)
    pygame.draw.rect(icon_surface, (0, 200, 0), (4, 4, 24, 24))
    pygame.draw.rect(icon_surface, (0, 100, 0), (8, 20, 16, 6))
    pygame.draw.rect(icon_surface, (255, 255, 255), (2, 6, 6, 6))
    pygame.draw.rect(icon_surface, (0, 0, 0), (4, 8, 2, 2))
    pygame.draw.rect(icon_surface, (255, 255, 255), (24, 6, 6, 6))
    pygame.draw.rect(icon_surface, (0, 0, 0), (26, 8, 2, 2))
    pygame.draw.polygon(icon_surface, (255, 0, 0), [(15, 26), (17, 26), (16, 32)])
    pygame.display.set_icon(icon_surface)
    return screen, WINDOW_SIZE

def die(snake, screen):
    import core.loader as loader
    import random, math
    clock = pygame.time.Clock()

    class Particle:
        def __init__(self, pos):
            self.x, self.y = pos
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(2, 5)
            self.vx = speed * math.cos(angle)
            self.vy = speed * math.sin(angle)
            self.alpha = 255
            self.life = random.uniform(0.6, 1.0)
            self.age = 0

        def update(self, dt):
            self.x += self.vx
            self.y += self.vy
            self.age += dt
            self.alpha = max(0, 255 * (1 - self.age / self.life))

        def draw(self, surf):
            if self.alpha > 0:
                s = pygame.Surface((10, 10), pygame.SRCALPHA)
                pygame.draw.rect(s, loader.violet + (int(self.alpha),), [0, 0, 10, 10])
                surf.blit(s, (self.x - 5, self.y - 5))

    particles = []
    while len(snake) > 0:
        tail = snake.pop(0)
        for _ in range(8):
            particles.append(Particle((tail[0] + 10, tail[1] + 10)))
        timer, dt = 0, 0
        while timer < 0.12:
            screen.fill(loader.black)
            draw_objects(20, snake, screen, loader.violet, loader.shadow)
            for p in particles[:]:
                p.update(dt)
                p.draw(screen)
                if p.alpha <= 0:
                    particles.remove(p)
            pygame.display.update()
            dt = clock.tick(12) / 1000
            timer += dt
    timer = 0
    while particles and timer < 1:
        screen.fill(loader.black)
        for p in particles[:]:
            p.update(dt)
            p.draw(screen)
            if p.alpha <= 0:
                particles.remove(p)
        pygame.display.update()
        dt = clock.tick(12) / 1000
        timer += dt

