import random

def primary():
  print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = len(quotes) - 1
  rnd = random.randint(0, last)
  print(len(quotes), quotes)
  print(quotes[rnd].replace("\n",""))
  print(quotes[len(quotes)-1].replace("\n",""))

if __name__== "__main__":
  primary()
