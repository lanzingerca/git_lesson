'''Python script that prints out'''


class ClassName(object):
	"""Generic classname"""
	def __init__(self, arg):
		self.arg = arg

	def method(self):
		a = 10
		for i in range(5):
			print(a + i)

c = ClassName(55)
print(c.method())
print('This is the last line')
