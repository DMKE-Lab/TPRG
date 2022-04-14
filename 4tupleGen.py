relid={}
entid={}
# 0	6898
# 序号 id
with open("entity2id.txt", "r", encoding="utf-8") as f:
    datas = f.readlines()
    for data in datas:
        line = data.split("\t")
        entid[line[1][0:len(line[1])-1]] = int(line[0])
with open("relation2id.txt", "r", encoding="utf-8") as f:
    datas = f.readlines()
    for data in datas:
        line = data.split("\t")
        relid[line[1][0:len(line[1])-1]]= int(line[0])

# print(relid)

with open("valid.txt", "r", encoding="utf-8") as f:
    datas = f.readlines()
    for data in datas:
        line = data.split("\t")
        line_new = str(entid[line[0]]) + "\t" + str(relid[line[1]]) + "\t" + str(entid[line[2]]) + "\t" + line[3] + "\n"
        with open("WIKI\\valid.txt", "a", encoding="utf-8") as fa:
            fa.write(line_new)

with open("test.txt", "r", encoding="utf-8") as f:
    datas = f.readlines()
    for data in datas:
        line = data.split("\t")
        line_new = str(entid[line[0]]) + "\t" + str(relid[line[1]]) + "\t" + str(entid[line[2]]) + "\t" + line[3] + "\n"
        with open("WIKI\\test.txt", "a", encoding="utf-8") as fa:
            fa.write(line_new)

with open("train.txt", "r", encoding="utf-8") as f:
    datas = f.readlines()
    for data in datas:
        line = data.split("\t")
        line_new = str(entid[line[0]]) + "\t" + str(relid[line[1]]) + "\t" + str(entid[line[2]]) + "\t" + line[3] + "\n"
        with open("WIKI\\train.txt", "a", encoding="utf-8") as fa:
            fa.write(line_new)



