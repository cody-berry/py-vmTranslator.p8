@256
D=A
@SP
M=D
// function Sys.init 0
@5
D=A
@SP
MD=D+M
@LCL
M=D
@5
D=D-A
@ARG
M=D
(Sys.init)
// push constant 4000
@4000
D=A
@SP
M=M+1
A=M-1
M=D
// pop pointer 0
@SP
AM=M-1
D=M
@3
M=D
// push constant 5000
@5000
D=A
@SP
M=M+1
A=M-1
M=D
// pop pointer 1
@SP
AM=M-1
D=M
@4
M=D
// call Sys.main 0
@1
D=A
@SP
M=D+M
@returnAddress1
D=A
@SP
A=M
M=D
@LCL
D=M
@SP
AM=M+1
M=D
@ARG
D=M
@SP
AM=M+1
M=D
@THIS
D=M
@SP
AM=M+1
M=D
@THAT
D=M
@SP
AM=M+1
M=D
@SP
MD=M+1
@5
D=D-A
@1
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Sys.main
0;JMP
(returnAddress1)
// pop temp 1
@SP
AM=M-1
D=M
@6
M=D
// label LOOP
(LOOP)
// goto LOOP
@LOOP
0;JMP
// function Sys.main 5
@5
D=A
@SP
MD=D+M
@LCL
M=D
@5
D=D-A
@ARG
M=D
(Sys.main)
@SP
M=M+1
A=M-1
M=0
@SP
M=M+1
A=M-1
M=0
@SP
M=M+1
A=M-1
M=0
@SP
M=M+1
A=M-1
M=0
@SP
M=M+1
A=M-1
M=0
// push constant 4001
@4001
D=A
@SP
M=M+1
A=M-1
M=D
// pop pointer 0
@SP
AM=M-1
D=M
@3
M=D
// push constant 5001
@5001
D=A
@SP
M=M+1
A=M-1
M=D
// pop pointer 1
@SP
AM=M-1
D=M
@4
M=D
// push constant 200
@200
D=A
@SP
M=M+1
A=M-1
M=D
// pop local 1
@1
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
// push constant 40
@40
D=A
@SP
M=M+1
A=M-1
M=D
// pop local 2
@2
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
// push constant 6
@6
D=A
@SP
M=M+1
A=M-1
M=D
// pop local 3
@3
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
// push constant 123
@123
D=A
@SP
M=M+1
A=M-1
M=D
// call Sys.add12 1
@0
D=A
@SP
M=D+M
@returnAddress2
D=A
@SP
A=M
M=D
@LCL
D=M
@SP
AM=M+1
M=D
@ARG
D=M
@SP
AM=M+1
M=D
@THIS
D=M
@SP
AM=M+1
M=D
@THAT
D=M
@SP
AM=M+1
M=D
@SP
MD=M+1
@5
D=D-A
@1
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Sys.add12
0;JMP
(returnAddress2)
// pop temp 0
@SP
AM=M-1
D=M
@5
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
// push local 1
@1
D=A
@LCL
A=D+M
D=M
@SP
M=M+1
A=M-1
M=D
// push local 2
@2
D=A
@LCL
A=D+M
D=M
@SP
M=M+1
A=M-1
M=D
// push local 3
@3
D=A
@LCL
A=D+M
D=M
@SP
M=M+1
A=M-1
M=D
// push local 4
@4
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
// add
@SP
AM=M-1
D=M
A=A-1
D=D+M
M=D
// add
@SP
AM=M-1
D=M
A=A-1
D=D+M
M=D
// add
@SP
AM=M-1
D=M
A=A-1
D=D+M
M=D
@LCL
D=M
@endFrame
M=D
@SP
AM=M-1
D=M
@ARG
A=M
M=D
@ARG
D=M+1
@SP
M=D
@endFrame
AM=M-1
D=M
@THAT
M=D
@endFrame
AM=M-1
D=M
@THIS
M=D
@endFrame
AM=M-1
D=M
@ARG
M=D
@endFrame
AM=M-1
D=M
@LCL
M=D
@endFrame
AM=M-1
A=M
0;JMP
// function Sys.add12 0
@5
D=A
@SP
MD=D+M
@LCL
M=D
@5
D=D-A
@ARG
M=D
(Sys.add12)
// push constant 4002
@4002
D=A
@SP
M=M+1
A=M-1
M=D
// pop pointer 0
@SP
AM=M-1
D=M
@3
M=D
// push constant 5002
@5002
D=A
@SP
M=M+1
A=M-1
M=D
// pop pointer 1
@SP
AM=M-1
D=M
@4
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
// push constant 12
@12
D=A
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
@LCL
D=M
@endFrame
M=D
@SP
AM=M-1
D=M
@ARG
A=M
M=D
@ARG
D=M+1
@SP
M=D
@endFrame
AM=M-1
D=M
@THAT
M=D
@endFrame
AM=M-1
D=M
@THIS
M=D
@endFrame
AM=M-1
D=M
@ARG
M=D
@endFrame
AM=M-1
D=M
@LCL
M=D
@endFrame
AM=M-1
A=M
0;JMP
