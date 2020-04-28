def command_type(command):
    """
    Returns the type of the current command:
    A_COMMAND when command is '@xxx', where 'xxx' is a symbol or decmal number
    C_COMMAND when command is 'dest=comp;jump'
    L_COMMAND when command is '(xxx)', where 'xxx' is a symbol
    NO_COMMAND for blanks or commented out lines
    """
    if command[0] in ["\n", "/"]:
        return 'NO_COMMAND'
    elif command[0] == "@":
        return 'A_COMMAND'
    elif command[0] == "(":
        return 'L_COMMAND'
    else:
        return 'C_COMMAND'

def symbol(command):
    """
    Returns the 'xxx' part of the current command, '@xxx' or '(xxx)'.
    Is only called when commandType() == A_COMMAND or commandType == L_COMMAND
    """
    if command[0] == '@':
        return int(command[1:])
    else:
        return command[1:-2]

def convert_aInst(symbol):
    bSymb = str(bin(symbol))[2:]
    aInst = bSymb.zfill(16)
    return aInst

def parser_dest(command):
    """
    Returns the 'dest' of the current C_COMMAND (null, A, M, D, AM, AD, MD, AMD)
    Is only called when commandType() == C_COMMAND
    """
    if "=" in command:
        d = command.split("=", 1)
        return d[0]
    else:
        return "null"

def parser_comp(command):
    """
    Returns the 'comp' of the current C_COMMAND (see comp table)
    Is only called when commandType() == C_COMMAND
    """
    if "=" in command:
        splitDest = command.split("=", 1)
        noDest = splitDest[1][:-1]
        if ";" in noDest:
            splitJump = noDest.split(";")
            return splitJump[0]
        else:
            return noDest
    else:
        splitJump = command.split(";")
        return splitJump[0]

def parser_jump(command):
    """
    Returns the 'jump' of the current C_COMMAND (null, JGT, JEQ, JGE, JLT, JNE, JLE, JMP)
    Is only called when commandType() = C_COMMAND
    """
    if ";" in command:
        j = command.split(";", 1)
        return j[1][:-1]
    else:
        return "null"
