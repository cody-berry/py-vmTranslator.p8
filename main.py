from CodeWriter import *
from Parser import *


parser = Parser('FunctionCalls/NestedCall/Sys.vm')
code_writer = CodeWriter('FunctionCalls/NestedCall/NestedCall.asm')

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
        case _:
            print('not found')
