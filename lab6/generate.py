
import random
import sys




def random_data(size):
  """<Write what this function does here>
  """
  #for i in range(size):
  #  rand = random.randint(0,255)
  #  sys.stdout.write(chr(rand))
  numbers = [random.randint(0,255) for x in range(size)]
  for i in numbers:
    sys.stdout.write(chr(i))
def perfect_eight():
  """<Write what this function does here>
  """
  i=0
  while(i<255):
    rand = chr(i)  #Generate each ASCII code only one time and convert it to a string
    sys.stdout.write(rand) 
    i+=1 



# the following code is provided to you for free
if __name__ == "__main__":
  try:
    which = sys.argv[1]
    if which == "random":
      size = int(sys.argv[2])
      random_data(size)
    elif which == "perfect":
      perfect_eight()
    else:
      raise IndexError("invalid option")
  except IndexError as e:
    usage_str = "Usage:\n"                 \
                "\tpython3 {prog} random <size>\n" \
                "\tpython3 {prog} perfect\n"
    sys.stderr.write(usage_str.format(prog=sys.argv[0]))
    sys.exit(1)




