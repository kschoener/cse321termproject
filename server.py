import sys
import os
import time
import subprocess
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def main():
    ret = subprocess.Popen(["ip", "route", "get", "8.8.8.8"], stdout=subprocess.PIPE)# | awk '{print $NF; exit}'"], stdout=subprocess.PIPE)
    out = ret.stdout.read().decode("utf-8").strip().split("\n") #converts from bytes to str
    print(out)
    myip = str(out[0][out[0].strip().find("src ")+4:].strip())
    print("Supposedly my IP Address: "+myip)

    pics = None
    if(len(sys.argv) > 1):
        picsDir = sys.argv[1] #path to the directory of all the pictures
        pics = updatePics(picsDir) #gets all the pictures from the directory

    mpl.rcParams['toolbar'] = 'None' #hides the matplotlib menu
    # plt.axis('off') #disables axis
    # plt.gcf().canvas.set_window_title(myip)

    fig = plt.figure(facecolor='black')
    fig.canvas.set_window_title(myip)
    plt.axis('off')
    plt.ion() #allows for changes at runtime

    firstTime = True
    index = 0

    while pics != None:
        if(index >= len(pics)):
            index = 0
            pics = updatePics(picsDir)
        #endif

        print("Picture path is: "+str(os.path.join(picsDir, pics[index])))
        plt.clf()
        plt.imshow(mpimg.imread(str(os.path.join(picsDir, pics[index]))))
        plt.pause(4)
        if(firstTime):
            firstTime = False
            plt.show()
        #endif
        index += 1
        time.sleep(5)
    #endwhile
#enddef main


def updatePics(path):
    pics = []
    for filename in os.listdir(path):
        if os.path.isfile(os.path.join(path, filename)) and (filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg') or filename.lower().endswith('.png')):
            pics.append(filename)
        #endif
    #endfor
    return pics
#enddef updatePics








































if __name__ == '__main__':
    main()
