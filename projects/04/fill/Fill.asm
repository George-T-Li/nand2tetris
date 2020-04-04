// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// NOTE: first 'offscreen' register is 17440

(LISTEN)
    @KBD        // refers to the register that detects keyboard input
    D=M         // sets D to the ASCII value of the keyboard's input
    @BLACK      // refers to BLACK
    D;JGT       // jumps to BLACK if a key is pressed
    @LISTEN     // refers to LISTEN
    0;JMP       // mandatory jump back to LISTEN

(BLACK)
    @SCREEN     // refers to the base address of the screen
    D=A         // sets D to the address of the screen, not the value in the address
    @pointer    // refers to a register
    M=D         // the value in pointer is now D (the address of the start of the screen)
    (WRITE)     
        @pointer
        A=M     // A register now has the value in pointer
        M=-1    // M[A] is now -1 (black pixels)
        @pointer
        D=M     // D now has the address of part of the screen
        @1
        D=D+A   // D now has the address of the next part of the screen
        @pointer
        M=D     // pointer now refers to the next part of the screen

        @KBD
        D=M
        @WHITE
        D;JEQ   // jump to WHITE if no key is pressed (D = 0)

        @24576
        D=A
        @pointer
        D=D-M
        @BLACK
        D;JEQ   // jump to BLACK when the register reaches 24576 (ie. offscreen)

        @WRITE
        0;JMP   // jump to WRITE

(WHITE)
    @SCREEN     // refers to the base address of the screen
    D=A         // sets D to the address of the screen, not the value in the address
    @pointer    // refers to a register
    M=D         // pointer now refers to D (the address of the start of the screen)
    (CLEAR)     
        @pointer
        A=M     // A register now has the value in pointer
        M=0     // M[A] is now 0 (white pixels)
        @pointer
        D=M     // D now has the address of part of the screen
        @1
        D=D+A   // D now has the address of the next part of the screen
        @pointer
        M=D     // pointer now refers to the next part of the screen

        @KBD
        D=M
        @BLACK
        D;JGT   // jump to BLACK if key is pressed (D > 0)

        @24576
        D=A
        @pointer
        D=D-M
        @WHITE
        D;JEQ   // jump to WHITE when the register reaches 24576 (ie. offscreen)
        
        @CLEAR
        0;JMP   // jump to CLEAR
