import json
def print_json(my_dict):
	json_str = json.dumps(my_dict, indent = 4)
	print(json_str)

def main():
  try:
    loc = input("Enter the path of the file : - ")
    with open(loc) as js_fl:
	     data = json.load(js_fl)
  except Exception as e:
    print("Please input correct file path next time :(")
    print(e)
  else:
    print_json(data)

main()

	

