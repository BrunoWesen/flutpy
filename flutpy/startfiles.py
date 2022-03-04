# Project Framework default is 1 (Model/View/Provider)
# src is source where is the lib folder located

def startmain(src="flutterproject/myapp/lib", pkg="Provider", file="app_widget", home="",
              project_framework=1, autoconfigfile=True):
    maindart = open(src + "/main.dart", "w")

    if project_framework == 1:
        maindart.write(
            "import 'package:flutter/material.dart';\n"
            "import '" + pkg + "/" + file + ".dart';\n\n"
            "void main() => runApp(AppWidget());")

    else:
        print("This project framework is not avaliable yet. :(")

    maindart.close()

    if autoconfigfile:
        configfile(home, src, pkg, file)

# Its not recomended use this manually

def configfile(home, src, pkg, file):
    app_widgetdart = open(src+"/"+pkg+"/"+file+".dart", "w")

    if home == "":
        app_widgetdart.write("import 'package:flutter/material.dart';\n\n"
                             "class AppWidget extends StatelessWidget {\n"
                             "  @override\n"
                             "  Widget build(BuildContext context) {\n"
                             "    return MaterialApp();\n"
                             "  }\n"
                             "}")

    else:
        app_widgetdart.write("import 'package:flutter/material.dart';\n"
                             "import '../View/Screens/homepage.dart';\n\n"
                             "class AppWidget extends StatelessWidget {\n"
                             "  @override\n"
                             "  Widget build(BuildContext context) {\n"
                             "    return MaterialApp(\n"
                             "      home:" + home + "(),\n"
                             "    );\n"
                             "  }\n"
                             "}")

    app_widgetdart.close()
