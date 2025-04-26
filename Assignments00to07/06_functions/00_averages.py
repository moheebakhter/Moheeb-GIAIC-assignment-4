def average(a: float, b:float):

    sum = a + b
    return sum/2

   

def main():

    averg1 = average(0,10)
    averg2 = average(8,10)


    final = average(averg1, averg2)
    print("averg1", averg1)
    print("averg2", averg2)
    print("final", final)

if __name__ == "__main__":
      main()  