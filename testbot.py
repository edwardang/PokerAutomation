import pypokerengine
from fish_player import FishPlayer 
from consoleplayer import ConsolePlayer 
from random_player import RandomPlayer 
from honestplayer import HonestPlayer
from pypokerengine.api.game import setup_config, start_poker

import pdb

#you can enter either f (fold), c (call/check), or r (raise) and enter the amount to raise. However, note that if the raise option says [-1, -1], raising is not an option.

config = setup_config(max_round=100, initial_stack=1000, small_blind_amount=20)
config.register_player(name="f1", algorithm=FishPlayer())
config.register_player(name="f2", algorithm=FishPlayer())
config.register_player(name="f3", algorithm=FishPlayer())
config.register_player(name="f4", algorithm=FishPlayer())
config.register_player(name="r1", algorithm=RandomPlayer())
config.register_player(name="r2", algorithm=RandomPlayer())
config.register_player(name="r3", algorithm=RandomPlayer())
config.register_player(name="r4", algorithm=RandomPlayer())
config.register_player(name="h1", algorithm=HonestPlayer())
# config.register_player(name="r4", algorithm=RandomPlayer())
# config.register_player(name="r5", algorithm=RandomPlayer())
# config.register_player(name="c1", algorithm=ConsolePlayer())
game_result = start_poker(config, verbose=1)


print('yes')