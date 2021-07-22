import os
def convert(source_file_location,destination_file_location):
    try:
        os.remove(destination_file_location)
    except:
        pass
    hh_list = []
    mm_list = []
    ss_list = []
    mms_list = []
    content_list = []
    file = open(source_file_location,"r",encoding="utf-8")
    sub2 = open(destination_file_location,"a",encoding="utf-8")
    sub = file.readlines()
    sub[0]=str(0)
    file.close
    a= 0
    for n in sub:
        n=n.strip('\n')
        if n.isdecimal() :
            time = sub[a+1].split(' --> ')[0]
            mm = str(int(time.split(':')[0])*60+int((time.split(':')[1])))
            ss = str(time.split(',')[0].split(':')[2])
            mms =  str(time.split(',')[1])
            content = sub[a+2]
            mm_list.append(mm)
            ss_list.append(ss)
            mms_list.append(mms)
            content_list.append(content)
        a +=1
    for a in range(len(mm_list)-1):
        sub2.write('['+mm_list[a]+':'+ss_list[a]+'.'+mms_list[a]+']'+content_list[a]
    sub2.close










    
        
