import pygame
import sys
import time
import random
import os

from movies import *


pygame.init()

WIN_HEIGHT = 800
WIN_WIDTH = 1200
WINDOW = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Rotten Tomatoes Guessing Game")

def load_image(number):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    image_path = os.path.join(script_dir, "images", f"{number}.jpg")
    print("Image path: ", image_path)
    return pygame.image.load(image_path)

image_files = os.listdir(os.path.join(os.path.dirname(os.path.realpath(__file__)), "images"))
print("Contents of 'images' directory:", image_files)


class Button:
    def __init__(self, color, x, y, width, height, text=""):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        if outline:
            pygame.draw.rect(win, outline, (self.x-2, self.y-2, self.width+4, self.height+4), 0)
        
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)
        
        if self.text != "":
            font = pygame.font.Font(None, 36)
            text = font.render(self.text, 1, "black")
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def is_over(self, pos):
        mouse_x, mouse_y = pos
        if self.x < mouse_x < self.x + self.width:
            if self.y < mouse_y < self.y + self.height:
                return True
        return False


def main_menu():
    run = True
    decision = False
    clock = pygame.time.Clock()
    #print("Entering main menu loop")
    while run:
        #print("inside main menu loop")
        # Fill the window with white
        WINDOW.fill("black")
# center=(((WIN_WIDTH // 2) - 300), (WIN_HEIGHT * 3 // 4)
        # Create buttons
        critic = Button((255, 0, 0), 200, 300, 300, 200, "Critic Score")
        audience = Button((0, 0, 255), 700, 300, 300, 200, "Audience Score")

        # Draw buttons
        critic.draw(WINDOW)
        audience.draw(WINDOW)

        # Handle events
        for event in pygame.event.get():
            #print("event: ", event)
            if event.type == pygame.QUIT:
                print("Quit event detected")
                run = False
                break

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                print("mouse click at: ", mouse_x, mouse_y)
                if critic.is_over((mouse_x, mouse_y)):
                    print("critic button clicked")
                    main("critic")
                    decision = True
                elif audience.is_over((mouse_x, mouse_y)):
                    print("audience button clicked")
                    main("audience")
                    decision = True
        pygame.display.update()
        clock.tick(30)
        if decision == True:
            run = False
    pygame.quit()
    sys.exit()

def main(score):
    if score == "critic":
        score = 1
    else:
        score = 2
    
    run = True
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)
    #print("entering main game loop")
    correct_message = None  # Variable to store the correct/incorrect message
    correct_answer = None  # Variable to store the correct movie information
    decision = True
    points = 0
    while run:
        points_text = font.render(f"Score: {points}", 1, "white")
        WINDOW.blit(points_text, (20, 20))
        pygame.display.update()
        #print("inside main game loop")
        end = len(movieList)
        if decision == True:
            WINDOW.fill((60, 0, 0))
            question = random.choice(["higher", "lower"])
            text = font.render(f"Choose the image with the {'higher' if question == 'higher' else 'lower'} score", True, "white")
            text_rect = text.get_rect(center=(WIN_WIDTH // 2, (WIN_HEIGHT // 4) - 100))
            WINDOW.blit(text, text_rect)
            # Display images and text

        # Scale the images to the same size
            num1 = random.randint(0, end-1)
            num2 = random.randint(0, end-1)
            #print("before loading image")
            #print("after loading image")
            #print("before setting movies")
            movie1 = movieList[num1]
            movie2 = movieList[num2]
            #print("after setting movies")

            while movie1[1] == movie2[1] or movie1[2] == movie2[2] or movie1 == movie2:
                num2 = random.randint(0, end-1)
                movie2 = movieList[num2]
            
            image1 = load_image(num1)
            image2 = load_image(num2)
            image_width = WIN_WIDTH // 3
            image_height = WIN_HEIGHT // 2
            scaled_image1 = pygame.transform.scale(image1, (image_width, image_height))
            scaled_image2 = pygame.transform.scale(image2, (image_width, image_height))

            image1_name = font.render(movie1[0], True, "white")
            image1_name_rect = image1_name.get_rect(center=(((WIN_WIDTH // 2) - 300), (WIN_HEIGHT * 3 // 4) - 450 ))
            WINDOW.blit(image1_name, image1_name_rect)

            image2_name = font.render(movie2[0], True, "white")
            image2_name_rect = image2_name.get_rect(center=(((WIN_WIDTH // 2) + 300), (WIN_HEIGHT * 3 // 4) - 450 ))
            WINDOW.blit(image2_name, image2_name_rect)



        # Adjust the distance between images
            distance_between_images = 100  # Adjust this value as needed
            scaled_image1_rect = scaled_image1.get_rect(left=(WIN_WIDTH // 2 - distance_between_images - image_width), centery=WIN_HEIGHT // 2)
            WINDOW.blit(scaled_image1, scaled_image1_rect)
        
            scaled_image2_rect = scaled_image2.get_rect(left=(WIN_WIDTH // 2 + distance_between_images), centery=WIN_HEIGHT // 2)
            WINDOW.blit(scaled_image2, scaled_image2_rect)
            pygame.display.update()
            decision = False

        
        #print("Before event loop")
        
        # Separate event handling loop
        for event in pygame.event.get():
            #print("Event: ", event)
            if event.type == pygame.QUIT:
                run = False
                print("Quit event detected")
                break

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                print("Mouse click at: ", mouse_x, mouse_y)
                if question == "higher":
                    correct_image = scaled_image1 if movie1[score] > movie2[score] else scaled_image2
                    #correct_answer = movie1 if movie1[score] > movie2[score] else movie2
                else:
                    correct_image = scaled_image1 if movie1[score] < movie2[score] else scaled_image2
                    #correct_answer = movie1 if movie1[score] < movie2[score] else movie2
                if correct_image == scaled_image1:
                    correct_image_rect = scaled_image1_rect
                else:
                    correct_image_rect = scaled_image2_rect
                WINDOW.blit(correct_image, correct_image_rect)
                if correct_image_rect.collidepoint(mouse_x, mouse_y):
                    print("Correct!")
                    correct_message = "Correct!"
                    points += 1
                else:
                    print("Incorrect!")
                    correct_message = "Incorrect!"
                pygame.time.delay(1000)
                decision = True  # Set the flag to True after user has made a selection
        
        if decision == False:
            continue  # Skip the rest of the loop and start from the beginning if no selection is made
        
        # Display correct/incorrect message
        if correct_message == "Correct!":
            result_text = font.render(correct_message, True, "green")
            result_text_rect = result_text.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT * 3 // 4))
        elif correct_message == "Incorrect!":
            result_text = font.render(correct_message, True, "red")
            result_text_rect = result_text.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT * 3 // 4))
        rect = Button("black", 500, 500, 200, 200, "")
        rect.draw(WINDOW)
        WINDOW.blit(result_text, result_text_rect)
        WINDOW.blit(points_text, (20, 20))

        #result_text = font.render(correct_message, True, "green" if correct_message == "Correct!" else "red")
        #result_text_rect = result_text.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT * 3 // 4))
        #WINDOW.blit(result_text, result_text_rect)

        movie1_text = font.render(str(movie1[score]), True, "white")
        movie1_text_rect = movie1_text.get_rect(center=(((WIN_WIDTH // 2) - 300), (WIN_HEIGHT * 3 // 4) + 20))
        WINDOW.blit(movie1_text, movie1_text_rect)

        movie2_text = font.render(str(movie2[score]), True, "white")
        movie2_text_rect = movie2_text.get_rect(center=(((WIN_WIDTH // 2) + 300), (WIN_HEIGHT * 3 // 4) + 20 ))
        WINDOW.blit(movie2_text, movie2_text_rect)
            # Introduce a delay to display the message for a short time
        pygame.display.update()
        correct_message = None
        pygame.time.delay(2000)  # Adjust the delay time (in milliseconds) as needed
        pygame.display.update() # Clear the correct message after the delay

        #print("before display update")
        pygame.display.update()
        clock.tick(30)

    pygame.quit()
    sys.exit()
if __name__ == "__main__":
    main_menu()