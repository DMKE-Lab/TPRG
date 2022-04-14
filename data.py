# with open("valid1.txt", "r", encoding="utf-8") as f:
#     datas = f.readlines()
#     for data in datas:
#         line = data.split("\t")
#         s = ""
#         length = 0
#         while length < len(line[3]):
#             if(line[3][length] != "\n"):
#                 s = s + line[3][length]
#                 length = length + 1
#             else:
#                 break
#         line_new = line[0] + "\t" + line[1] + "/" + s + "\t" + line[2] + "\n"
#         with open("valid.txt", "a", encoding="utf-8") as fa:
#             fa.write(line_new)
#
# with open("test1.txt", "r", encoding="utf-8") as f:
#     datas = f.readlines()
#     for data in datas:
#         line = data.split("\t")
#         s = ""
#         length = 0
#         while length < len(line[3]):
#             if(line[3][length] != "\n"):
#                 s = s + line[3][length]
#                 length = length + 1
#             else:
#                 break
#         line_new = line[0] + "\t" + line[1] + "/" + s + "\t" + line[2] + "\n"
#         with open("valid.txt", "a", encoding="utf-8") as fa:
#             fa.write(line_new)

# with open("valid.txt", "r", encoding="utf-8") as f:
#     datas = f.readlines()
#     for data in datas:
#         line = data.split("\t")
#         line_new = line[0] + "\t" + line[2][0:len(line[2])-1] + "\t" + line[1] + "\n"
#         with open("test_sparsity_0.995", "a", encoding="utf-8") as fa:
#             fa.write(line_new)
#
# with open("valid.txt", "r", encoding="utf-8") as f:
#     datas = f.readlines()
#     for data in datas:
#         line = data.split("\t")
#         line_new = line[0] + "\t" + line[2][0:len(line[2])-1] + "\t" + line[1] + "\n"
#         with open("valid_sparsity_0.995", "a", encoding="utf-8") as fa:
#             fa.write(line_new)

#test_sparsity_0.995 valid_sparsity_0.995