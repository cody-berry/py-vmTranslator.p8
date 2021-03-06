
import enum
import pathlib


class Command(enum.Enum):
    C_ARITHMETIC = 1
    C_PUSH = 2
    C_POP = 3
    C_LABEL = 4
    C_GOTO = 5
    C_IF = 6
    C_FUNCTION = 7
    C_RETURN = 8
    C_CALL = 9


class Parser:
    def __init__(self, file_name):
        files = []
        if file_name[-2:] == 'vm':
            files.append(open(file_name, 'r'))
        else:
            for path in pathlib.Path(file_name).iterdir():  # iterate through all the files in the directory
                print(path)
                if path.__str__()[-2:] == 'vm':
                    if path.__str__()[-6:-3] == 'Sys':  # if the filename of the file is Sys, then we make it first priority
                        files.insert(0, open(path.__str__(), 'r'))
                    else:
                        files.append(open(path.__str__(), 'r'))

                    print("accepted!")

        self.file = []

        for file in files:
            self.file.append("// Remember to change the filename to " + file.name[(file.name.rfind("\\") + 1):-3] + "!")
            for line in file:
                c = line

                if len(c) > 2 and c[0] != ' ' and c[0] != '/':
                    self.file.append(c)

        self.lineNumber = -1
        self.lineContent = ' '

        self.filename = 'Sys'

    def hasMoreLines(self) -> bool:
        return self.lineNumber < len(self.file) - 1

    def advance(self):
        self.lineNumber += 1
        print(self.lineNumber)
        self.lineContent = self.file[self.lineNumber].strip()
        print(self.lineContent)

    def commandType(self):
        command = self.lineContent.split(' ')

        print(command)

        if command[0] in ['add', 'sub', 'neg', 'or', 'and', 'not', 'lt', 'eq', 'gt']:
            return Command.C_ARITHMETIC
        if command[0] == 'push':
            return Command.C_PUSH
        if command[0] == 'pop':
            return Command.C_POP
        if command[0] == 'label':
            return Command.C_LABEL
        if command[0] == 'goto':
            return Command.C_GOTO
        if command[0] == 'if-goto':
            return Command.C_IF
        if command[0] == 'function':
            return Command.C_FUNCTION
        if command[0] == 'return':
            return Command.C_RETURN
        if command[0] == 'call':
            return Command.C_CALL

        # there's an edge case where it says something like:
        # "// Remember to change the filename to Sys!"
        # In those cases, we return 0.
        if command[0] == '//':
            return 0

    def arg1(self) -> str:
        command = self.lineContent.split(' ')
        if self.commandType() == Command.C_ARITHMETIC:
            return command[0]
        else:
            return command[1]

    def arg2(self) -> int:
        command = self.lineContent.split(' ')
        return int(command[2])



