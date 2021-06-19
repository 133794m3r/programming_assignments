class RomanNumerals:
	def to_roman(number: int) -> str:
		roman = { 'M':1000,'CM':900,'D':500,'CD': 400, 'C': 100, 'XC': 90, 'L': 50,
			'XL': 40, 'X': 10, 'IX': 9, 'V': 5,'IV': 4, 'I': 1}
		output = ''
		for k,v in roman.items():
			numerals, number = divmod(number,v)
			output += k*numerals
		return output

	def from_roman(numerals:str) -> int:
		import re
		roman = { 'M':1000,'CM':900,'D':500,'CD': 400, 'C': 100, 'XC': 90, 'L': 50,
			'XL': 40, 'X': 10, 'IX': 9, 'V': 5,'IV': 4, 'I': 1}
		out = 0
		pattern = re.compile(r'[MDLV]|C[MD]?|X[CL]?|I[XV]?')
		"""
		"""

		for numeral in pattern.findall(numerals):
			out += roman[numeral]
		return out

print(to_roman(1666))
print(from_roman('MDCLXVI'))