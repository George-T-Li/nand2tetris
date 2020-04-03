// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

@R2         // R2 refers to a location in memory
M = 0       // sets R2 to 0
@count      // count refers to a location in memory
M = 0       // sets count to 0

(LOOP)      // start of loop for repeated addition of R0, R1 times
    @count  // refers to count
    D=M     // sets D to count
    @R1     // refers to R1
    D=D-M   // sets D to D - R1
    @END    // refers to END
    D;JEQ   // if D == R1 then goto END
    @count  // refers to count
    M=M+1   // count is increased by 1

    @R0     // refers to R0
    D=M     // sets D to the value in R0
    @R2     // refers to the value in R2
    M=M+D   // sets R2 to R2 + R0 
    @LOOP   // refers to LOOP
    0;JMP   // unconditional jump to LOOP
(END)
    @END
    0;JMP   // unconditional jump to END
