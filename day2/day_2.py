
def aoe():
    with open("input.txt", "r") as f:
        temp = f.read().splitlines()
        print(temp)
    deph = 0
    forward = 0
    aim = 0

    ### Part 1 ###
    # for i in range(len(temp)):
    #     tempString = temp[i]
    #     if tempString[0] == 'f':
    #         forward +=int(tempString[-1])
    #     elif tempString[0] == 'd':
    #         deph +=int(tempString[-1])
    #     elif tempString[0] == 'u':
    #         deph -=int(tempString[-1])
    # print(deph*forward)


    ###### Part 2 ####
    # for i in range(len(temp)):
    #     tempString = temp[i]
    #     if tempString[0] == 'f':
    #         forward +=int(tempString[-1])
    #         deph = deph+  int(tempString[-1])*aim
    #     elif tempString[0] == 'd':
    #         aim +=int(tempString[-1])
    #     elif tempString[0] == 'u':
    #         aim -=int(tempString[-1])
    # print(deph*forward)

if __name__ == "__main__":
        aoe()