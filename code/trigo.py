#!/usr/bin/python

import math

# from linear import x_simple as x_simple
from linear import *

class trigo():
	'''
	Toy forward automatic differentiation
	class.
	E.g.
	f(x) = alpha * sin(x) + beta

	Note:
	x is a class object
	'''
	# def __init__(self, x_object, alpha=1, beta=0):

	# 	# #self.a = a # value to evaluate at
	# 	# self.alpha = alpha # regard as a x variable with coefficient of x = 1
	# 	# self.beta = beta # regard as a x variable with no constant
	# 	# #self.currclass = currclass

	# 	# self.val = self.calc_function_val()
	# 	# self.der = self.calc_function_derivative_val()

	# 	raise NotImplementedError

	def __init__(self, x_object, alpha=1, beta=0):
		self.alpha = alpha # regard as a x variable with coefficient of the trigo operation (e.g. sine)
		self.beta = beta # regard as a x variable with no constant
		self.x_object = x_object # regard as a simple x_object class within the trigo operation (e.g. sine)

		self.val = self.calc_function_val()
		self.der = self.calc_function_derivative_val()


	def calc_function_val(self):
		'''
		Calculate the current value of this
		function at the 
		'''
		raise NotImplementedError

	
	def calc_function_derivative_val(self):
		'''
		Calculate the derivative of this function
		at the a value of interest
		'''
		raise NotImplementedError


	def update_value_and_derivative(self):
		'''
		Run functions to update the function values
		and derivatives
		'''
		self.val = self.calc_function_val()
		self.der = self.calc_function_derivative_val()


	def __add__(self, other):
		'''
		Performs addition of two trigo objects,
		or trigo object with a float/int
		'''
		#print(self.__add__.__qualname__)

		# Assume that both objects are AutoDiffToyObjects
		# try:
		# 	alpha = self.alpha + other.alpha
		# 	beta = self.beta + other.beta
		# 	new_toy = cls(self.a, alpha, beta)
		# 	return(new_toy)

		# # Perhaps the 'other' is not an AutoDiffToyObject.
		# # So we'll just add the constant values
		# except:
		# 	try:
		# 		beta = self.beta + other.real
		# 		new_toy = cls(self.a, self.alpha, beta)
		# 		return(new_toy)
		# 	except:
		# 		raise AttributeError(f'{other.__class__.__name__}.{name} is invalid for addition.')

		print(isinstance(self, type(other)))

		return self.__perform_add__(self, other)

	# @classmethod
	# def __perform_addition__(cls, self, other):
	# 	# Assume that both objects are AutoDiffToyObjects
	# 	print("add")
	# 	try:
	# 		alpha = self.alpha + other.alpha
	# 		beta = self.beta + other.beta
	# 		new_toy = cls(self.x_object, alpha=alpha, beta=beta)
	# 		return(new_toy)

	# 	# Perhaps the 'other' is not an AutoDiffToyObject.
	# 	# So we'll just add the constant values
	# 	except:
	# 		try:
	# 			# beta = self.beta + other.real
	# 			# new_toy = cls(self.a, self.alpha, beta)

	# 			self.__radd__(other)
	# 			#return(new_toy)
	# 		except:
	# 			print("oranges")
	# 			raise AttributeError(f'{other.__class__.__name__} is invalid for addition.')


	@classmethod
	def __perform_add__(cls, self, other):
		print("add")
		# Assume that both objects are AutoDiffToyObjects
		# Check if both objects are of the same type
		if isinstance(self, type(other)):
			alpha = self.alpha + other.alpha
			beta = self.beta + other.beta
			new_object = cls(self.x_object, alpha=alpha, beta=beta)
			return(new_object)

		# Perhaps the 'other' is not an AutoDiffToyObject.
		else:
			try:
				return self.__radd__(other)
			except:
				raise AttributeError(f'{other.__class__.__name__} is invalid for addition.')


	def __radd__(self, other):
		'''
		Allows for commuative cases of addition, where a
		float or integer are added to the autodifftoy object.
		'''
		# Assume that both objects are AutoDiffToyObjects
		print("radd")
		# try:
		# 	print("adding")
		# 	alpha = self.alpha + other.alpha
		# 	beta = self.beta + other.beta
		# 	new_toy = cls(self.x_object, alpha=alpha, beta=beta)
		# 	return(new_toy)
		# # Perhaps the 'other' is not an AutoDiffToyObject.
		# # So we'll just add the constant values
		# except:
		# 	try:
		# 		print("adding2")
		# 		alpha = self.alpha
		# 		beta = self.beta + other.real
		# 		new_toy = cls(self.x_object, alpha=alpha, beta=beta)
		# 		return(new_toy)
		# 	except:
		# 		#pass
		# 		raise AttributeError(f'{other.__class__.__name__} is invalid for multiplication.')
		apple = self.__perform_radd__(self, other)
		print("-----")
		print(dir(apple))
		print(apple)
		return(apple)


	@classmethod
	def __perform_radd__(cls, self, other):
		print("add")

		try:
			alpha = self.alpha + other.alpha
			beta = self.beta + other.beta
			new_toy = cls(self.x_object, alpha=alpha, beta=beta)
			return(new_toy)

		# Perhaps the 'other' is not an AutoDiffToyObject.
		# So we'll just add the constant values
		except:
			try:
				print("-=-=-=-=")
				print(self)
				print(other)
				if isinstance(self, cls):
					print("inself")
					alpha = self.alpha
					beta = self.beta + other.real
					new_toy = cls(self.x_object, alpha=alpha, beta=beta)
					print(new_toy)
				elif isinstance(other, cls):
					print("inother")
					alpha = other.alpha
					beta = other.beta + self.real
					new_toy = cls(other.x_object, alpha=alpha, beta=beta)
				else:
					raise AttributeError(f'{other.__class__.__name__} is invalid for multiplication.')
				
				return(new_toy)
			except:
				raise AttributeError(f'{other.__class__.__name__} is invalid for multiplication.')




	# def __mul__(self, other):
	# 	'''
	# 	This allows for multiplication between a coefficient 
	# 	value and a AutoDiffToy object
	# 	'''
	# 	# Multiply a number with a 'x' class
	# 	try:
	# 		alpha = self.alpha * other.real
	# 		new_toy = AutoDiffToy(self.a, alpha, self.beta)
	# 		return(new_toy)

	# 	# Catch weird cases. E.g. when we're multiplying two 'x' classes
	# 	except:
	# 		raise AttributeError(f'{other.__class__.__name__}.{name} is invalid for multiplication.')


	# def __rmul__(self, other):
	# 	'''
	# 	We use rmul as it allows us to deal with commutative case
	# 	in which we have to multiply a float value with a AutoDiffToy
	# 	class, without having to overlaod __mul__ function in the
	# 	float class. (__mul__ function is called from the first variable
	# 	in a multiplication)
	# 	'''
	# 	try:
	# 		alpha = self.alpha * other.real
	# 		new_toy = AutoDiffToy(self.a, alpha, self.beta)
	# 		return(new_toy)
	# 	except:
	# 		raise AttributeError(f'{other.__class__.__name__}.{name} is invalid for multiplication.')


class sin(trigo):
	'''
	E.g.
	f(x) = alpha * sin(x) + beta
	'''
	def calc_function_val(self):
		'''
		Calculate the current value of this
		function at the value of x
		'''
		value = self.alpha * math.sin(self.x_object.val) + self.beta

		return value

	
	def calc_function_derivative_val(self):
		'''
		Calculate the derivative of this function
		at the a value of interest
		'''
		derivative_val = self.alpha * self.x_object.der * math.cos(self.x_object.val)

		return derivative_val


class cos(trigo):
	'''
	E.g.
	f(x) = alpha * cos(x) + beta
	'''
	def calc_function_val(self):
		'''
		Calculate the current value of this
		function at the value of x
		'''
		value = self.alpha * math.cos(self.x_object.val) + self.beta
		return value

	
	def calc_function_derivative_val(self):
		'''
		Calculate the derivative of this function
		at the a value of interest
		'''
		derivative_val = (-1) * self.alpha * self.x_object.der * math.sin(self.x_object.val)

		return derivative_val


class tan(trigo):
	'''
	E.g.
	f(x) = alpha * tan(x) + beta
	'''
	def calc_function_val(self):
		'''
		Calculate the current value of this
		function at the 
		'''
		value = self.alpha * math.cos(self.x_object.val) + self.beta
		return value

	
	def calc_function_derivative_val(self):
		'''
		Calculate the derivative of this function
		at the a value of interest
		'''
		derivative_val = self.alpha * self.x_object.der * (1 / (math.cos(self.x_object.val) ** 2))
		return derivative_val


class exponential(trigo):
	'''
	E.g.
	f(x) = alpha * exp(x) + beta
	'''
	def calc_function_val(self):
		'''
		Calculate the current value of this
		function at the 
		'''
		value = self.alpha * math.exp(self.x_object.val) + self.beta
		return value

	
	def calc_function_derivative_val(self):
		'''
		Calculate the derivative of this function
		at the a value of interest
		'''
		derivative_val = self.alpha * self.x_object.der * math.exp(self.x_object.val)
		return derivative_val



a = 2.0 # Value to evaluate at

alpha = 2.0
beta = 3.0
gamma = 4.0



a = 2.0 # Value to evaluate at
x = AutoDiffToy(a)

alpha = 2.0
beta = 3.0
f = alpha * x + beta

print(f.val, f.der)


x_2 = sin(f)
print(x_2.val, x_2.der)

x_3 = sin(f)


x_4 = x_2 + x_3 + x_2
print(x_4.alpha)
print(x_4.val, x_4.der)

# print("======")
x_5 = (x_4 + 1)
print(x_5)
print(x_5.der)
print(x_5.val, x_5.der)

# x_6 = 1 + x_4
# print(x_6.val, x_6.der)



# x = sin(a=a)
# #f = alpha * x + beta
# f = x + beta
# print(f.val, f.der)


#f = alpha * x + beta
#f = x * alpha + beta

# f = beta + alpha * x 

# f = alpha * x + beta
# print(f.val, f.der)
# print("====================")


# print("Testing: f = alpha * x + beta")
# f_1 = alpha * x + beta
# print(f_1.val, f_1.der)
# print("====================")

# print("Testing: f = x * alpha + beta")
# f_2 = x * alpha + beta
# print(f_2.val, f_2.der)
# print("====================")

# print("Testing: f = beta + alpha * x")
# f_3 = beta + alpha * x
# print(f_3.val, f_3.der)
# print("====================")

# print("Testing: f = beta + x * alpha")
# f_4 = beta + x * alpha
# print(f_4.val, f_4.der)
# print("====================")



