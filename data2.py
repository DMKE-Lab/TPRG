rel_id = set()
relid = 0
ent_id = set()
entid = 0

with open("train.txt", "r", encoding="utf-8") as f:
    datas = f.readlines()
    for data in datas:
        line = data.split("\t")
        if line[1] not in rel_id:
            rel_id.add(line[1])
            with open("relation2id.txt", "a", encoding="utf-8") as f:
                f.write(str(relid) + "\t" + line[1] + "\n")
            relid = relid + 1

        if line[2] not in ent_id:
            ent_id.add(line[2])
            with open("entity2id.txt", "a", encoding="utf-8") as f:
                s = ""
                length = 0
                while length < len(line[2]):
                    if (line[2][length] != "\n"):
                        s = s + line[2][length]
                        length = length + 1
                    else:
                        break
                f.write(str(entid) + "\t" + s + "\n")
            entid = entid + 1

        if line[0] not in ent_id:
            ent_id.add(line[0])
            with open("entity2id.txt", "a", encoding="utf-8") as f:
                f.write(str(entid) + "\t" + line[0] + "\n")
            entid = entid + 1

with open("test.txt", "r", encoding="utf-8") as f:
    datas = f.readlines()
    for data in datas:
        line = data.split("\t")
        if line[1] not in rel_id:
            rel_id.add(line[1])
            with open("relation2id.txt", "a", encoding="utf-8") as f:
                f.write(str(relid) + "\t" + line[1] + "\n")
            relid = relid + 1

        if line[2] not in ent_id:
            ent_id.add(line[2])
            with open("entity2id.txt", "a", encoding="utf-8") as f:
                s = ""
                length = 0
                while length < len(line[2]):
                    if (line[2][length] != "\n"):
                        s = s + line[2][length]
                        length = length + 1
                    else:
                        break
                f.write(str(entid) + "\t" + s + "\n")
            entid = entid + 1

        if line[0] not in ent_id:
            ent_id.add(line[0])
            with open("entity2id.txt", "a", encoding="utf-8") as f:
                f.write(str(entid) + "\t" + line[0] + "\n")
            entid = entid + 1


with open("valid.txt", "r", encoding="utf-8") as f:
    datas = f.readlines()
    for data in datas:
        line = data.split("\t")
        if line[1] not in rel_id:
            rel_id.add(line[1])
            with open("relation2id.txt", "a", encoding="utf-8") as f:
                f.write(str(relid) + "\t" + line[1] + "\n")
            relid = relid + 1

        if line[2] not in ent_id:
            ent_id.add(line[2])
            with open("entity2id.txt", "a", encoding="utf-8") as f:
                s = ""
                length = 0
                while length < len(line[2]):
                    if (line[2][length] != "\n"):
                        s = s + line[2][length]
                        length = length + 1
                    else:
                        break
                f.write(str(entid) + "\t" + s + "\n")
            entid = entid + 1

        if line[0] not in ent_id:
            ent_id.add(line[0])
            with open("entity2id.txt", "a", encoding="utf-8") as f:
                f.write(str(entid) + "\t" + line[0] + "\n")
            entid = entid + 1
