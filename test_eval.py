class ClassName(object):
	"""docstring for ClassName"""
	def __init__(self):
		super(ClassName, self).__init__()
		
	def a(self):
		print("Dai dep trai")
		return 4

	def test(self, name):
		x = eval("self.{}()". format(name))
		print(x)

if __name__ == '__main__':
	cla = ClassName()
	cla.test("a")
