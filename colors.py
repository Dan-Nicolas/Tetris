class Colors:
	dark_grey = (26, 31, 40)
	green = (47, 230, 23)
	red = (232, 18, 18)
	orange = (226, 116, 17)
	yellow = (237, 234, 4)
	purple = (166, 0, 247)
	cyan = (21, 204, 209)
	blue = (13, 64, 216)
	white = (255, 255, 255)
	dark_blue = (44, 44, 127)
	light_blue = (59, 85, 162)
	white = (255,255,255)
	royal_blue = (47, 78, 235)
	
	@classmethod
	def get_cell_colors(cls):
		return [cls.dark_grey, cls.orange, cls.royal_blue, cls.cyan, cls.yellow, cls.green, cls.purple, cls.red]