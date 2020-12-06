# Advent of Code 2020, Day 1 
# https://adventofcode.com/2020/day/1

from numpy import array, loadtxt


def main():

	input = loadtxt('inputs/01_input.txt', dtype=int)
	print(find_three(input))

	
def find_three(input):
	for i in input:
		for j in input:
			for k in input:
				if i+j+k==2020:
					return i*j*k


if __name__ == "__main__":
    main()
