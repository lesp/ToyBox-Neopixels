from microbit import *
import neopixel
np = neopixel.NeoPixel(pin0, 100)
from time import sleep
from random import randint
Toy_Mapping = {
"test" : (0,1,2,3,4,5,6,7),
"test2" : (8,9,10,11,12,13,14,15),
"yellow_ring" : (1,30,31),
"green_lips" : (2),
"playdough_tub" : (3),
"duplo_car" : (4,5,34,35),
"yellow_tetris_block" : (6),
"orange_duplo_brick_1" : (7),
"blue_ring" : (8,37,38),
"cream_egg_1" : (9),
"blue_duck" : (10),
"cream_egg_2" : (11),
"orange_lips" : (12),
"orange_ping_pong_ball" : (13),
"green_dinosaur" : (14),
"pink_tetris_block" : (15),
"yellow_cup" : (16),
"blue_fish" : (17),
"purple_roof" : (18),
"lilac_walrus" : (19),
"red_ball_1" : (20),
"purple_bug_butt" : (21),
"blue_4" : (22),
"purple_cat_mask" : (23,24),
"red_ring" : (25,26),
"steam_roller" : (27),
"orange_boat" : (28),
"green_ladybird" : (29),
"orange_egg" : (32),
"green_orange_train_front" : (33),
"red_heart" : (36),
"green_moon" : (39),
"red_ball_2" : (40),
"pink_tractor" : (41,42),
"blue_starfish" : (43),
"yellow_duplo_block" : (44),
"pink_egg" : (45),
"orange_flat_duplo_block" : (46),
"red_flower" : (47),
"green_duplo_block" : (48),
"yellow_cog" : (49),
"green_alligator" : 50,
"orange_roof" : (51),
"yellow_duplo_block_2" : (52),
"purple_zombling" : (53),
"yellow_elephant" : (54),
"green_duplo_block" : (55),
"blue_whistle" : (56),
"orange_ring" : (57, 58),
"green_palm_leaf" : (59),
"purple_tom_mould" : (60,61),
"green_handle" : (62),
"purple_moon" : (63),
"yellow_lips" : (64),
"red_duplo_brick" : (65),
"blue_cup" : (66,67),
"green_dolphin" : (68,69,70,71),
"purple_ladybird" : (72,73),
"barbie_head" : (74),
"yellow_turtle" : (75,76),
"pink_whistle" : (77),
"yellow_insect" : (78),
"purple_duck" : (79,80),
"turqouise_whale" : (81,82),
"red_tall_megablock" : (83,84),
"yellow_boat" : (85,86,87,88),
"fin_the_human" : (89,90),
"squishy_crocodile" : (91),
"red_boat" : (92,93),
"pink_smiley_face" : (94),
"yellow_bear_star" : (95),
"blue_ball" : (96),
"yellow_tetris_brick_2" : (97,98),
"orange_duplo_brick_2" : (99),
"barbie_skirt" : (100),
}

def toylight(toyname):
    for lights in Toy_Mapping[toyname]:
	    red = randint(0,60)
	    green = randint(0,60)
	    blue = randint(0,60)
	    np[lights] = (red, green, blue)
	    np.show()
	    sleep(0.1)

toylight("test")