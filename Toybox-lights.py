from microbit import *
import neopixel
np = neopixel.NeoPixel(pin0, 102)
import time
from random import randint
Toy_Mapping = {
"yellow_ring" : (1,30,31),
"green_lips" : (2,101),
"playdough_tub" : (3,101),
"duplo_car" : (4,5,34,35),
"yellow_tetris_block" : (6,101),
"orange_duplo_brick_1" : (7,101),
"blue_ring" : (8,37,38),
"cream_egg_1" : (9,101),
"blue_duck" : (10,101),
"cream_egg_2" : (11,101),
"orange_lips" : (12,101),
"orange_ping_pong_ball" : (13,101),
"green_dinosaur" : (14,101),
"pink_tetris_block" : (15,101),
"yellow_cup" : (16,101),
"blue_fish" : (17,101),
"purple_roof" : (18,101),
"lilac_walrus" : (19,101),
"red_ball_1" : (20,101),
"purple_bug_butt" : (21,101),
"blue_4" : (22,101),
"purple_cat_mask" : (23,24),
"red_ring" : (25,26),
"steam_roller" : (27,101),
"orange_boat" : (28,101),
"green_ladybird" : (29,101),
"orange_egg" : (32,101),
"green_orange_train_front" : (33,101),
"red_heart" : (36,101),
"green_moon" : (39,101),
"red_ball_2" : (40,101),
"pink_tractor" : (41,42),
"blue_starfish" : (43,101),
"yellow_duplo_block" : (44,101),
"pink_egg" : (45,101),
"orange_flat_duplo_block" : (46,101),
"red_flower" : (47,101),
"green_duplo_block" : (48,101),
"yellow_cog" : (49,101),
"green_alligator" : (50,101),
"orange_roof" : (51,101),
"yellow_duplo_block_2" : (52,101),
"purple_zombling" : (53,101),
"yellow_elephant" : (54,101),
"green_duplo_block" : (55,101),
"blue_whistle" : (56,101),
"orange_ring" : (57, 58),
"green_palm_leaf" : (59,101),
"purple_tom_mould" : (60,61),
"green_handle" : (62,101),
"purple_moon" : (63,101),
"yellow_lips" : (64,101),
"red_duplo_brick" : (65,101),
"blue_cup" : (66,67),
"green_dolphin" : (68,69,70,71),
"purple_ladybird" : (72,73),
"barbie_head" : (74,101),
"yellow_turtle" : (75,76),
"pink_whistle" : (77,101),
"yellow_insect" : (78,101),
"purple_duck" : (79,80),
"turqouise_whale" : (81,82),
"red_tall_megablock" : (83,84),
"yellow_boat" : (85,86,87,88),
"fin_the_human" : (89,90),
"squishy_crocodile" : (91,101),
"red_boat" : (92,93),
"pink_smiley_face" : (94,101),
"yellow_bear_star" : (95,101),
"blue_ball" : (96,101),
"yellow_tetris_brick_2" : (97,98),
"orange_duplo_brick_2" : (99,101),
"barbie_skirt" : (100,101),
}

def toylight(toyname):
    for lights in Toy_Mapping[toyname]:
        print(lights)
        red = randint(128,255)
        green = randint(128,255)
        blue = randint(128,255)
        np[lights] = (red, green, blue)
        np.show()
        time.sleep(0.1)
    time.sleep(1)
    all_off()
        
def all_off():
    for i in range(102):
        np[i] = 0,0,0
        np.show()

while True:
    for key in Toy_Mapping:
        toylight(key)