def load(path):
    hh_starts = []
    mm_starts = []
    ss_starts = []
    mms_starts = []
    content_list = []
    hh_ends = []
    mm_ends = []
    ss_ends = []
    mms_ends = []
    file = open(path, "r", encoding="utf-8")
    sub = file.readlines()
    file.close()

    if path.split(".")[len(path.split(".")) - 1] == "lrc":
        a = 0
        for n in sub:
            n = n.strip(" ")
            n = n.strip("[")
            content = n.split("]")[1]
            time = n.split("]")[0]
            hh_starts.append(str(int(time.split(':')[0]) // 60).rjust(2, '0'))
            mm_starts.append(str(int(time.split(':')[0]) % 60).rjust(2, '0'))
            ss_starts.append(
                str(time.split(':')[1].split('.')[0]).rjust(2, '0'))
            mms_starts.append(
                str(time.split(':')[1].split('.')[1]).ljust(3, '0'))
            content_list.append(content)

            if a == len(sub)-1:
                timenext = sub[a].strip("[").split("]")[0]
                ss_ends.append(
                    str(int(timenext.split(':')[1].split('.')[0])+3).rjust(2, '0'))
            else:
                timenext = sub[a+1].strip("[").split("]")[0]
                ss_ends.append(
                    str(timenext.split(':')[1].split('.')[0]).rjust(2, '0'))
            hh_ends.append(
                str(int(timenext.split(':')[0]) // 60).rjust(2, '0'))
            mm_ends.append(str(int(timenext.split(':')[0]) % 60).rjust(2, '0'))
            mms_ends.append(
                str(timenext.split(':')[1].split('.')[1]).ljust(3, '0'))

            a = a+1

        final_list = [hh_starts, mm_starts, ss_starts, mms_starts,
                      hh_ends, mm_ends, ss_ends, mms_ends,
                      content_list]
        return final_list

    elif path.split(".")[len(path.split(".")) - 1] == "srt":
        a = 0
        for n in sub:
            n = n.strip('\n')
            if n.isdecimal():
                time = sub[int(a) + 1].split(' --> ')[0]
                hh = str((time.split(':')[0]))
                mm = str((time.split(':')[1]))
                ss = str(time.split(',')[0].split(':')[2])
                mms = str(time.split(',')[1])
                content = sub[a + 2]
                hh_starts.append(hh)
                mm_starts.append(mm)
                ss_starts.append(ss)
                mms_starts.append(mms)
                content_list.append(content)
                time = sub[int(a) + 1].split(' --> ')[1]
                hh = str((time.split(':')[0]))
                mm = str((time.split(':')[1]))
                ss = str(time.split(',')[0].split(':')[2])
                mms = str(time.split(',')[1].strip("\n"))
                hh_ends.append(hh)
                mm_ends.append(mm)
                ss_ends.append(ss)
                mms_ends.append(mms)

            a = a + 1
        final_list = [hh_starts, mm_starts, ss_starts, mms_starts,
                      hh_ends, mm_ends, ss_ends, mms_ends,
                      content_list]
        return final_list


def convert(data, path):
    hh_starts = data[0]
    mm_starts = data[1]
    ss_starts = data[2]
    mms_starts = data[3]
    hh_ends = data[4]
    mm_ends = data[5]
    ss_ends = data[6]
    mms_ends = data[7]
    content_list = data[8]
    file = open(path, "w", encoding="utf-8")

    if path.split(".")[len(path.split(".")) - 1] == "txt":
        for a in content_list:
            file.write(a)

    if path.split(".")[len(path.split(".")) - 1] == "lrc":
        for a in range(len(mm_starts)):
            file.write('[' + mm_starts[a] + ':' + ss_starts[a] +
                       '.' + mms_starts[a] + ']' + content_list[a])

    if path.split(".")[len(path.split(".")) - 1] == "srt":
        for a in range(len(hh_starts)):
            file.write(str(a) + '\n')
            file.write(str(hh_starts[a]) + ':' + str(mm_starts[a]) + ':' + str(ss_starts[a]) + ','
                       + str(mms_starts[a]) + " --> " +
                       str(hh_ends[a]) + ':' + str(mm_ends[a])
                       + ':' + str(ss_ends[a]) + ',' + str(mms_ends[a]) + '\n')
            file.write(content_list[a] + '\n')

    if path.split(".")[len(path.split(".")) - 1] == "ass":
        file.write("[Script Info]\nTitle: <untitled>\nScriptType: v4.00+\n"
                   "Collisions: Normal\n"
                   "PlayDepth: 0\n\n"
                   "[v4+ Styles]\n"
                   "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour,"
                   " Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, "
                   "Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\nStyle: Default,Arial,20,&H00FFFFFF,"
                   "&H000080FF,&H00000000,&H80000000,0,0,0,0,100,100,0,0,1,2,2,2,10,10,20,0\n\n"
                   "[Events]\nFormat: Layer, Start, End, Style, Actor, MarginL, MarginR, MarginV, Effect, Text\n")
        for a in range(len(hh_starts)):
            file.write("Dialogue:")
            file.write("0,")
            file.write(
                str(int(hh_starts[a]) + 0) + ":" + str(mm_starts[a]) + ":" + str(ss_starts[a]) + "." + str(
                    mms_starts[a]) + "," +
                str(int(hh_ends[a]) + 0) + ":" + str(mm_ends[a]) +
                ":" + str(ss_ends[a]) + "." + str(mms_ends[a])
                + ",Default,,0,0,0,," + content_list[a])
    file.close()
