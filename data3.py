
with open("valid1.txt", "r", encoding="utf-8") as f:
    datas = f.readlines()
    for data in datas:
        line = data.split("\t")
        line_new = line[0] + "\t" + line[1] + "\t" + line[2] + "\n"
        with open("valid.txt", "a", encoding="utf-8") as fa:
            fa.write(line_new)

with open("test1.txt", "r", encoding="utf-8") as f:
    datas = f.readlines()
    for data in datas:
        line = data.split("\t")
        line_new = line[0] + "\t" + line[1] + "\t" + line[2] + "\n"
        with open("test.txt", "a", encoding="utf-8") as fa:
            fa.write(line_new)

with open("train1.txt", "r", encoding="utf-8") as f:
    datas = f.readlines()
    for data in datas:
        line = data.split("\t")
        line_new = line[0] + "\t" + line[1] + "\t" + line[2] + "\n"
        with open("train.txt", "a", encoding="utf-8") as fa:
            fa.write(line_new)



