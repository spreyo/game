import pygame
import sys
from pathlib import Path

from pygame.constants import K_ESCAPE, MOUSEBUTTONDOWN
import random

OUTPUT_PATH = Path(__file__).parent

score = 0
class Fighter(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(OUTPUT_PATH / Path('./graphics/fighter.png'))
        self.rect = self.image.get_rect(center= (960, 540))
        self.health = 20
        self.health_max = 20
        self.damage = 50
        self.rotation = 'left'
        self.attacking = False
        self.type = 'Fighter'
        self.score = 0

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.y >=0:
            self.rect.y -= 10
        if keys[pygame.K_a] and self.rect.x >=0:
            self.image = pygame.image.load(OUTPUT_PATH / Path('./graphics/fighter.png'))
            self.rotation = 'left'
            self.rect.x -= 10
        if keys[pygame.K_s] and self.rect.bottom <=1080:
            self.rect.y += 10
        if keys[pygame.K_d] and self.rect.right <=1920:
            self.image = pygame.image.load(OUTPUT_PATH / Path('./graphics/fighterRight.png'))
            self.rotation = 'right'
            self.rect.x += 10   

    def attack(self):
        keys = pygame.mouse.get_pressed()
        if keys[0]:
            if self.rotation == 'left':
                self.image = pygame.image.load(OUTPUT_PATH / Path('./graphics/fighterAttack.png'))
                self.rect = self.image.get_rect(center=self.rect.center)
                self.attacking = True
            if self.rotation == 'right':
                self.image = pygame.image.load(OUTPUT_PATH / Path('./graphics/fighterRightAttack.png'))
                self.rect = self.image.get_rect(center=self.rect.center)
                self.attacking = True


    def update(self):
        if self.image == pygame.image.load(OUTPUT_PATH / Path('./graphics/fighterAttack.png')) or self.image == pygame.image.load(OUTPUT_PATH / Path('./graphics/fighterRightAttack.png')):
            self.attacking == True
        else:
            self.attacking == False
        self.movement()
        self.attack()

class Knight(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(OUTPUT_PATH / Path('./graphics/knight.png'))
        self.rect = self.image.get_rect(center=(960, 540))
        self.health = 50
        self.health_max = 50
        self.damage = 10
        self.rotation = 'left'
        self.attacking = False
        self.type = 'Knight'
        self.score = 0
    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.y >=0:
            self.rect.y -= 10
        if keys[pygame.K_a] and self.rect.x >=0:
            self.rotation = 'left'
            self.image = pygame.image.load(OUTPUT_PATH / Path('./graphics/knight.png'))
            self.rect.x -= 10
        if keys[pygame.K_s] and self.rect.bottom <=1080:
            self.rect.y += 10
        if keys[pygame.K_d] and self.rect.right <=1920:
            self.rotation = 'right'
            self.image = pygame.image.load(OUTPUT_PATH / Path('./graphics/knightRight.png'))
            self.rect.x += 10


    def attack(self):
        keys = pygame.mouse.get_pressed()
        if keys[0]:
            if self.rotation == 'left':
                self.image = pygame.image.load(OUTPUT_PATH / Path('./graphics/knightAttack.png'))
                self.rect = self.image.get_rect(center=self.rect.center)
                self.attacking = True
            if self.rotation == 'right':
                self.image = pygame.image.load(OUTPUT_PATH / Path('./graphics/knightRightAttack.png'))
                self.rect = self.image.get_rect(center=self.rect.center)


    def update(self):
        if self.image == pygame.image.load(OUTPUT_PATH / Path('./graphics/knightAttack.png')) or self.image == pygame.image.load(OUTPUT_PATH / Path('./graphics/knightRightAttack.png')):
            self.attacking == True
        else:
            self.attacking == False
        self.movement()
        self.attack()

class Enemy(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        if type == 'spider':
            self.image = pygame.image.load(OUTPUT_PATH / Path('./graphics/spider.png'))
            self.rect = self.image.get_rect(center=(random.randint(50, 1800), random.randint(50, 900)))
            self.rect = self.rect.inflate(50, 50)
            self.health = 20
            self.damage = 10
    
    def back(self):
        self.image = pygame.image.load(OUTPUT_PATH / Path('./graphics/spider.png'))

    def hurt(self, damage):
        player.sprite.health -= damage

    def CheckAttack(self):
        global hurt_player
        if self.rect.colliderect(player.sprite.rect):
            self.image = pygame.image.load(OUTPUT_PATH / Path('./graphics/spiderAttack.png'))
            self.rect = self.image.get_rect(center=self.rect.center)
            
            
    def update(self):
        self.CheckAttack()
    



pygame.init()
screen = pygame.display.set_mode((1920, 1080))
game_active = False
playerClass = None
fighterClass = pygame.image.load(OUTPUT_PATH / Path('./buttons/fighterClass.png'))
fighter_rect = fighterClass.get_rect(center= (328, 672))
knightClass = pygame.image.load(OUTPUT_PATH / Path('./buttons/knightClass.png'))
knight_rect = knightClass.get_rect(center= (1592 , 672))
game_font = pygame.font.Font(OUTPUT_PATH / Path('./fonts/ubuntu.ttf'), 50)
background = pygame.image.load(OUTPUT_PATH / Path('./graphics/background.png'))
clock = pygame.time.Clock()
enemies_group = pygame.sprite.Group()
enemies_group.sprites()
SPAWN = pygame.USEREVENT + 1 
ATTACK_ANIMATION = pygame.USEREVENT + 2
ATTACK_PLAYER = pygame.USEREVENT + 3
hurt_player = True
spawnMobs = True
enemies = []
score = 0
timer = pygame.time.set_timer(SPAWN, 900)
attack_timer = pygame.time.set_timer(ATTACK_ANIMATION, 500)
attack_player_timer = pygame.time.set_timer(ATTACK_PLAYER, 900)
attacking = False
while True:
    player = pygame.sprite.GroupSingle(playerClass)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if fighter_rect.collidepoint(event.pos):
                playerClass = Fighter()
                player = pygame.sprite.GroupSingle(playerClass)
                game_active = True
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            if knight_rect.collidepoint(event.pos):
                playerClass = Knight()
                player = pygame.sprite.GroupSingle(playerClass)
                game_active = True
        if event.type == pygame.KEYDOWN:
            if pygame.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == SPAWN:
            if spawnMobs == True:
                if len(enemies_group.sprites()) < 5:
                    enemies_group.add(Enemy(type='spider'))
                else:
                    pass
        if event.type == ATTACK_ANIMATION:
            if game_active:
                for spriteObject in enemies_group.sprites():
                    spriteObject.back()
                player = pygame.sprite.GroupSingle(playerClass)
                player_damage = player.sprite.damage
                hit = pygame.sprite.spritecollide(player.sprite, enemies_group, False)
                if len(hit) > 0:
                    if hurt_player:  
                        if player.sprite.health > 0:
                            player.sprite.health -= 10
                            hurt_player = False
                elif not len(hit) > 0:
                    hurt_player = True

            if event.type == ATTACK_ANIMATION:
                if attacking == True:
                    if player.sprite.type == 'Knight':
                        if player.sprite.rotation == 'right':
                            player.sprite.image = pygame.image.load(OUTPUT_PATH / Path('./graphics/knightRight.png'))
                        elif player.sprite.rotation == 'left':
                            player.sprite.image = pygame.image.load(OUTPUT_PATH / Path('./graphics/knight.png'))
                    elif player.sprite.type == 'Fighter':
                        if player.sprite.rotation == 'right':
                            player.sprite.image = pygame.image.load(OUTPUT_PATH / Path('./graphics/fighterRight.png'))
                        elif player.sprite.rotation == 'left':
                            player.sprite.image = pygame.image.load(OUTPUT_PATH / Path('./graphics/fighter.png'))
        if event.type == pygame.MOUSEBUTTONDOWN:
            hit = pygame.sprite.spritecollide(player.sprite, enemies_group, False)
            for enemy in hit:
                enemy.health -= player.sprite.damage
                if enemy.health <= 0:
                    enemy.kill()
                    score += 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DELETE:
                game_active = False

    if game_active == False:
        screen.fill('#297e46')
        screen.blit(fighterClass, fighter_rect)
        screen.blit(knightClass, knight_rect)
        score = 0

    if game_active:
        screen.blit(background, (0, 0))
        attacking = player.sprite.attacking
        hit = pygame.sprite.spritecollide(player.sprite, enemies_group, False)
        player.draw(screen)
        player.update()
        stats = game_font.render(f'{player.sprite.health} / {player.sprite.health_max}', True, 'white')
        stats_rect = stats.get_rect(center=(1383,797))
        score_text = game_font.render(f'Score:{score}', True, 'white')
        score_text_rect = score_text.get_rect(center=(665, 875))
        screen.blit(score_text, score_text_rect)
        screen.blit(stats, stats_rect)
        enemies_group.draw(screen)
        enemies_group.update()
        if player.sprite.health <= 0:
            game_active = False
    pygame.display.update()
    clock.tick(60)
