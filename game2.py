import pygame
import random

# Inicializa o pygame
pygame.init()

# Definir as dimensões da tela
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jogo de Captura")

# Cores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Jogador
player_width = 50
player_height = 50
player_x = SCREEN_WIDTH // 2 - player_width // 2
player_y = SCREEN_HEIGHT - player_height - 10
player_speed = 5

# Objetos e Obstáculos
object_radius = 20
object_speed = 5
obstacle_width = 40
obstacle_height = 40
obstacle_speed = 5

# Lista de objetos e obstáculos
objects = []
obstacles = []

# Função para criar objetos aleatórios
def create_object():
    x = random.randint(0, SCREEN_WIDTH - object_radius)
    return pygame.Rect(x, 0, object_radius, object_radius)

# Função para criar obstáculos aleatórios
def create_obstacle():
    x = random.randint(0, SCREEN_WIDTH - obstacle_width)
    return pygame.Rect(x, 0, obstacle_width, obstacle_height)

# Contagem de pontos
score = 0

# Controla o tempo do jogo
clock = pygame.time.Clock()
FPS = 60

# Função principal do jogo
def game():
    global player_x, score

    running = True
    while running:
        screen.fill(WHITE)

        # Eventos do jogo (fechar a janela, teclas pressionadas)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Movimento do jogador
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_width:
            player_x += player_speed

        # Desenho do jogador
        player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
        pygame.draw.rect(screen, BLUE, player_rect)

        # Criar novos objetos e obstáculos
        if random.randint(1, 20) == 1:
            objects.append(create_object())
        if random.randint(1, 30) == 1:
            obstacles.append(create_obstacle())

        # Atualizar e desenhar os objetos
        for obj in objects[:]:
            obj.y += object_speed
            pygame.draw.circle(screen, GREEN, (obj.x, obj.y), object_radius)
            if obj.colliderect(player_rect):
                objects.remove(obj)
                score += 1  # Aumenta a pontuação ao capturar o objeto
            elif obj.y > SCREEN_HEIGHT:
                objects.remove(obj)

        # Atualizar e desenhar os obstáculos
        for obstacle in obstacles[:]:
            obstacle.y += obstacle_speed
            pygame.draw.rect(screen, RED, obstacle)
            if obstacle.colliderect(player_rect):
                running = False  # Fim de jogo ao colidir com um obstáculo
            elif obstacle.y > SCREEN_HEIGHT:
                obstacles.remove(obstacle)

        # Exibir a pontuação
        font = pygame.font.Font(None, 36)
        text = font.render(f"Pontos: {score}", True, (0, 0, 0))
        screen.blit(text, (10, 10))

        # Atualiza a tela
        pygame.display.flip()

        # Controla a taxa de quadros
        clock.tick(FPS)

# Executar o jogo
game()

# Finalizar o pygame
pygame.quit()
