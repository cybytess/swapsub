import sys

def load(path):
    start_time = []
    end_time = []
    content_list = []
    file = open(path, "r", encoding="utf-8")
    sub = file.readlines()
    file.close()

    if path.split(".")[len(path.split(".")) - 1] == "lrc":
        a = 0
        for n in sub:
            end = 0
            start = 0
            n = n.strip(" ")
            n = n.strip("[")
            content = n.split("]")[1]
            time = n.split("]")[0]
            start += (int(time.split(':')[0]))*60
            start += (float(time.split(':')[1]))*1
            start_time.append(start)
            content_list.append(content)

            if a == len(sub)-1:
                timenext = sub[a].strip("[").split("]")[0]
                end += (float(timenext.split(':')[1])+3)*1
            else:
                timenext = sub[a+1].strip("[").split("]")[0]
                end += float(timenext.split(':')[1])*1
            end += (int(timenext.split(':')[0]))*60
            end_time.append(end)
            
            a = a+1


    elif path.split(".")[len(path.split(".")) - 1] == "srt":
        a = 0
        for n in sub:
            n = n.strip('\n')
            if n.isdecimal():
                end = 0
                start = 0
                
                time = sub[int(a) + 1].split(' --> ')[0]
                start += int((time.split(':')[0]))*3600
                start += int((time.split(':')[1]))*60
                start += float(str(time.split(',')[0].split(':')[2])+"."+str(time.split(',')[1]))*1
                content = sub[a + 2]
                start_time.append(start)
                content_list.append(content)
                
                time = sub[int(a) + 1].split(' --> ')[1]
                end += int((time.split(':')[0]))*3600
                end += int((time.split(':')[1]))*60
                end += float(str(time.split(',')[0].split(':')[2])+"."+str(time.split(',')[1]))*1
                end_time.append(end)
        
                
            a = a + 1
    
    elif path.split(".")[len(path.split(".")) - 1] == "ass":
        for n in sub:
            start = 0
            end = 0
            if n[0:8] == 'Dialogue':
                start += int(n.split(',')[1].split(':')[0])*3600
                start += int(n.split(',')[1].split(':')[1])*60
                start += float(n.split(',')[1].split(':')[2])
                start_time.append(start)
                
                end += int(n.split(',')[2].split(':')[0])*3600
                end += int(n.split(',')[2].split(':')[1])*60
                end += float(n.split(',')[2].split(':')[2])
                end_time.append(end)
                
                content_list.append(n.split(',')[9])
                

    final_list = [start_time,end_time,content_list]
    return final_list


def convert(data, path):
    final = []
    start_time = data[0]
    end_time = data[1]
    content_list = data[2]
    file = open(path, "w", encoding="utf-8")

    if path.split(".")[len(path.split(".")) - 1] == "txt":
        for a in content_list:
            final.append(a)

    if path.split(".")[len(path.split(".")) - 1] == "lrc":
        for a in range(len(start_time)):
            final.append('[' + str(int(start_time[a] // 60)) + ':'
                         + str(round(start_time[a]%60,3))+ ']' + content_list[a])

    if path.split(".")[len(path.split(".")) - 1] == "srt":
        for a in range(len(start_time)):
            final.append(str(a) + '\n')
            final.append(str(int(start_time[a]//3600)) + ':' + str(int(start_time[a]//60))
                         + ':' + str(round(start_time[a]%60,3)).replace('.',',')
                        + " --> " +
                        str(int(end_time[a]//3600)) + ':' + str(int(end_time[a]//60))
                         + ':' + str(round(end_time[a]%60,3)).replace('.',',')+'\n')
            final.append(content_list[a] + '\n')

    if path.split(".")[len(path.split(".")) - 1] == "ass":
        final.append("[Script Info]\nTitle: <untitled>\nScriptType: v4.00+\n"
                   "Collisions: Normal\n"
                   "PlayDepth: 0\n\n"
                   "[v4+ Styles]\n"
                   "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour,"
                   " Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, "
                   "Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\nStyle: Default,Arial,20,&H00FFFFFF,"
                   "&H000080FF,&H00000000,&H80000000,0,0,0,0,100,100,0,0,1,2,2,2,10,10,20,0\n\n"
                   "[Events]\nFormat: Layer, Start, End, Style, Actor, MarginL, MarginR, MarginV, Effect, Text\n")
        for a in range(len(start_time)):
            final.append("Dialogue:")
            final.append("0,")
            final.append(
                str(int(start_time[a]//3600)) + ":" + str(int(start_time[a]//60))
                + ":" + str(round(start_time[a]%60,3)) + "," +           
                str(int(end_time[a]//3600)) + ":" + str(int(end_time[a]//60)) +
                ":" + str(round(start_time[a]%60,3))
                + ",Default,,0,0,0,," + content_list[a])
    for a in final:
        file.write(a)
    file.close()
    return 1

if len(sys.argv) != 3  :
    #print("[ERROR]  Invalid parameter\n",
            #"swapsub <source path>  <target path>")
else:
    if convert(load(sys.argv[1]),sys.argv[2]):
        print("done")