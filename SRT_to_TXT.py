import os
def convert(source_file_location,destination_file_location):
    try:
        os.remove(destination_file_location)
    except:
        pass
    content_list = []
    file = open(source_file_location,"r",encoding="utf-8")
    sub2 = open(destination_file_location,"a",encoding="utf-8")
    sub = file.readlines()
    sub[0]=str(0)
    file.close()
    a= 0
    for n in sub:
        n=n.strip('\n')
        if n.isdecimal() :
            content = sub[a+2]
            content_list.append(content)
        a +=1
    for a in range(len(content_list)-1):
        sub2.write(content_list[a])
    sub2.close()
