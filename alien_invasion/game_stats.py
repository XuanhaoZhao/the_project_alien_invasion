class GameStats:
	"""docstring for GameStats跟踪游戏统计信息"""
	def __init__(self, ai_game):
		"""初始化统计信息"""
		self.settings = ai_game.settings
		self.reset_stats()

		#让游戏刚启动时处于非活动状态
		self.game_active = False

		#任何情况下都不应重置最高得分
		self.high_score = 0


	def reset_stats(self):
		"""初始化在游戏"""
		self.ships_left = self.settings.ship_limit
		self.score = 0
		self.level = 1