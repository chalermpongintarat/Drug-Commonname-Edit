with open("drug_list.txt", "r") as file: 
    lines = file.read().split("\n")
    
    find = "'"

    drug_commonname_edit = []

    for line in lines:
        if find in line:
            line = line.replace("'", "_")
            drug_commonname_edit.append(line)
        else:
            drug_commonname_edit.append(line)

    f = open("drug_commonname_edit.txt", "w")
    for line in drug_commonname_edit:
        f.write(str(line))
        f.write("\n")
    f.close()