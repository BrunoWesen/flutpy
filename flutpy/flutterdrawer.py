# This class will read the .flutter files to draw interfaces classes.

def builder(file, src="flutterproject/myapp/lib/View/Screens"):
    if file.split(".")[1] != "flutter":
        raise TypeError('builder only receive valid .flutter files')

    flutterfile = open(file, "r", encoding="utf-8")
    filer = flutterfile.read()
    flutterfile.close()
    # print(filer)
    filesplit = filer.split("\n")

    try:
        while True:
            filesplit.remove("")

    except ValueError:
        pass

    # print(filesplit)
    dartfile = open(src + "/" + file.split(".")[0] + ".dart", "w")
    dartfile.write("import 'package:flutter/material.dart';\n\n")
    # line = 1

    end_of_code = []

    for i in filesplit:
        # print(i)
        isplit = i.split(" ")
        # print(isplit)

        # if line == 1:
        #     class_name = isplit[0]
        #
        #     if isplit[1] == "<<":
        #         extends = " extends " + isplit[2]
        #         dartfile.write("class " + class_name + extends + " {\n  const " + class_name +
        #                        "({\n    Key? key,\n  }) : super(key: key);\n\n  @override\n  "
        #                        "Widget build(BuildContext context) {\n    "
        #                        "Size size = MediaQuery.of(context).size;\n    return ")
        #
        # elif line == 2:
        #     space = 0
        #
        #     for j in i:
        #         if j != " ":
        #             print(space)
        #             break
        #
        #         space += 1
        #
        #     if space != 4:
        #         raise IndentationError("Child without parent")
        #
        # try:
        #     while True:
        #         isplit.remove("")
        #
        # except ValueError:
        #     pass
        #
        # class_name = isplit[0]
        # dartfile.write(class_name + "(\n")
        #
        # if isplit[1] == "a>":
        #     atribute = isplit[2].split(":")
        #     print(isplit[2])
        #     print(atribute)
        #     # for k in isplit[2:]:
        #     #     print(k)
        #     #     k.find("a>")
        #     # object_name = isplit[3]
        #     # dartfile.write(object_name)

        space = 0

        for j in i:
            if j != " ":
                # print(space)
                break

            space += 1

        if space % 4 != 0:
            raise IndentationError("Invalid indentation, must be a multiple of 4 spaces")

        # print(isplit)

        if isplit[0] != "":
            try:
                while True:
                    isplit.remove("")

            except ValueError:
                pass

            class_name = isplit[0]

            if isplit[1] == "<<":
                extends = " extends " + isplit[2]
                dartfile.write("class " + class_name + extends + " {\n  const " + class_name +
                               "({\n    Key? key,\n  }) : super(key: key);\n\n  @override\n  "
                               "Widget build(BuildContext context) {\n    "
                               "Size size = MediaQuery.of(context).size;\n    return ")
                end_of_code.append("\n  }\n}")

        elif space == 4:
            try:
                while True:
                    isplit.remove("")

            except ValueError:
                pass

            object_name = isplit[0]
            dartfile.write(object_name + "(\n")
            end_of_code.append("\n    );")

            if isplit.count("a>") > 0:
                repeated_times = isplit.count("a>")
                # if repeated_times > 1:
                list_to_write = []
                end_of_code_2 = []
                item = []
                items = "".join(f"{e}{i} " for i, e in enumerate(isplit))
                items = items.split(" ")

                for m in items:
                    # print(m)
                    if m.find("a>") != -1:
                        item.append(m[2:])

                # print(item)

                for k in item:
                    # if isplit[k] == "a>":
                    atribute = isplit[int(k)+1].split(":")

                    if atribute[1] == "":
                        try:
                            atribute[1] = isplit[int(k)+2]

                        except IndexError:
                            pass
                        # print(atribute)

                    if atribute[0] == "children":
                        # dartfile.write("      " + atribute[0] + ": " + atribute[1] + "[")
                        list_to_write.append("      " + atribute[0] + ": " + atribute[1] + "[")
                        end_of_code_2.append("\n      ],")

                    else:
                        # dartfile.write("      " + atribute[0] + ": " + atribute[1] + "(")
                        list_to_write.append("      " + atribute[0] + ": " + atribute[1] + "(")
                        end_of_code_2.append("\n      ),")

                index = -1
                # print(list_to_write)

                while repeated_times > 1:
                    add_space = "  " * (repeated_times - 1)
                    list_to_write[index] = "\n" + add_space + list_to_write[index]
                    end_of_code_2[index] = end_of_code_2[index][:2] + add_space + end_of_code_2[index][2:]
                    index -= 1
                    repeated_times -= 1
                    # print(end_of_code_2)

                for element in list_to_write:
                    dartfile.write(element)

                for element in end_of_code_2:
                    end_of_code.append(element)

        # line += 1

    # dartfile.write("\n    );\n  }\n}")
    end_of_code.reverse()
    # print(end_of_code)
    j = ""

    for i in end_of_code:
        j += i

    # print(j)
    dartfile.write(j)
    dartfile.close()
