import pygame
import math

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball in Hexagon")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Ball properties
ball_radius = 10
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_speed = 3
ball_angle = math.radians(45)  # Initial direction

# Hexagon properties
hex_radius = 200
hex_center = (WIDTH // 2, HEIGHT // 2)
hex_points = [
    (
        hex_center[0] + hex_radius * math.cos(math.radians(60 * i)),
        hex_center[1] + hex_radius * math.sin(math.radians(60 * i)),
    )
    for i in range(6)
]


def reflect(angle, normal):
    """Reflects an angle around a given normal."""
    normal_angle = math.atan2(normal[1], normal[0])
    return 2 * normal_angle - angle


def get_normal(p1, p2):
    """Computes the normal of a given hexagonal edge."""
    edge_vector = (p2[0] - p1[0], p2[1] - p1[1])
    normal = (-edge_vector[1], edge_vector[0])
    norm_length = math.hypot(normal[0], normal[1])
    return (normal[0] / norm_length, normal[1] / norm_length)


# Game loop
running = True
while running:
    screen.fill(WHITE)
    pygame.draw.polygon(screen, BLUE, hex_points, 3)

    # Move ball
    ball_x += ball_speed * math.cos(ball_angle)
    ball_y += ball_speed * math.sin(ball_angle)

    # Collision detection with hexagon edges
    for i in range(6):
        p1, p2 = hex_points[i], hex_points[(i + 1) % 6]
        edge_vec = (p2[0] - p1[0], p2[1] - p1[1])
        normal = get_normal(p1, p2)

        # Check if ball crosses the edge using vector projection
        ap = (ball_x - p1[0], ball_y - p1[1])
        proj = ap[0] * normal[0] + ap[1] * normal[1]
        if proj < ball_radius:
            ball_angle = reflect(ball_angle, normal)
            break

    # Draw ball
    pygame.draw.circle(screen, RED, (int(ball_x), int(ball_y)), ball_radius)

    pygame.display.flip()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.time.delay(10)

pygame.quit()
