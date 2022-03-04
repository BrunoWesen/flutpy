# This class will read the .flutter files to draw interfaces classes.

def builder(file):

    if file.split(".")[1] != "flutter":
        raise TypeError('builder only receive valid .flutter files')

    flutterfile = open(file, "r")
    print(flutterfile.read())
    flutterfile.close()
