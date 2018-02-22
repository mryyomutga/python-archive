class genom:
	"""Genom class"""
	genom_list = None
	evaluation = None

	def __init__(self, genom_list, evaluation):
		"""Constractor"""
		self.genom_list = genom_list
		self.evaluation = evaluation
	
	def getGenom(self):
		"""get genom_list"""
		return self.genom_list
	
	def getEvaluation(self):
		"""get evaluation"""
		return self.evaluation
	
	def setGenom(self, genom_list):
		"""set genom_list"""
		self.genom_list = genom_list
	
	def setEvaluation(self, evaluation):
		"""set evaluation"""
		self.evaluation = evaluation
