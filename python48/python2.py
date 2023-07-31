aList = [12, 34, 56, 78, 98, 22, 45, 13]
def recursiveBinarySearch(aList, target, index):
    aList = sorted(aList)
    
    if len(aList) == 0:
        return False
    else:
        midpoint = len(aList) // 2
        print(midpoint)
        if aList[midpoint] == target:
            return aList.index(target)
        else:
            if target < aList[midpoint]:
                print("this is", aList[:midpoint])
                return recursiveBinarySearch(aList[:midpoint],target, index)
            else:
                 print("this is", aList[:midpoint])
                 return recursiveBinarySearch(aList[midpoint:],target, index + midpoint)
                

print(recursiveBinarySearch(aList,98,0), sorted(aList))
