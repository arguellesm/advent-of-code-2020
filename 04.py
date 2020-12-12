# Advent of Code 2020, Day 4
# https://adventofcode.com/2020/day/4

from re import split, search, ASCII


def main():

	file    = open('inputs/04_input.txt', encoding='utf-8')
	content = file.read()
	file.close()

	# Part one

	passports = content.split('\n\n')
	required  = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
	n_valid   = 0
	valid_p   = []

	for passport in passports:		
		if all(field in passport for field in required):
			n_valid += 1
			valid_p.append(passport)			
	print(n_valid)

	
	# Part two

	n_valid   = 0
	eyecolors = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')

	for passport in valid_p:
		valid_height = False
		
		fields = split(r'[ \n]', passport)
		fields.sort()
		if 'cid' in fields[1]:
			fields.remove(fields[1])

		# Birth year
		if fields[0][4:] and int(fields[0][4:]) in range(1920,2003):
			# Eye color
			if fields[1][4:] in eyecolors:
				# Expiration year
				if fields[2][4:] and int(fields[2][4:]) in range(2020,2031):
					# Hair color
					if len(fields[3][4:])==7 and search('#\w', fields[3][4:], ASCII) is not None:
						# Height
						if 'cm' in fields[4][4:] and fields[4][4:7].isnumeric():
							if int(fields[4][4:7]) in range(150,194):
								valid_height = True
						elif 'in' in fields[4][4:] and fields[4][4:6].isnumeric():
							if int(fields[4][4:6]) in range(59,77):
								valid_height = True
						if valid_height is True:
							# Issue year
							if fields[5][4:] and int(fields[5][4:]) in range(2010,2021):
								# Passport ID
								if fields[6][4:].isnumeric() and len(fields[6][4:])==9:
									n_valid += 1
								
	print(n_valid)




if __name__ == '__main__':
	main()