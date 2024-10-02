def title(text):
    if isinstance(text, str):
        print("======================================")
        print(text)
        print("======================================")
    else:
        raise TypeError("INPUT ERROR: Input not str")

def inputForceType(text, varType):
    while True:
        var = input(str(text))
        if varType == str:
            return var
        
        elif varType == int:
            try:
                int(var)
            except ValueError:
                title("INPUT ERROR: Expected INT input")
            else:
                return int(var)

        elif varType == float:
            try:
                float(var)
            except ValueError:
                title("INPUT ERROR: Expected FLOAT input")
            else:
                return float(var)
            
        else:
            raise TypeError("DUMBASS: You out here making sure the user doesn't input somehting wrong and you go and type \""+str(varType)+"\"")

help("module")
