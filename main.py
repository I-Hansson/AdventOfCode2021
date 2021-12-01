
def aoe():
    x = 0;

    with open("input.txt", "r") as f:
        temp = f.read().splitlines()
        print(temp)
        listOfValues = [];
    for i in range(len(temp)):
        temp1 = int(temp[i]);
        listOfValues.append(temp1);

    ###  Part 1 ####
    # print(listOfValues)
    # for i in range(len(listOfValues)):
    #      if (i == 0):
    #          continue;
    #      elif (listOfValues[i] > listOfValues[i-1]):
    #
    #         x = x + 1;
    #
    ####  Part 2 ####
    # print(listOfValues);
    # for i in range(len(listOfValues)):
    #     try:
    #         temp1 = listOfValues[i]+listOfValues[i+1]+listOfValues[i+2];
    #         temp2 = listOfValues[i+1]+listOfValues[i+2]+listOfValues[i+3];
    #     except Exception:
    #         print(x)
    #
    #     if temp2 > temp1:
    #         x +=1;

if __name__ == "__main__":
   aoe()