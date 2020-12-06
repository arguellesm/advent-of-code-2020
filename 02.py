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
		min, max, letter, pasw = split(r'[-: ]+', line)

		if pasw.count(letter) in range(int(min),int(max)+1):
			num_valid += 1

	return num_valid


def part_two(lines):

	num_valid = 0

	for line in lines:
		pos1, pos2, letter, pasw = split(r'[-: ]+', line)
		
		con1 = pasw[int(pos1)-1] == letter
		con2 = pasw[int(pos2)-1] == letter

		if (con1 and not con2) or (not con1 and con2):
			num_valid += 1

	return num_valid


if __name__ == "__main__":
    main()
