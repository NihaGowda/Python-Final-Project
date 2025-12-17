from src.io_utils import load_levels_csv
from src.player import Player
from src.game import GameEngine

levels = load_levels_csv("data/levels.csv")
player = Player(name="Meeval")
engine = GameEngine()

engine.run_main_menu(player, levels)
