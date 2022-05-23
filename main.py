import glob


text_files = []
for filename in glob.glob("*txt"):
    text_files.append(filename)
if "Result.txt" in text_files:
    text_files.remove("Result.txt")


def sorting_files(files: list, result_file: str):
    temp_dict = {sum(1 for _ in open(one_file, encoding="UTF-8")): one_file for one_file in files}
    with open(result_file, "w") as file_write:
        file_write.write("")
    with open(result_file, "a") as file_write:
        for key in sorted(temp_dict.keys()):
            file_write.write(temp_dict[key] + "\n")
            file_write.write(str(key) + "\n")
            file_write.writelines(line for line in open(temp_dict[key], "r", encoding="UTF-8"))
            file_write.write("\n")


sorting_files(text_files, "Result.txt")