def load(location):
    if location.split(".")[len(location.split("."))-1]=="lrc":
        hh_list = []
        mm_list = []
        ss_list = []
        mms_list = []
        content_list = []
        file = open(location,"r",encoding="utf-8")
        sub = file.readlines()
        sub[0]=sub[0][2:len(sub[0])+1]
        file.close()
        for n in sub:
            n = n.strip(" ")
            n = n.strip("[")
            content = n.split("]")[1]
            time = n.split("]")[0]
            hh_list.append(str(int(time.split(':')[0])//60).rjust(2,'0'))
            mm_list.append(str(int(time.split(':')[0])%60).rjust(2,'0'))
            ss_list.append(str(time.split(':')[1].split('.')[0]).rjust(2,'0'))
            mms_list.append(str(time.split(':')[1].split('.')[1]).ljust(3,'0'))
            content_list.append(content)
        finallist = [hh_list,ss_list,mms_list,content_list]
        return(finallist)
    
    
    if location.split(".")[len(location.split("."))-1]=="srt":
        hh_list = []
        mm_list = []
        ss_list = []
        mms_list = []
        content_list = []
        file = open(location,"r",encoding="utf-8")
        sub = file.readlines()
        sub[0]=str(0)
        file.close()
        a= 0
        for n in sub:
            n=n.strip('\n')
            print (n)
            if n.isdecimal() :
                print ("uuuuu")
                time = sub[int(n)+1].split(' --> ')[0]
                hh = str((time.split(':')[0]))
                print (time)
                print(n)
                mm = str((time.split(':')[1]))
                ss = str(time.split(',')[0].split(':')[2])
                mms =  str(time.split(',')[1])
                content = sub[a+2]
                mm_list.append(mm)
                ss_list.append(ss)
                mms_list.append(mms)
                content_list.append(content)
        a +=1
        print(a)
    finallist = [hh_list,ss_list,mms_list,content_list]
    return(finallist)
print(load("test2.srt"))
