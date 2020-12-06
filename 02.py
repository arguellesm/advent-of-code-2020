# Advent of Code 2020, Day 2
# https://adventofcode.com/2020/day/2

from re import split


def main():

	file  = open('inputs/02_input.txt', encoding='utf-8')
	lines = file.readlines()
	file.close()

	print(part_one(lines))
	print(part_two(lines))


def part_one(lines):

	num_valid = 0

	for line in lines:
		parsed = split(r'[-: ]+', line)

		min  = int(parsed[0])
		max  = int(parsed[1])+1 

		if parsed[3].count(parsed[2]) in range(min,max):
			num_valid += 1

	return num_valid


def part_two(lines):

	num_valid = 0

	for line in lines:
		parsed = split(r'[-: ]+', line)

		pos1 = int(parsed[0])-1
		pos2 = int(parsed[1])-1
		pasw = parsed[3]
		
		con1 = pasw[pos1] == parsed[2]
		con2 = pasw[pos2] == parsed[2]

		if (con1 and not con2) or (not con1 and con2):
			num_valid += 1

	return num_valid


if __name__ == "__main__":
    main()
