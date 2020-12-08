from pathlib import Path


def read_input(input_path: Path):
	numbers = []
	with open(input_path, "r") as input_file:
		for line in input_file.readlines():
			numbers.append(int(line.strip()))
	return numbers


def find_numbers(numbers, goal):
	for index, number in enumerate(numbers):
		if (goal - number) in numbers[index + 1:]:
			return number * (goal - number)
	return 0  # Error code

def find_numbers_task2(numbers, goal):
	for first_index, first in enumerate(numbers):
		for second_index, second in enumerate(numbers[first_index + 1:]):
			if (goal - first - second) in numbers[first_index + second_index + 1:]:
				return first * second * (goal - first - second)
	return  0


def main():
	numbers = read_input(Path("input1.txt"))
	goal = find_numbers_task2(numbers, 2020)
	print(goal)

if __name__ == '__main__':
	main()
