from xmlrpc.client import FastParser
from setup import *
from helper import *


WIN = pygame.display.set_mode((WIDTH, HEIGHT))

def draw(cur_word, word_rect, user_word, user_rect, time_word, time_rect):
    WIN.fill(WHITE)

    
    WIN.blit(cur_word, word_rect)
    WIN.blit(user_word, user_rect)
    WIN.blit(time_word, time_rect)
    pygame.display.update()

def main():
    
    score = 0
    start_time = time.time()
    time_left = 10

    user_text = ''
    user_word = FONT.render(user_text, True, BLACK, WHITE) 
    user_rect = user_word.get_rect()
    user_rect.center = (WIDTH // 2, HEIGHT // 2)

    cur_text = ''

    time_word = FONT.render(str(time_left), True, BLACK, WHITE)
    time_rect = time_word.get_rect()
    
    run = True
    found_word = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                    user_word = FONT.render(user_text, True, BLACK, WHITE)
                    user_rect.centerx += 10

                elif event.key == pygame.K_RETURN:
                    if user_text == cur_text and user_rect != '':
                        score += 1

                        user_text = ''
                        user_word = FONT.render(user_text, True, BLACK, WHITE) 
                        user_rect.center = (WIDTH // 2, HEIGHT // 2)

                        found_word = True
                else:
                    user_text += event.unicode
                    user_word = FONT.render(user_text, True, BLACK, WHITE)
                    user_rect.centerx -= 10
        
        if time_left == 0:
            run = False
            print(f'Your typing speed is {score} words per minute')

        if time.time() - start_time >= 1: 
            start_time = time.time()
            time_left -= 1
            time_word = FONT.render(str(time_left), True, BLACK, WHITE)

        if found_word:
            cur_text = WORDS[random.randint(0, len(WORDS)-1)]
            cur_word = FONT.render(cur_text, True, BLACK, WHITE)
            text_rect = cur_word.get_rect()
            text_rect.center = (WIDTH // 2, (HEIGHT // 2) - 100)
            found_word = False

        draw(cur_word, text_rect, user_word, user_rect, time_word, time_rect)





if __name__ == '__main__':
    main()