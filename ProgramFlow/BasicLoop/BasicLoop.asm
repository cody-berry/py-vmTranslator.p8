// initialization code
@256
D=A
@SP
M=D
// push constant 0
@0
D=A
@SP
M=M+1
A=M-1
M=D
// pop local 0
@0
D=A
@LCL
D=D+M
@ad
M=D
@SP
AM=M-1
D=M
@ad
A=M
M=D
// label LOOP_START
(LOOP_START)
// push argument 0
@0
D=A
@ARG
A=D+M
D=M
@SP
M=M+1
A=M-1
M=D
// push local 0
@0
D=A
@LCL
A=D+M
D=M
@SP
M=M+1
A=M-1
M=D
// add
@SP
AM=M-1
D=M
A=A-1
D=D+M
M=D
// pop local 0
@0
D=A
@LCL
D=D+M
@ad
M=D
@SP
AM=M-1
D=M
@ad
A=M
M=D
// push argument 0
@0
D=A
@ARG
A=D+M
D=M
@SP
M=M+1
A=M-1
M=D
// push constant 1
@1
D=A
@SP
M=M+1
A=M-1
M=D
// sub
@SP
AM=M-1
D=M
A=A-1
D=M-D
M=D
// pop argument 0
@0
D=A
@ARG
D=D+M
@ad
M=D
@SP
AM=M-1
D=M
@ad
A=M
M=D
// push argument 0
@0
D=A
@ARG
A=D+M
D=M
@SP
M=M+1
A=M-1
M=D
// if-goto LOOP_START
@SP
AM=M-1
D=M
@LOOP_START
D;JNE
// push local 0
@0
D=A
@LCL
A=D+M
D=M
@SP
M=M+1
A=M-1
M=D
