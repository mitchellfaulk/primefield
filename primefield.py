class Element:
	def __init__(self, value, characteristic):
		self.characteristic = characteristic
		self.value = value % self.characteristic

	def __repr__(self):
		return f"Element(value={self.value}, characteristic={self.characteristic})"

	def __str__(self):
		return f"[{self.value}]_{self.characteristic}"

	# Define an __add__ method to use + to add
	def __add__(self, other):
		if not isinstance(other, Element):
			return NotImplemented

		if self.characteristic != other.characteristic:
			raise TypeError('Addition not supported between elements of fields of different characteristics')

		value = (self.value + other.value) % self.characteristic
		return Element(value, self.characteristic)

	# Define a __sub__ method to use - to subtract
	def __sub__(self, other):
		if not isinstance(other, Element):
			return NotImplemented

		if self.characteristic != other.characteristic:
			raise TypeError('Addition not supported between elements of fields of different characteristics')

		value = (self.value - other.value) % self.characteristic
		return Element(value, self.characteristic)

	# Define a __mul__ method to use * to multiply
	def __mul__(self, other):
		if not isinstance(other, Element):
			return NotImplemented

		if self.characteristic != other.characteristic:
			raise TypeError('Multiplication not supported between elements of fields of different cahracteristics')

		value = (self.value * other.value) % self.characteristic
		return Element(value, self.characteristic)

	# Define a __pow__ method to use ** for exponents
	def __pow__(self, power):
		if not isinstance(power, int):
			return NotImplemented

		elif self.value == 0:
			return self

		elif power == 0:
			return Element(1, self.characteristic)

		else:
			res = self
			for i in range(abs(power) - 1):
				res *= self
			if power > 0:
				return res
			else:
				return ~res

	# Define an inverse of every nonzero element, accessed by ~ in front of the element
	def __invert__(self):
		if self.value == 0:
			raise ZeroDivisionError('Zero has no inverse')

		for i in range(1, self.characteristic):
			if i * self.value % self.characteristic == 1:
				return Element(i, self.characteristic)


	# Define a __truediv__ method to use / to divide
	def __truediv__(self, other):
		if not isinstance(other, Element):
			return NotImplemented

		if self.characteristic != other.characteristic:
			raise TypeError('Multiplication not supported between elements of fields of different cahracteristics')

		if other.value == 0:
			raise ZeroDivisionError('Cannot divide by zero')

		return self * (~other)

	def __div__(self, other):
		return self/other
			
	# Define an equality method so we can use == to compare instances accurately
	def __eq__(self, other):
		if not isinstance(other, Element):
			return NotImplemented

		return self.value == other.value and self.characteristic == other.characteristic

	# Make the class hashable so that its instances can be used, e.g., as keys of dictionaries or elements of sets
	def __hash__(self):
		return hash((self.value, self.characteristic))



def is_prime(num):
	if not isinstance(num, int) or num <= 1:
		return False

	prime_flag = True

	for i in range(2, int(num ** (.5)) + 1):
		if (num % i) == 0:
			prime_flag = False
			break

	return prime_flag



class PrimeField:
	def __init__(self, characteristic):
		if not is_prime(characteristic):
			raise ValueError('Expected characteristic to be a prime number.')
		self.characteristic = characteristic
		self.elements = frozenset(Element(i, characteristic) for i in range(characteristic))

	def __repr__(self):
		return f"PrimeField(characteristic={self.characteristic})"

	def __str__(self):
		return f"Z/{self.characteristic}Z"

	def __eq__(self, other): 
		if not isinstance(other, PrimeField):
			return NotImplemented

		return self.characteristic == other.characteristic 

	def __getitem__(self, value):
		if not isinstance(value, int):
			typ = type(value)
			raise ValueError(f"Elements of a field are represented by integers, not {typ}") 

		return Element(value, self.characteristic)

	def __len__(self):
		return self.characteristic


