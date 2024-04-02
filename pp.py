#!/usr/bin/env python3
import subprocess
import sys

solution = False

def make_filename_list(arg):
  global solution
  arg = arg.replace("-",".")
  lis = arg.split(".")
  if len(lis)>1 and "solution" in lis[1]:
    solution=True
  return lis[0]

def split_json(json_string):
  if "\\\\r\\\\n" in str(json_string):
    json_string=str(json_string).replace("\\\\r\\\\n","L")
  else:
    json_string=str(json_string).replace("\\r\\n","L")
  string_list = []
  list_list=[]
  
  start = json_string.find("A")
  end = json_string.find("LT")
  string_list.append(json_string[start+2:end])
  
  start = json_string.find("T")
  end = json_string.find("LS")
  string_list.append(json_string[start+2:end])

  start = json_string.find("S")
  end = json_string.find("LV")
  string_list.append(json_string[start+2:end])

  start = json_string.find("V")
  end = json_string.find("LH")
  string_list.append(json_string[start+2:end])

  start = json_string.find("H")
  end = json_string.find("LL")
  string_list.append(json_string[start+2:end])

  for string in string_list:
    new_string=" ".join(string.split())
    num = ""
    cur = [[] for i in range(7)]
    row = 0
    for char in new_string:
      if char == " " or char == "L":
        if num == "+" or num == "-" or num == "*" or num == "/":
          cur[row].append(num)
        elif num != "":
          cur[row].append(int(num))
        if char == "L":
            row +=1
        num = ""
      else:
        num += char
    if num == "+" or num == "-" or num == "*" or num == "/":
      cur[row].append(num)
    elif num != "":
      cur[row].append(int(num))
    list_list.append(cur)
  
  return list_list

def format_json_data(json_data):
  for i in range(len(json_data[1])):
    json_data[1][i] = [p if p != 0 else '' for p in json_data[1][i]]
  for i in range(len(json_data[2])):
    json_data[2][i] = [p if p != 0 and p!=1 else '' for p in json_data[2][i]]
  for i in range(len(json_data[3])):
    json_data[3][i] = ['ǁ' if p != 0 else '|' for p in json_data[3][i]]
  for i in range(len(json_data[4])):
    json_data[4][i] = ['=' if p != 0 else '-' for p in json_data[4][i]]
  return json_data

def pretty_print(json_data):
  vert_bold = "ǁ"
  global solution
  print('='*57)
  for i in range(7):
    cur = vert_bold
    for j in range(6):
      cur+=str(json_data[1][i][j])
      cur+=str(json_data[2][i][j])
      cur+=" "* (7-len(str(json_data[1][i][j]))-len(str(json_data[2][i][j])))
      cur+=str(json_data[3][i][j])
    cur+=str(json_data[1][i][6])
    cur+=str(json_data[2][i][6])
    cur+=" "* (7-len(str(json_data[1][i][6]))-len(str(json_data[2][i][6])))
    cur+=vert_bold
    print(cur)
    cur=vert_bold
    for j in range(6):
      cur+=" "*3
      if solution:
        cur+=str(json_data[0][i][j])
      else:
        cur+=" "
      cur+=" "*3
      cur+=json_data[3][i][j]
    cur+=" "*3
    if solution:
      cur+=str(json_data[0][i][6])
    else:
      cur+=" "
    cur+=" "*3
    cur+=vert_bold
    print(cur)
    cur = vert_bold
    for j in range(6):
      cur+=" "*7
      cur+=json_data[3][i][j]
    cur += " "*7+vert_bold
    print(cur)
    cur = vert_bold
    if i<6:
      for j in range(7):
        cur+=json_data[4][j][i]*7
        if j <6:
          cur+=json_data[3][i][j]
      cur+=vert_bold
      print(cur)
  print("="*57)
  return

def main():
  arg = sys.argv[1]
  num_and_type = make_filename_list(arg)
  json_string = subprocess.check_output("./fetch.sh {0}".format(num_and_type),stderr=subprocess.STDOUT,shell=True)
  json_data = format_json_data(split_json(json_string))
  pretty_print(json_data)
  return
  
if __name__ == "__main__":
  main()