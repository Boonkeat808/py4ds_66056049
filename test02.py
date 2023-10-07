def calculateSum(list_data):
    result = 0
    for number in list_data:
        result = result + number
    return result


def calculateProduct(list_data):
    """

    :param list_data:
    :return:
    """
    result = 1
    for number in list_data:
        result = result * number
    return result

def average(list_data):
    if len(list_data) == 0:
        return None
    result = 0
    for number in list_data:
        result = result + number
    return result/len(list_data)


def median(list_data):
    if len(list_data) == 0:
        return None
    list_data.sort()
    middleNumber=len(list_data) // 2
    if len(list_data) % 2 == 0:
        return(list_data[middleNumber]+list_data[middleNumber-1]) / 2
    else:
        return list_data[middleNumber]


def mode(list_data):
    if len(list_data) == 0:
        return None
    numberCount={}
    mostFreqNumber=None
    mostFreqNumberCount=0

    for number in list_data:
        if number not in numberCount:
            numberCount[number]=0
        numberCount[number]+=1
        if numberCount[number]>mostFreqNumberCount:
            mostFreqNumber=number
            mostFreqNumberCount=numberCount[number]


    return mostFreqNumber



if __name__ == '__main__':
    list_data=([2,4,6,8,10])
    print("SUM:", calculateSum(list_data))
    print("Product:",calculateProduct(list_data))
    print("Average :", median(list_data))
    print("Medianvalue :",median(list_data))
    print("Modevalue :",mode(list_data))











#%%
