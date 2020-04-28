from parser_module_l import *
from code_module import *

def hack_assembler(fileName):
    """
    Translates each individual assembly command in 'fileName' to its
    equivalent binary instruction in the Hack language.
    """
    outFileName = fileName[:-3] + 'hack'
    with open(fileName, 'r') as asmProgram, open(outFileName, 'w') as hackProgram:
        for line in asmProgram:
            cType = command_type(line)
            if cType == 'A_COMMAND':
                symb = symbol(line)
                aInst = convert_aInst(symb)
                hackProgram.write(aInst+"\n")
            elif cType == 'L_COMMAND':
                symb = symbol(line)
            elif cType == 'C_COMMAND':
                pDest = parser_dest(line)
                pComp = parser_comp(line)
                pJump = parser_jump(line)
                cDest = code_dest(pDest)
                cComp = code_comp(pComp)
                cJump = code_jump(pJump)
                hackProgram.write("111"+cComp+cDest+cJump+"\n")

hack_assembler("C:/Users/under/Documents/GitHub/nand2tetris/projects/06/add/Add.asm")
hack_assembler("C:/Users/under/Documents/GitHub/nand2tetris/projects/06/max/MaxL.asm")
hack_assembler("C:/Users/under/Documents/GitHub/nand2tetris/projects/06/pong/PongL.asm")
hack_assembler("C:/Users/under/Documents/GitHub/nand2tetris/projects/06/rect/RectL.asm")
