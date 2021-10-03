#coding=utf-8
import json
import os

def Merge():
    data1 = []
    for root, dirs, files in os.walk("D:\\crawler\\Origin_JSON"):
        for file in files:
            temp = (os.path.join(root, file))
            data1.append(os.path.basename(temp))


    data2 = []
    for i in range(1, 3):
        for root, dirs, files in os.walk("D:\\crawler\\zips"):
            for file in files:
                temp = os.path.join(root, file)
                if temp.split(".")[-1] == 'json':
                    data2.append(os.path.basename(temp))

    for i in range(0, len(data1)):
        with open("D:\\crawler\\Origin_JSON\\{}".format(data1[i])) as f:
            li1 = list(f.read()[1:-1].split(","))
            # print(li1)
            Num = 1


            for j in range(0, len(data2)):
                if data1[i] == data2[j]:
                    tempdata2 = data2[j][0:-5]
                    with open("D:\\crawler\\zips\\{}\\{}".format(tempdata2, data2[j]), encoding='utf-8') as f2:
                        # print(f2.read())
                        li2 = list(f2.read()[4:-3].split(","))
                        # print(li2)
                        li2 = [x.strip() for x in li2 if x.strip()!='']
                    dictFina = {}


                    for k in range(len(li2)):
                        li1.append(li2[k])
                    li1 = [x.strip() for x in li1 if x.strip()!='']
                    index = 0


                    for num in range(0, len(li1)):
                        tempList = li1[num].split(":")
                        str_1 = list(tempList[0])
                        str_2 = list(tempList[1])
                        for num2 in reversed(range(len(str_1))):
                            if str_1[num2] == '''"''':
                                str_1.pop(num2)
                        str_1 = ''.join(str_1)



                        for num2 in reversed(range(len(str_2))):
                            if str_2[num2] == '''"''':
                                str_2.pop(num2)
                        str_2 = ''.join(str_2)

                        dictFina[str_1] = str_2
                    print(dictFina)


                    with open("./zips/{}/{}".format(tempdata2, data2[j]), 'w', encoding='utf-8') as fileFina:

                        fileFina.write(json.dumps(dictFina, indent=4, ensure_ascii=False))
                Num += 1

if __name__ == '__main__':
    Merge()