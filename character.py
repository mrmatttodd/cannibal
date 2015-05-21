from item import Item
from part import Part

class Character():
	"""Character
		
		Attributes:
			name - the characters name chosen on 
			       game start

			is_player - is the player an NPC?

			loc_x, loc_y - the location co-ordinates
			       of the character

			health - character's health

			status - characters current status can be
			       'Awake', 'Coma', 'Dead'

			inventory - the set of items in the
			       characters inventory

			leg_l, leg_r, arm_l, arm_r, head - parts
			       that can be added to the character

	"""

	def __init__(self, name, is_player):
		self.name = name
		self.is_player = is_player
		self.loc_x = 0
		self.loc_y = 0
		self.health = 100
		self.status = 'Awake'
		self.invetory = set()
		self.leg_l = None
		self.leg_r = None
		self.arm_l = None
		self.arm_r = None
		self.head  = None

	def health_change(self, value):
		""" Modify health by value

			Args:
				value - the amount to modify health by
				        can be positive or negative
			
			Return:
				status - The current status of the player
				         'Awake', 'Coma', 'Dead'

			Side Effects:
				Health should have been modified.
		"""
		pass

	def add_item(self, item):
		""" Add item to the character's inventory

			Args:
				item - the item object to be added to the
				       inventory

			Return:
				None

			Side Effects:
				Item should be added to inventory
		"""
		pass

	def remove_item(self, item):
		""" Remove item from the character's inventory

			Args:
				item - the item object to be removed from the
				       inventory

			Return:
				None

			Side Effects:
				Item should be removed from inventory
		"""
		pass
	
	def add_part(self, part):
		""" Add a part to the character

			Args:
				part - the part object to be added to the
				       character

			Return:
				None

			Side Effects:
				Part should be added in the correct location
		"""
		pass

	def remove_part(self, part):
		""" Remove a part from the character

			Args:
				part - the part object to be removed from the
				       character

			Return:
				None

			Side Effects:
				Correct part should be removed
		"""	
		pass
