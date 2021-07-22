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
    sub[0]=sub[0][2:len(sub[0])+1]
    sub.append(sub[len(sub)-1])
    file.close
    for n in sub:
        n = n.strip(' ')
        content = n.split("]")[1]
        content_list.append(content)
    for a in range(len(content_list)-1):
                sub2.write(content_list[a])
    sub2.close









    
        
