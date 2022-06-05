from CodeWriter import *
from Parser import *


parser = Parser('ProgramFlow/BasicLoop/BasicLoop.vm')
code_writer = CodeWriter('ProgramFlow/BasicLoop/BasicLoop.asm')


while parser.hasMoreLines():

    print("_______________________ₓ_________________ₓ__________ₓ____________ₑ____________")

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
        case _:
            print('not found')
