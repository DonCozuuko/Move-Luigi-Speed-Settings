import pygame as pg

pg.init()
pg.font.init()
FONT = pg.font.SysFont(None, 40)
FONT_S = pg.font.SysFont(None, 60)

WIN_SIZE = (600, 600)
WIDTH, HEIGHT = WIN_SIZE
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SPEED = 1

SCREEN = pg.display.set_mode(WIN_SIZE)

def checkForInput(position, rect):
    if position[0] in range(rect.left, rect.right) and position[1] in range(rect.top, rect.bottom):
        return True
    return False

class Block():
    def __init__(self):
        self.screen = SCREEN
        self.image = pg.image.load("Sprite_Control/Luigi.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        self.x = 0
        self.y = 0

    def movement(self):
        global SPEED
        key = pg.key.get_pressed()
        dist = SPEED
        if key[pg.K_w]:
            self.y -= dist
        elif key[pg.K_s]:
            self.y += dist
        elif key[pg.K_d]:
            self.x += dist
        elif key[pg.K_a]:
            self.x -= dist
        
    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))


class Menu:
    def __init__(self):
        self.add_button_rect = None
        self.minus_button_rect = None


    def draw_menu_icon(self):
        image = pg.image.load("Sprite_Control/gear.png")
        IMAGE = pg.transform.scale(image, (50, 50))
        rect = IMAGE.get_rect()
        rect.topright = (600, 0)
        SCREEN.blit(IMAGE, rect)


    def add_speed(self):
        text = FONT_S.render(" + ", True, WHITE)
        self.add_button_rect = text.get_rect()
        self.add_button_rect.center = (WIDTH // 2 + 30, HEIGHT // 2)
        self.add_button_rect.top = 150
        SCREEN.blit(text, self.add_button_rect)
    

    def minus_speed(self):
        text = FONT_S.render(" - ", True, WHITE)
        self.minus_button_rect = text.get_rect()
        self.minus_button_rect.center = (WIDTH // 2 - 30, HEIGHT // 2)
        self.minus_button_rect.top = 150
        SCREEN.blit(text, self.minus_button_rect)


    def display_speed(self, speed):
        speed = FONT_S.render(f"{speed}", True, WHITE)
        speed_rect = speed.get_rect()
        speed_rect.center = (WIDTH // 2, HEIGHT // 2)
        speed_rect.top = 200
        SCREEN.blit(speed, speed_rect)

    
    def close_menu(self):
        image = pg.image.load("Sprite_Control/white x.png")
        IMAGE = pg.transform.scale(image, (50, 50))
        self.close_menu_rect = IMAGE.get_rect()
        self.close_menu_rect.topright = (550, 0)
        SCREEN.blit(IMAGE, self.close_menu_rect)


    def open_menu(self):
        global SPEED

        while True:
            
            SCREEN.fill(BLACK)
            MOUSE_POS = pg.mouse.get_pos()

            text1 = FONT.render("Speed:", True, WHITE)
            text1_rect = text1.get_rect()
            text1_rect.center = (WIDTH // 2, HEIGHT // 2)
            text1_rect.top = 100
            SCREEN.blit(text1, text1_rect)
            
            Menu.add_speed(self)
            Menu.minus_speed(self)
            Menu.display_speed(self, SPEED)
            Menu.close_menu(self)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()

                if event.type == pg.MOUSEBUTTONDOWN:
                    if checkForInput(MOUSE_POS, self.add_button_rect):
                        SPEED += 1
                    elif checkForInput(MOUSE_POS, self.minus_button_rect):
                        SPEED -= 1
                    elif checkForInput(MOUSE_POS, self.close_menu_rect):
                        print("i work")
                        return
                    
            pg.display.update()


class Game:
    def __init__(self):
        self.Block = Block()
        self.Menu = Menu()
        self.input = False

    
    def check_events(self):
        self.position = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()

            if event.type == pg.MOUSEBUTTONDOWN and self.position[0] in range(550, 600) and self.position[1] in range(0, 50):
                self.input = True


    def run_game(self):
        while True:

            SCREEN.fill(BLACK)
            self.Block.movement()
            self.Block.draw()
            self.Menu.draw_menu_icon()

            if self.input == True:
                self.Menu.open_menu()
                self.input = False

            self.check_events()
            pg.display.update()


if __name__ == "__main__":
    game = Game()
    game.run_game()