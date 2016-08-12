class ClassName(object):
	"""docstring for ClassName"""
	def __init__(self):
		super(ClassName, self).__init__()
		
	def get_a(self):
		return 4

	def get_b(self):
		return 5

	def test(self, attr):
		setattr(self, attr, eval("self.get_{}()". format(attr)))

if __name__ == '__main__':
	cla = ClassName()
	cla.test("a")
	cla.test("b")
	print(dir(cla))
	print(cla.a)
	print(cla.b)
