from utils.pantry import Ingredient

def genPrintStr(prependStr, args, appendStr):
    printStr = prependStr
    printStr += " " + args[0]

    if len(args) > 2:
        for item in args[1:-1]:
            printStr += ", " + item

    if len(args) > 1:
        printStr += " and " + args[-1]

    if appendStr != "":
        printStr += " " + appendStr

    return printStr 

def fry(i):
    print "Fry " + i.name
    return "Fried " + i.name

def blend(*args):
    print genPrintStr("Blend", args, "")
    return "blended mixture"

def cook(*args):
    print genPrintStr("Use a pressure cooker to boil", args, "")
    return "cooked mixture"

def add(*args):
    print genPrintStr("Add", args[1:], "to " + args[0])
    return args[0]

def simmer(*args):
    print genPrintStr("Use a pan to simmer", args, "under medium heat")
    return "simmering mixture"

def temper(*args):
    print genPrintStr("Heat oil in a small pan and temper", args, "")
    return "tempered mix"
