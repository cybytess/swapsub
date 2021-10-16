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
    sub[0]=sub[0][2:len(sub[0])+1]
    sub.append(sub[len(sub)-1])
    file.close()
    for n in sub:
        n = n.strip(' ')
        n = n.strip("[")
        content = n.split("]")[1]
        time = n.split("]")[0]
        hh_list.append(str(int(time.split(':')[0])//60).rjust(2,'0'))
        mm_list.append(str(int(time.split(':')[0])%60).rjust(2,'0'))
        ss_list.append(str(time.split(':')[1].split('.')[0]).rjust(2,'0'))
        mms_list.append(str(time.split(':')[1].split('.')[1]).ljust(3,'0'))
        content_list.append(content)
        
    for a in range(len(hh_list)-1):
        sub2.write(str(a)+'\n')
        sub2.write(str(hh_list[a])+':'+str(mm_list[a])+':'+str(ss_list[a])+','
                   +str(mms_list[a])+" --> "+str(hh_list[a+1])+':'+str(mm_list[a+1])
                   +':'+str(ss_list[a+1])+','+str(mms_list[a+1])+'\n')
        sub2.write(content_list[a]+'\n')
    sub2.close()







    
        
