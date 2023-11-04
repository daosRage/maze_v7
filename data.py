import pygame

pygame.init()

setting_win = {
    "WIDTH": 1000,
    "HEIGHT": 600
}
setting_hero = {
    "WIDTH": 70,
    "HEIGHT": 105
}
setting_bot = {
    "WIDTH": 70,
    "HEIGHT": 70
}
print(1000/20) 
print(600/20) 
maps = {
    "MAP1": [
        "00000001000000000000000000000000010000000000000000",
        "00000000000000000000000000000000000000000000000000",
        "00000000000000000000000000000000000000000000000000",
        "00000000000000000000000000000000000000000000000000",
        "00000000000000000000000000000000000000000000000000",
        "00000000000000000000000000000000000000000000000000",
        "00000000000000003000000000000000020000000100000000",
        "00000000000000000000000000000000000000000000000000",
        "00000000000000000000000000000000000000000000000000",
        "00000000000000000000000000000000000000000000000000",
        "00000000000000000000000000000000000000000000000000",
        "00000000000000000000000000000000000000000000000000",
        "00000000000000000000000000000000000000000000000000",
        "00000000000000000000000000000000000000000000000000",
        "00000000000000000000000000000000000000000000000000",
        "00000000000000000000000000000000000000000000000000",
        "00000000000000000000000000000000000000000000000000",
        "00000000000000001300000021000000000000000000000000",
        "00000000000000000000000000000000000000000000000000",
        "00000000000000000000000000000000000000000000000000",
        "00000000000000000000000000000000000000000200000000",
        "00000002300000002000000002300000200000000300000002",
        "00000000000000000000000000000000000000000000000000",
        "00000000000000000000000000000000000000000000000000",
        "00000000000000000000000000000000000000000000000000",
        "00000000000000000000000000000000000000000000000000",
        "00000000000000000000000000000000000000000000000000",
        "00000000000000000000000000000000000000000000000000",
        "00000000000000000000000000000000000000000000000000",
        "00000000000000000000000000000000000000000000000000"
    ]
}

wall_list = list()

hero_image_list = [
    pygame.transform.scale(pygame.image.load("image\\hero1.png"), (setting_hero["WIDTH"], setting_hero["HEIGHT"])),
    pygame.transform.scale(pygame.image.load("image\\hero2.png"), (setting_hero["WIDTH"], setting_hero["HEIGHT"])),
    pygame.transform.scale(pygame.image.load("image\\hero3.png"), (setting_hero["WIDTH"], setting_hero["HEIGHT"]))
]

bot_walk_image_list = [
    pygame.transform.scale(pygame.image.load("image\\gangster_walk_1.png"), (setting_bot["WIDTH"], setting_bot["HEIGHT"])),
    pygame.transform.scale(pygame.image.load("image\\gangster_walk_2.png"), (setting_bot["WIDTH"], setting_bot["HEIGHT"]))
]
bullet_image = pygame.image.load("image\\bullet.png")