from CodeWriter import *
from Parser import *


parser = Parser('FunctionCalls/StaticsTest')
code_writer = CodeWriter('FunctionCalls/StaticsTest/StaticsTest.asm')


code_writer.writeInit()


while parser.hasMoreLines():

    print("_______________ₓₑ_______ₓ_________________ₓ__________ₓ____________ₑ____________")

    parser.advance()
    print(parser.lineContent)

    match parser.commandType():
        case Command.C_POP:
            code_writer.writePushPop('pop', parser.arg1(), parser.arg2())
        case Command.C_PUSH:
            code_writer.writePushPop('push', parser.arg1(), parser.arg2())
        case Command.C_ARITHMETIC:
            code_writer.writeArithmetic(parser.arg1())
        case Command.C_LABEL:
            code_writer.writeLabel(parser.arg1())
        case Command.C_IF:
            code_writer.writeIf(parser.arg1())
        case Command.C_GOTO:
            code_writer.writeGoto(parser.arg1())
        case Command.C_FUNCTION:
            code_writer.writeFunction(parser.arg1(), parser.arg2())
        case Command.C_RETURN:
            code_writer.writeReturn()
        case Command.C_CALL:
            code_writer.writeCall(parser.arg1(), parser.arg2())
        case 0:
            code_writer.changeFile(parser.lineContent[38:-1])
            print(code_writer.filename)
        case _:
            print('not found')
