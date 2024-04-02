#!/usr/bin/env python3
import sys


def remove_brackets(output):

  # find first and last '(' and ')'
  first_open_bracket = output.find('(')
  first_closed_bracket = output.rfind(')')

  # find ";; statistics", ignores that line and everything below
  stats_index = output.find(';; statistics')
  if stats_index != -1:
    first_closed_bracket = stats_index

  # extract the inner content substring, splits it, strip whitespace and any empty lines
  if first_open_bracket != -1 and first_closed_bracket != -1:
    main_content = output[first_open_bracket + 1:first_closed_bracket].strip()
    main_lines = main_content.split('\n')
    main_lines = [line.strip() for line in main_lines if line.strip()]
    return main_lines

  else:
    return None


def parse_results(puzzle):

  solution = remove_brackets(puzzle)

  if solution is not None:

    # initialize a library to store the inputs in, parse the results and add them to a dictionary
    solutions = {}
    for line in solution:

      parts = line.split()

      if len(parts) == 1 and parts[0] in ['(', ')']:
        continue

      if len(parts) == 2:

        # extract variable name ("vx" where x = 0, 1, 2, ..., 48), remove parentheses
        variable = parts[0]
        variable = variable.replace('(', '').replace(')', '')

        # extract value (the value associated with "vx", ranging from 1 to 7), remove parentheses
        value = parts[1]
        value = value.replace('(', '').replace(')', '')

        # convert value to integer and add it to the dictionary
        solutions[variable] = int(value)

      else:
        print("Error: Unexpected format in line '{}'".format(line))
        continue

    # print the values in the solutions dictionary (the puzzle solution) to stdout
    for value in solutions.values():
      print(value, end='')

  else:
    return None


def main():

  first_line = input().strip()

  # if the puzzle is solvable
  if first_line == "sat" or first_line == "Sat":
    print("Puzzle is solvable.")
    puzzle_content = sys.stdin.read().strip()
    parse_results(puzzle_content)

  # if puzzle is not solvable
  elif first_line == "unsat" or first_line == "Unsat":

    print("Puzzle not solvable.")
    sys.exit(1)


if __name__ == "__main__":
  main()
