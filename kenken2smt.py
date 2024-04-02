#!/usr/bin/env python3
import sys


class kenken_cell:
  regions = [[]]

  def __init__(self, R, Ro, Rn, val, cur):
    self.R = R  #Region identifier
    self.Ro = Ro  #Operand
    self.Rn = Rn  #Region total
    self.val = val  #Cell value
    self.cur = "V" + str(cur) #Cell ID (ie how many cells existed before it)

    if (R < len(self.regions)):
      self.regions[R].append(self)
    else:
      self.regions.append([self])

  def __str__(self):
    return "R: " + str(self.R) + " Ro: " + str(self.Ro) + " Rn: " + str(
        self.Rn) + "val:" + str(self.val) + " cur: " + str(self.cur) + "\n"


#########################################################################################################


def distinct_rows():
  for x in range(7):
    line = "(assert (distinct "
    for y in range(7):
      line += "V" + str((x * 7) + y) + " "
    line += "))"
    print(line)
  return


def distinct_columns():
  for x in range(7):
    line = "(assert (distinct "
    for y in range(7):
      line += "V" + str((y * 7) + x) + " "
    line += "))"
    print(line)
  return


def rules_for_data():
  for region in kenken_cell.regions[1:]:
    if region[0].Ro == '/' or region[0].Ro == '-':
      line = "(assert (or (= ("
      line += region[0].Ro
      for cell in region:
        line += " " + str(cell.cur)
      line += ") " + str(region[0].Rn) + ") (= ("+region[0].Ro
      
      for cell in reversed(region):
        line += " " + str(cell.cur)
      line += ") " + str(region[0].Rn) + ")))"
      print(line)
    elif region[0].Ro == '=':
      line = "(assert (= "
      line += str(region[0].cur)
      line += " " + str(region[0].Rn) + "))"
    else:
      line = "(assert (= ("
      line += region[0].Ro
      for cell in region:
        line += " " + str(cell.cur)
      line += ") " + str(region[0].Rn) + "))"
      print(line)      
  return


def push_smt_to_file(smt_puzzle, filename):
  try:
    with open(filename, 'w') as file:
      file.write(smt_puzzle)
    print("SMT-LIB puzzle has been written to", filename)
  except IOError:
    print("Error writing SMT-LIB puzzle to file", filename)
  return


def declare_const():
  # print("(set-logic UFNIA)")
  print("(set-option :produce-models true)")
  # print("(set-option :produce-assignments true)")
  for num in range(0, 49):
    print("(declare-const V{0} Int)".format(num))
  for num in range(0, 49):
    print("(assert (and (> V{0} 0) (< V{0} 8)))".format(num))
  return


def create_cell(arg, cur):  #create kenken_cell object for storage
  if '.' in arg:
    parts = arg.split('.')
    R = int(parts[0][1:])

    if parts[1].isdigit():
      Ro = '='
      Rn = int(parts[1])
    else:
      Ro = parts[1][-1]
      Rn = int(parts[1][:-1])

    val = None
  else:
    R = int(arg[1:])
    parent = kenken_cell.regions[R][0]
    Ro = parent.Ro
    Rn = parent.Rn
    val = parent.val
  return kenken_cell(R, Ro, Rn, val, cur)


def wrap_up():
  print("(check-sat)")
  pin = "(get-value (V0"
  for num in range(1, 49):
    pin += " V" + str(num)
  pin += " ))"
  print(pin)
  print("(exit)")
  return


def main(args):  #main
  skip_first_line = True
  cur = 0
  args = ''
  for line in sys.stdin:
    if not skip_first_line: 
      args += line
    skip_first_line = False
    
  args = args.replace('\n', ',')
  arguments = args.split(',')
  arguments = [arg for arg in arguments if arg != '' and arg != '\n']
  cells = []
  for arg in arguments:
    cell = create_cell(arg, cur)
    cur += 1
    cells.append(cell)

  declare_const()
  distinct_rows()
  distinct_columns()
  rules_for_data()
  wrap_up()
  return


if __name__ == "__main__":
  main(sys.argv[1:])
