import pygame

pygame.init()

#list of every game object - cards, dice
game_object_group = pygame.sprite.OrderedUpdates()

#list of every HUD object - at the moment, just big card
hud_group = pygame.sprite.OrderedUpdates()

#card
class Card(pygame.sprite.Sprite):
	
	def __init__(self, identifier):
		self.identifier = identifier
		
		self.x = 0
		self.y = 0
		
		self.facing = 0
		self.rotation = 0
		
		self.facing_image = 0
		self.back_image = 0
		
		self.image = 0
		
		
#setup
def create_cards_from_images(image_directory):
	card_list = []
	return card_list

#-------------------------------------------------------
#NETWORK

#get a socket, send game state as pickled string
#discard socket
def send_network_update(game_object_group):
	pass
	
#get a socket, request update from server,
#receive update from server, unpickle game state
#return game state
def receive_network_update():
	state = []
	return state

#-------------------------------------------------------

running = 1
while running:
	
	for e in pygame.event.get():
		