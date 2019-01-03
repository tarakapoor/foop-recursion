#folder = input("Folder of files to analyze ")
#showsteps = input("Would you like to use showsteps? ")
#search = input("What value would you like to search for?")
#files = input("Enter the files you would like to analyze separated by commas ")


import configparser
from configparser import ConfigParser

parser = ConfigParser()
parser.read('config.txt')

#config = ConfigParser.ConfigParser()
#config.readfp(open(r'config.txt'))
file = parser.get('options', 'file')
method = parser.get('options', 'mode')
value = int(parser.get('options', 'search'))
sort = parser.get('options', 'sort')
showsteps = parser.get('options', 'showsteps')
print("file:", file)
print("method:", method)
print("search for:", value)
print("sort:", sort)
print("showsteps:", showsteps)


filelist = []
with open(file) as f:
    for line in f:
        data = line.split()
        filelist.append(int(data[0]))


#text = open(file,'r').read()
#text = text.lower()
#for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
#    text = text.replace(ch, ' ')
#    filelist = text.split()

#for i in range(len(filelist)):
#    filelist[i] = int(filelist[i])


#works
def linsearch(x, nums):
    count = 1
    for i in range(len(nums)):
        if showsteps == 'yes':
            print("comparing", nums[i], "to", x)
        if nums[i] == x:
            print("found in", count, "search steps")
            return i
        count += 1
    return -1

#works
def linbin(x, nums):
    count = 1
    low = 0
    high = len(nums) - 1
    #print("low high")
    #print (low, high)
    while low <= high:
        mid = (low + high)//2
        item = nums[mid]

        if showsteps == 'yes':
            print("comparing", item, "to", x)
        #print("item: ", item)
        if x == item:
            print ("found in", count, "search steps")
            return mid
        elif x < item:
            count += 1
            high = mid - 1
            #print ("high:", high)
        elif x > item:
            count += 1
            low = mid + 1
            #print ("low:", low)
    return -1

countrecbin = 1
#works
def recbin(x, nums, low, high):
    global countrecbin
    if low > high:
        return -1
    mid = (low + high) // 2
    item = nums[mid]
    if showsteps == 'yes':
        print("comparing", item, "to", x)
    if item == x:
        print ("found in", countrecbin, "search steps")
        return mid
    elif x < item:
        countrecbin += 1
        return recbin(x, nums, low, mid-1)
    else:
        countrecbin += 1
        return recbin(x, nums, mid+1, high)


#sorting function if sort == "simple"
def simplesort(numlist):
    n = len(numlist)
    for bottom in range(n-1):
        mp = bottom
        for i in range(bottom+1, n):
            if numlist[i] < numlist[mp]:
                mp = i
        numlist[bottom], numlist[mp] = numlist[mp], numlist[bottom]

#sorting if sort == "merge"
def merge(lst1, lst2, lst3):
#merge sorted lists lst1 and lst1 into lst3
    #these indexes keep track of current position in each list
    i1, i2, i3 = 0, 0, 0

    n1, n2 = len(lst1), len(lst2)

    #loop while both lst1 and lst2 have more items
    while i1 < n1 and i2 < n2:
        if lst1[i1] < lst2[i2]: #top of lst1 is smaller
            lst3[i3] = lst1[i1] #copy it into current spot in lst3
            i1 += 1

        else: #top of lst2 is smaller
            lst3[i3] = lst2[i2] #copy it into current spot in lst3
            i2 += 1
        i3 += 1

    #now either lst1 or lst2 is done. one of the following loops will execute to finish the merge

    #copy remaining items (if any) from lst1
    while i1 < n1:
        lst3[i3] = lst1[i1]
        i1 += 1
        i3 += 1
    while i2 < n2:
        lst3[i3] = lst2[i2]
        i2 += 1
        i3 += 1

    return lst3

def mergeSort(nums):
    #put items in ascending order
    n = len(nums)
    if n > 1:
        m = n // 2
        nums1, nums2 = nums[:m], nums[m:]
        
        mergeSort(nums1)
        mergeSort(nums2)

        numlist = merge(nums1, nums2, nums)
        return numlist


if sort == "simple":
    #simplesort(filelist)
    filelist.sort(key=int)
if sort == "merge":
    mergeSort(filelist)
print("filelist:", filelist)
if sort == "none":
    print("")


if method == "linear simple":
    print(linsearch(value, filelist))
elif method == "linear binary":
    print(linbin(value, filelist))
elif method == "binary recursive":
    print(recbin(value, filelist, 0, len(filelist)-1))


