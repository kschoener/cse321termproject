import sys
import os
import time
import subprocess
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def main():
    ret = subprocess.Popen(["ip", "route", "get", "8.8.8.8"], stdout=subprocess.PIPE)# | awk '{print $NF; exit}'"], stdout=subprocess.PIPE)
    out = ret.stdout.read().decode("utf-8").strip().split("\n") #converts from bytes to str
    print(out)
    myip = str(out[0][out[0].strip().find("src ")+4:].strip())
    print("Supposedly my IP Address: "+myip)

    picsDir = sys.argv[1] #path to the directory of all the pictures
    pics = updatePics(picsDir) #gets all the pictures from the directory

    mpl.rcParams['toolbar'] = 'None' #hides the matplotlib menu
    plt.axis('off') #disables axis
    plt.gcf().canvas.set_window_title(myip)
    plt.ion() #allows for changes at runtime
    plt.imshow(mpimg.imread("testImages/goog.png"))
    plt.show()
    start = time.time()
    while(time.time() < start + 10):
        pass
    # time.sleep(5)
    # print("hopefully showing DSC")
    # plt.clf()
    # plt.imshow(mpimg.imread("testImages/DSC_0008.JPG"))
    start = time.time()
    while(time.time() < start + 10):
        pass
    # time.sleep(5)
    # print("hopefully showing image2")
    # plt.imshow(mpimg.imread("testImages/image2.png"))
    time.sleep(5)

    index = 0
    imPlt = None
    while False:
        if(index >= len(pics)):
            index = 0
            pics = updatePics(picsDir)
        #endif

        print("Picture path is: "+str(os.path.join(picsDir, pics[index])))
        plt.imshow(mpimg.imread(str(os.path.join(picsDir, pics[index]))))
        # plt.show()
        # if(imPlt == None):
        #     img = mpimg.imread(str(os.path.join(picsDir, pics[index])))
        #     imPlt = plt.imshow(img)
        #     plt.draw()
        # else:
        #     imPlt.set_data(mpimg.imread(str(os.path.join(picsDir, pics[index]))))

        # plt.draw()

        # img = mpimg.imread(str(os.path.join(picsDir, pics[index])))
        # plt.imshow(img)
        # plt.draw()

        time.sleep(10)
        # start = time.time()
        # while(time.time() < start + 10):
        #     pass
        # print("Its's been 5 seconds, time to switch pics")
        index += 1
    #endwhile
#enddef main


def updatePics(path):
    pics = []
    for filename in os.listdir(path):
        # print(filename)
        if os.path.isfile(os.path.join(path, filename)) and (filename.lower().endswith('jpg') or filename.lower().endswith('jpeg') or filename.lower().endswith('png')):
            # print("that was a file!")
            # print(filename + " was added!")
            pics.append(filename)
        #endif
    #endfor
    return pics
#enddef updatePics








































if __name__ == '__main__':
    main()
