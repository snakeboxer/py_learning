import time
import random
#简单测试
def test(num):
  i = 0
  while i < 10:
    print("-----%d-----"%i)
    i+=1
    time.sleep(1)
    
def main():
  test(random.randint(0,10))
  
if __name__ == "__main__":
  main()
