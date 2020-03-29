import os
def getplacename(fname):
    return fname.split("_")[1]
def getfileformate(fname):
    return fname.split(".")[-1]
def makeplacedir(places):
    for place in places:
        os.mkdir(place)

def organize_photos(dir):
    os.chdir(dir)
    print(os.getcwd())
    places =[]
    all_list = os.listdir(dir)
    for fname in all_list:
        if getplacename(fname) not in places:
            places.append(getplacename(fname))
    print(places)
    makeplacedir(places)

    for fname in all_list:
        place = getplacename(fname)
        os.rename(fname,os.path.join(place,fname))
        #print(os.path.join(place,fname))
def organize_formates(dir):
    os.chdir(dir)
    print(os.getcwd())
    places =[]
    all_list = os.listdir(dir)
    for fname in all_list:
        if getfileformate(fname) not in places and getfileformate(fname) not in all_list:
            places.append(getfileformate(fname))
    print(places)
    #exit()
    makeplacedir(places)

    for fname in all_list:
        if fname.count(".") ==0:
            continue
        else:
            place = getfileformate(fname)
            os.rename(fname,os.path.join(place,fname))
            #print(os.path.join(place,fname))
#organize_photos("C:/Users/Admin/Desktop/photos")
organize_formates("C:/Users/Admin/Downloads")