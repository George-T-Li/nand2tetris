from parser_module import *
from code_module import *
from symbolTable_module import *

def hack_assembler(fileName):
    """
    Translates each individual assembly command in 'fileName' to its
    equivalent binary instruction in the Hack language.
    """
    outFileName = fileName[:-3] + 'hack'

    #initialization
    symbolTable = constructor()

    #first pass
    with open(fileName, 'r') as asmFirstPass:
        romAddress = 0
        for line in asmFirstPass:
            if line != "\n" and line[0] != "/":
                #remove leading whitespace
                l = line.lstrip()
                #remove trailing comments
                lSplit = l.split("/", 1)
                parsedLine = lSplit[0].rstrip()
                cType = command_type(parsedLine)
                if cType == 'A_COMMAND' or cType == 'C_COMMAND':
                    romAddress += 1
                elif cType == 'L_COMMAND':
                    symb = symbol(line)
                    add_entry(symb, romAddress, symbolTable)
    #end of first pass
    
    #second pass
    with open(fileName, 'r') as asmSecondPass, open(outFileName, 'w') as hackProgram:
        ramAddress = 16
        for line in asmSecondPass:
            if line != "\n" and line[0] != "/":
                #remove leading whitespace
                l = line.lstrip()
                #remove trailing comments
                lSplit = l.split("/", 1)
                parsedLine = lSplit[0].rstrip()

                cType = command_type(parsedLine)
                if cType == 'A_COMMAND':
                    symb = symbol(parsedLine)
                    if not symb.isdigit():
                        if table_contains(symb, symbolTable):
                            aNumeric = get_address(symb, symbolTable)
                        else:
                            add_entry(symb, ramAddress, symbolTable)
                            ramAddress += 1
                            aNumeric = get_address(symb, symbolTable)
                        aInst = convert_aInst(aNumeric)
                    else:
                        aInst = convert_aInst(int(symb))
                    hackProgram.write(aInst+"\n")
                elif cType == 'L_COMMAND':
                    symb = symbol(parsedLine)
                elif cType == 'C_COMMAND':
                    pDest = parser_dest(parsedLine)
                    pComp = parser_comp(parsedLine)
                    pJump = parser_jump(parsedLine)
                    cDest = code_dest(pDest)
                    cComp = code_comp(pComp)
                    cJump = code_jump(pJump)
                    hackProgram.write("111"+cComp+cDest+cJump+"\n")

hack_assembler("C:/Users/under/Documents/GitHub/nand2tetris/projects/06/add/Add.asm")
hack_assembler("C:/Users/under/Documents/GitHub/nand2tetris/projects/06/max/Max.asm")
hack_assembler("C:/Users/under/Documents/GitHub/nand2tetris/projects/06/pong/Pong.asm")
hack_assembler("C:/Users/under/Documents/GitHub/nand2tetris/projects/06/rect/Rect.asm")
