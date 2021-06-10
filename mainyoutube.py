# Imports
import pygame
import sys
import time
import random
import threading

pygame.init()

# Screen + Font
screen = pygame.display.set_mode((720, 720))
pygame.display.set_caption("Reaction Time!")

main_font = pygame.font.SysFont("Roboto", 90)

# Title
title = main_font.render("Reaction Time Game", True, "red")
title_rect = title.get_rect(center=(360, 50))

# Click to Start
click_to_start = main_font.render("Click to Start", True, "black")
click_to_start_rect = click_to_start.get_rect(center=(360, 360))

# Waiting
waiting = main_font.render("Wait...", True, "black")
waiting_rect = waiting.get_rect(center=(360, 360))

# Click
click = main_font.render("Click NOW!", True, "black")
click_rect = click.get_rect(center=(360, 360))

# Score
score = main_font.render("Speed: 1000 ms", True, "red")
score_rect = score.get_rect(center=(360, 360))

# Game State
game_state = "Click to Start"

# Times 
start_time, end_time = 0, 0

# Game Loop
while True:
	# Events and MOUSEBUTTONDOWN
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			if game_state == "Click to Start":
				game_state = "Waiting"
			elif game_state == "Test Starting":
				ending_time = time.time()
				game_state = "Showing Results"
			elif game_state == "Showing Results":
				game_state = "Click to Start"

	screen.fill("white")

	screen.blit(title, title_rect)

	# Game State Logic
	if game_state == "Click to Start":
		screen.blit(click_to_start, click_to_start_rect)
	elif game_state == "Waiting":
		screen.fill("yellow")

		screen.blit(waiting, waiting_rect)

		pygame.display.update()

		delay_time = random.uniform(1, 10)

		time.sleep(delay_time)

		game_state = "Test Starting"

		starting_time = time.time()
	elif game_state == "Test Starting":
		screen.fill("green")
		screen.blit(click, click_rect)
	elif game_state == "Showing Results":
		reaction_time = round((ending_time - starting_time) * 1000)
		score_text = main_font.render(f"Speed: {reaction_time} ms", True, "black")
		screen.blit(score_text, score_rect)

	# Update Display
	pygame.display.update()