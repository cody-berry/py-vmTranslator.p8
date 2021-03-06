class CodeWriter:
    def __init__(self, file_name):
        self.file = open(file_name, 'w')
        self.equality_counter = 0
        self.filename = file_name
        self.return_address_counter = 0

    # write an arithmetic command like add or subtract
    def writeArithmetic(self, command):
        if command == 'add':
            self._writeAdd()
        if command == 'sub':
            self._writeSub()
        if command == 'neg':
            self._writeNeg()
        if command == 'not':
            self._writeNot()
        if command == 'and':
            self._writeAnd()
        if command == 'or':
            self._writeOr()
        if len(command) == 2 and command != 'or':
            operator = ' '
            if command == 'lt':
                operator = 0
            if command == 'eq':
                operator = 1
            if command == 'gt':
                operator = 2
            self._writeEqGtLt(operator)

    # PROTECTED
    # write an add command
    def _writeAdd(self):
        c = [
            "// add",
            "@SP",
            "AM=M-1",
            "D=M",
            "A=A-1",
            "D=D+M",
            "M=D"
        ]

        for line in c:
            print(line)
            self.file.write(line + "\n")

    # PROTECTED
    # write a subtract command
    def _writeSub(self):
        c = [
            "// sub ",
            "@SP",
            "AM=M-1",
            "D=M",
            "A=A-1",
            "D=M-D",
            "M=D"
        ]

        for line in c:
            print(line)
            self.file.write(line + "\n")

    # PROTECTED
    # write a neg command
    def _writeNeg(self):
        c = [
            "// neg ",
            "@SP",
            "A=M-1",
            "M=-M"
        ]

        for line in c:
            print(line)
            self.file.write(line + "\n")

    # PROTECTED
    # write a 'not' command
    def _writeNot(self):
        c = [
            "// not ",
            "@SP",
            "A=M-1",
            "M=!M"
        ]

        for line in c:
            print(line)
            self.file.write(line + "\n")

    # PROTECTED
    # write an and command
    def _writeAnd(self):
        c = [
            "// and",
            "@SP",
            "AM=M-1",
            "D=M",
            "A=A-1",
            "D=D&M",
            "M=D"
        ]
        for line in c:
            print(line)
            self.file.write(line + "\n")

    # PROTECTED
    # write an or command
    def _writeOr(self):
        c = [
            "// or ",
            "@SP",
            "AM=M-1",
            "D=M",
            "A=A-1",
            "D=D|M",
            "M=D"
        ]
        for line in c:
            print(line)
            self.file.write(line + "\n")

    # PROTECTED
    # write an equality command
    def _writeEqGtLt(self, operator):
        self.equality_counter += 1

        jump_type = ""
        if operator == 0:  # lt
            jump_type = "LT"
        if operator == 1:  # eq
            jump_type = "EQ"
        if operator == 2:  # gt
            jump_type = "GT"

        c = [
            "// " + jump_type.lower(),
            "@SP",
            "AM=M-1",
            "D=M",
            "A=A-1",
            "D=M-D",
            f"@TRUE{self.equality_counter}",
            f"D;J{jump_type}",
            "@SP",
            "A=M-1",
            "M=0",
            f"@STOP{self.equality_counter}",
            f"D;JMP",
            f"(TRUE{self.equality_counter})",
            "@SP",
            "A=M-1",
            "M=-1",
            f"(STOP{self.equality_counter})"
        ]

        for line in c:
            print(line)
            self.file.write(line + "\n")

    # write a push or pop command like push constant i
    def writePushPop(self, push_or_pop, segment, index):
        if push_or_pop == 'push':
            if segment == 'constant':
                self._writePushConstant(index)
            if segment == 'static':
                self._writePushStatic(index)
            if segment == 'pointer':
                self._writePushPointer(index)
            if segment == 'this':
                self._writePushThis(index)
            if segment == 'that':
                self._writePushThat(index)
            if segment == 'local':
                self._writePushLocal(index)
            if segment == 'argument':
                self._writePushArgument(index)
            if segment == 'temp':
                self._writePushTemp(index)
        if push_or_pop == 'pop':
            if segment == 'static':
                self._writePopStatic(index)
            if segment == 'pointer':
                self._writePopPointer(index)
            if segment == 'this':
                self._writePopThis(index)
            if segment == 'that':
                self._writePopThat(index)
            if segment == 'local':
                self._writePopLocal(index)
            if segment == 'argument':
                self._writePopArgument(index)
            if segment == 'temp':
                self._writePopTemp(index)

    # PROTECTED
    # write push constant i
    def _writePushConstant(self, i):
        c = [
            f"// push constant {i}",
            f"@{i}",
            "D=A",  # D=i
            "@SP",
            "M=M+1",  # SP++
            "A=M-1",  # A=originalSP
            "M=D"  # RAM[SP] = i
        ]
        for line in c:
            print(line)
            self.file.write(line + "\n")

    # PROTECTED
    # write push static i
    def _writePushStatic(self, i):
        c = [
            f"// push static {i}",
            f"@{self.filename}.{i}",  # access static i
            "D=M",  # D = RAM[variable at i]
            "@SP",
            "M=M+1",  # SP++
            "A=M-1",  # A=originalSP
            "M=D"  # RAM[SP] = i
        ]
        for line in c:
            print(line)
            self.file.write(line + "\n")

    # PROTECTED
    # write pop static i
    def _writePopStatic(self, i):
        c = [
            f"// pop static {i}",
            "@SP",
            "AM=M-1",  # SP--, A=SP
            "D=M",  # D=RAM[SP]
            f"@{self.filename}.{i}",
            "M=D"  # RAM[variable at i] = RAM[SP]
        ]
        for line in c:
            print(line)
            self.file.write(line + "\n")

    # PROTECTED
    # write push pointer i
    def _writePushPointer(self, i):
        c = [
            f"// push pointer {i}",
            f"@{3 + i}",  # access THIS/THAT
            "D=M",  # D=THIS/THAT
            "@SP",
            "M=M+1",
            "A=M-1",
            "M=D",  # RAM[SP] = THIS/THAT
        ]
        for line in c:
            print(line)
            self.file.write(line + "\n")

    # PROTECTED
    # write pop pointer i
    def _writePopPointer(self, i):
        c = [
            f"// pop pointer {i}",
            "@SP",
            "AM=M-1",
            "D=M",  # D=RAM[SP]
            f"@{3 + i}",
            "M=D"  # THIS/THAT = RAM[SP]
        ]
        for line in c:
            print(line)
            self.file.write(line + "\n")

    # PROTECTED
    # write push pointer i
    def _writePushTemp(self, i):
        c = [
            f"// push temp {i}",
            f"@{5 + i}",  # access RAM[5-12]
            "D=M",  # D=RAM[5-12]
            "@SP",
            "M=M+1",
            "A=M-1",
            "M=D",  # RAM[SP] = RAM[5-12]
        ]
        for line in c:
            print(line)
            self.file.write(line + "\n")

    # PROTECTED
    # write pop pointer i
    def _writePopTemp(self, i):
        c = [
            f"// pop temp {i}",
            "@SP",
            "AM=M-1",
            "D=M",  # D=RAM[SP]
            f"@{5 + i}",
            "M=D"  # RAM[5-12] = RAM[SP]
        ]
        for line in c:
            print(line)
            self.file.write(line + "\n")

    # PROTECTED
    # write push this i
    def _writePushThis(self, i):
        c = [
            f"// push this {i}",
            f"@{i}",
            "D=A",  # D=i
            f"@THIS",  # access THIS
            "A=D+M",
            "D=M",  # D=*THIS
            "@SP",
            "M=M+1",
            "A=M-1",
            "M=D",  # RAM[SP] = THIS
        ]
        for line in c:
            print(line)
            self.file.write(line + "\n")

    # PROTECTED
    # write pop this i
    def _writePopThis(self, i):
        c = [
            f"// pop this {i}",
            f"@{i}",
            "D=A",  # D=i
            "@THIS",
            "D=D+M",  # D = RAM[THIS] + i
            "@ad",
            "M=D",  # address = RAM[THIS] + i
            "@SP",
            "AM=M-1",
            "D=M",  # D=RAM[SP]
            "@ad",
            "A=M",  # A = RAM[THIS] + i
            "M=D",  # RAM[RAM[THIS] + i] = RAM[SP]
        ]
        for line in c:
            print(line)
            self.file.write(line + "\n")

    # PROTECTED
    # write push that i
    def _writePushThat(self, i):
        c = [
            f"// push that {i}",
            f"@{i}",
            "D=A",  # D=i
            f"@THAT",  # access THAT
            "A=D+M",
            "D=M",  # D=*THAT
            "@SP",
            "M=M+1",
            "A=M-1",
            "M=D",  # RAM[SP] = THAT
        ]
        for line in c:
            print(line)
            self.file.write(line + "\n")

    # PROTECTED
    # write pop that i
    def _writePopThat(self, i):
        c = [
            f"// pop that {i}",
            f"@{i}",
            "D=A",  # D=i
            "@THAT",
            "D=D+M",  # D = RAM[THAT] + i
            "@ad",
            "M=D",  # address = RAM[THAT] + i
            "@SP",
            "AM=M-1",
            "D=M",  # D=RAM[SP]
            "@ad",
            "A=M",  # A = RAM[THAT] + i
            "M=D",  # RAM[RAM[THAT] + i] = RAM[SP]
        ]
        for line in c:
            print(line)
            self.file.write(line + "\n")

    # PROTECTED
    # write push local i
    def _writePushLocal(self, i):
        c = [
            f"// push local {i}",
            f"@{i}",
            "D=A",  # D=i
            f"@LCL",  # access LCL
            "A=D+M",
            "D=M",  # D=*LCL
            "@SP",
            "M=M+1",
            "A=M-1",
            "M=D",  # RAM[SP] = LCL
        ]
        for line in c:
            print(line)
            self.file.write(line + "\n")

    # PROTECTED
    # write pop local i
    def _writePopLocal(self, i):
        c = [
            f"// pop local {i}",
            f"@{i}",
            "D=A",  # D=i
            "@LCL",
            "D=D+M",  # D = RAM[LCL] + i
            "@ad",
            "M=D",  # address = RAM[LCL] + i
            "@SP",
            "AM=M-1",
            "D=M",  # D=RAM[SP]
            "@ad",
            "A=M",  # A = RAM[LCL] + i
            "M=D",  # RAM[RAM[LCL] + i] = RAM[SP]
        ]
        for line in c:
            print(line)
            self.file.write(line + "\n")

    # PROTECTED
    # write push argument i
    def _writePushArgument(self, i):
        c = [
            f"// push argument {i}",
            f"@{i}",
            "D=A",  # D=i
            f"@ARG",  # access ARG
            "A=D+M",
            "D=M",  # D=*ARG
            "@SP",
            "M=M+1",
            "A=M-1",
            "M=D",  # RAM[SP] = ARG
        ]
        for line in c:
            print(line)
            self.file.write(line + "\n")

    # PROTECTED
    # write pop argument i
    def _writePopArgument(self, i):
        c = [
            f"// pop argument {i}",
            f"@{i}",
            "D=A",  # D=i
            "@ARG",
            "D=D+M",  # D = RAM[ARG] + i
            "@ad",
            "M=D",  # address = RAM[ARG] + i
            "@SP",
            "AM=M-1",
            "D=M",  # D=RAM[SP]
            "@ad",
            "A=M",  # A = RAM[ARG] + i
            "M=D",  # RAM[RAM[ARG] + i] = RAM[SP]
        ]
        for line in c:
            print(line)
            self.file.write(line + "\n")

    # write label label
    def writeLabel(self, label):
        c = [
            f"// label {label}",
            f"({label})"
        ]
        print(c)
        for line in c:
            print(line)
            self.file.write(line + "\n")

    # write if-goto label
    def writeIf(self, label):
        c = [
            f"// if-goto {label}",
            "@SP",
            "AM=M-1",
            "D=M",
            f"@{label}",
            "D;JNE"
        ]
        for line in c:
            print(line)
            self.file.write(line + "\n")

    # write goto label
    def writeGoto(self, label):
        c = [
            f"// goto {label}",
            f"@{label}",
            "0;JMP"
        ]
        for line in c:
            print(line)
            self.file.write(line + "\n")

    # write function functionName numVars
    def writeFunction(self, function_name, num_vars):
        c = [
            f"// function {function_name} {num_vars}",
            "@5",           # in case we're calling this function by hand, we
            "D=A",          # increment SP by 5 and set that to LCL and that
            "@SP",          # minus 5 to ARG.
            "MD=D+M",       # This command adds D (5) to M while also storing it in D.

            "@LCL",
            "M=D",          # Set LCL to D, which is SP.

            "@5",
            "D=D-A",
            "@ARG",
            "M=D",          # ARG=SP-5.
            f"({function_name})"
        ]
        for i in range(0, num_vars):
            c.append('@SP')
            c.append('M=M+1')
            c.append('A=M-1')
            c.append('M=0')
        for line in c:
            print(line)
            self.file.write(line + "\n")

    # write return
    def writeReturn(self):
        # in order, the list of segments we want to return
        segments_to_restore = ['THIS', 'THAT', 'ARG', 'LCL']

        c = [
            "@LCL",
            "D=M",
            "@endFrame",
            "M=D",           # endFrame = LCL

            "@SP",
            "AM=M-1",
            "D=M",           # SP--, D=RAM[SP]
            "@ARG",
            "A=M",
            "M=D",           # ARG=D
                             # total: pop arg 0

            "@ARG",
            "D=M+1",
            "@SP",
            "M=D",           # SP=ARG+1
                             # From the start, we have set a variable called
                             # endFrame to LCL and turned the arguments that we
                             # inputted from call into the return value.
            #
            # "@endFrame",     # We're beginning to jump to the return address an
            # "AM=M-1",        # restore THAT, THIS, ARG, and LCL.
            # "D=M",
            # "@THAT",
            # "M=D",           # endFrame--, THAT=RAM[endFrame]
            #
            # "@endFrame",
            # "AM=M-1",
            # "D=M",
            # "@THIS",
            # "M=D",           # endFrame--, THIS=RAM[endFrame]. Repeat for LCL
            #                  # and ARG.
            #
            # "@endFrame",
            # "AM=M-1",
            # "D=M",
            # "@ARG",
            # "M=D",

            # "@endFrame",
            # "AM=M-1",
            # "D=M",
            # "@LCL",
            # "M=D",
            ]
        for segment in segments_to_restore:
            c.extend(['@endFrame',
                      'AM=M-1',
                      'D=M',
                      '@' + segment,
                      'M=D'   # endFrame--, sets whatever segment to RAM[endFrame]
                      ])

        c.extend([

            "@endFrame",
            "AM=M-1",
            "A=M",
            "0;JMP"          # endFrame--, goto RAM[endFrame].
        ])
        for line in c:
            print(line)
            self.file.write(line + "\n")

    # write call functionName numArgs
    def writeCall(self, function_name, num_args):
        self.return_address_counter += 1
        # in order, the segments we want to push onto the stack
        segments_to_push = ['LCL', 'ARG', 'THIS', 'THAT']

        c = [
            f"// call {function_name} {num_args}",
            f"@{max(1-num_args, 0)}",
            "D=A",                          # in a weird way, sets D to 1 if
            "@SP",                          # num_args is 0, and otherwise sets
            "M=D+M",                        # D to 0.
            f"@returnAddress{self.return_address_counter}",
            "D=A",
            "@SP",
            "A=M",
            "M=D"                           # in SP's current position, push the
            # "@LCL",                       # return address onto the stack
            # "D=M",
            # "@SP",
            # "AM=M+1",
            # "M=D",                        # push LCL onto the stack
            # "@ARG",
            # "D=M",
            # "@SP",
            # "AM=M+1",
            # "M=D",                        # push ARG onto the stack
            # "@THIS",
            # "D=M",
            # "@SP",
            # "AM=M+1",
            # "M=D",                        # push THIS onto the stack
            # "@THAT",
            # "D=M",
            # "@SP",
            # "AM=M+1",
            # "M=D",                        # push THAT onto the stack
            ]

        for segment in segments_to_push:
            c.extend([
                "@" + segment,
                "D=M",                       # sets D to the location of segment
                "@SP",
                "AM=M+1",
                "M=D"                        # SP++, RAM[SP]=D
            ])

        c.extend([
            "@SP",
            "MD=M+1",                # SP++ to accommodate that the fact that
                                     # SP is in the position of the saved THAT,
                                     # set D to SP

            "@5",
            "D=D-A",                 # D -= 5

            f"@{max(num_args, 1)}",
            "D=D-A",                 # D -= 1 if num_args is 0, otherwise
                                     # D -= num_args

            "@ARG",
            "M=D",                   # ARG=D

            "@SP",
            "D=M",
            "@LCL",
            "M=D",                   # LCL=SP

            f"@{function_name}",
            "0;JMP",                 # goto function_name
            f"(returnAddress{self.return_address_counter})"  # here is our return address
        ])
        for line in c:
            print(line)
            self.file.write(line + "\n")

    # write the bootstrap code that sets SP to 256
    def writeInit(self):
        c = [
            "@256",
            "D=A",
            "@SP",
            "M=D"
        ]
        for line in c:
            print(line)
            self.file.write(line + "\n")

    # changes the filename
    def changeFile(self, filename):
        self.filename = filename

