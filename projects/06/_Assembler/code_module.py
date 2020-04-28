def code_dest(string):
    """Returns the binary code of the dest mnemonic"""
    dest_switcher = {
        "null": "000",
        "M": "001",
        "D": "010",
        "MD": "011",
        "A": "100",
        "AM": "101",
        "AD": "110",
        "AMD": "111"
    }
    return dest_switcher.get(string, "dEr")

def code_comp(string):
    """Returns the binary code of the comp mnemonic"""
    comp_switcher = {
       "0": "0101010", "1": "0111111", "-1": "0111010", "D": "0001100",
       "A": "0110000", "M": "1110000", "!D": "0001101", "!A": "0110001",
       "!M": "1110001", "-D": "0001111", "-A": "0110011", "-M": "1110011",
       "D+1": "0011111", "A+1": "0110111", "M+1": "1110111", "D-1": "0001110",
       "A-1": "0110010", "M-1": "1110010", "D+A": "0000010", "D+M": "1000010",
       "D-A": "0010011", "D-M": "1010011", "A-D": "0000111", "M-D": "1000111",
       "D&A": "0000000", "D&M": "1000000", "D|A": "0010101", "D|M": "1010101"
    }
    return comp_switcher.get(string, "compErr")

def code_jump(string):
    """Returns the binary code of the jump mnemonic"""
    jump_switcher = {
        "null": "000",
        "JGT": "001",
        "JEQ": "010",
        "JGE": "011",
        "JLT": "100",
        "JNE": "101",
        "JLE": "110",
        "JMP": "111"   
    }
    return jump_switcher.get(string, "jEr")
    