import sys
import os
import subprocess





def main():
    print("\n\nSubprocess arp call:\n")
    ret = subprocess.Popen(["arp","-a"], stdout=subprocess.PIPE)
    out = ret.stdout.read().decode("utf-8") #converts from bytes to str
    print(out)

    ips = []
    for line in out.split("\n")[:-1]:
        # ip = line[(line.find("(")+1):(line.find(")"))]
        lineSplit = line.strip().split(' ')
        print(str(lineSplit))
        print(str(line))
        ip = lineSplit[1][1:-1] # "(xxx.xxx.xxx)"
        mac = lineSplit[3]
        ips.append((ip, mac))
    #endfor
    print("\n\nIps and Macs are: ")
    print(str(ips))

    for tup in ips:
        pingCount = 5
        ret = subprocess.Popen(["ping",tup[0], "-c", str(pingCount)], stdout=subprocess.PIPE)
        out = ret.stdout.read().decode("utf-8").split("\n") #converts from bytes to str
        mean = []
        for i in range(1,pingCount+1):
            try:
                timeTaken = float(out[i].strip().split(' ')[-2])
                print("\tTime = "+str(timeTaken))
                mean.append(timeTaken)
            except:
                print("packet lost: "+out[i])
            #end try
        #endfor
        try:
            print("Average time taken = "+str(sum(mean)/len(mean)))
        except:
            print("There was an error getting average time, here is output: "+str(out))
    #endfor

    # ip route get 8.8.8.8 | awk '{print $NF; exit}' --> this prints out your local IP address
    # ret = subprocess.Popen(["ip", "route", "get", "8.8.8.8", "|", "awk", "'{print", "$NF;", "exit}'"], stdout=subprocess.PIPE)
    # ret = subprocess.Popen(["ip", "route", "get", "8.8.8.8"], stdout=subprocess.PIPE)# | awk '{print $NF; exit}'"], stdout=subprocess.PIPE)
    # out = ret.stdout.read().decode("utf-8").strip().split("\n") #converts from bytes to str
    # print(out)
    # print("index of 'src ' is: "+str(out[0].find("src ")))
    # print("Supposedly my IP Address: "+str(out[0][out[0].strip().find("src ")+4:]))


    # print("\n\nSubprocess ping router call:\n")
    # ret = subprocess.Popen(["ping","192.168.0.1", "-c", "5"], stdout=subprocess.PIPE)
    # print(ret.stdout.read().decode("utf-8")) #converts from bytes to str

    # print("\n\nos.system:\n")
    # os.system("arp -a")

    # print("\n\nSubprocess netstat call:\n")
    # ret = subprocess.Popen(["netstat","-s"], stdout=subprocess.PIPE)
    # print(ret.stdout.read().decode("utf-8")) #converts from bytes to str
#enddef main











































if __name__ == '__main__':
    main()
