# Advent of Code 2020, Day 3
# https://adventofcode.com/2020/day/3


def main():
	
	file  = open('inputs/03_input.txt', encoding='utf-8')
	global lines
	lines = file.readlines()
	file.close()

	# Part one
	print(trees(3,1))
	# Part two
	print(trees(1,1)*trees(3,1)*trees(5,1)*trees(7,1)*trees(1,2))


def trees(right, down):

	slope    = (right, down)
	rows	 = len(lines)
	columns  = len(lines[0])
	column   = 0
	trees 	 = 0

	for row in range(slope[1],rows, slope[1]):	
		column = (column+slope[0])%(columns-1)
		if lines[row][column] == '#':
			trees += 1

	return trees


if __name__ == '__main__':
	main()