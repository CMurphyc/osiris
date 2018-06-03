from enum import Enum, unique

class _meta:
    __slots__ = (
        'full',
        'version',
        'image',
        'extension',
        'compile',
        'compile_command',
        'running_command',
        'running_extension',
        '_field'
    )

    def __init__( self , ** kw ):
        for _ in kw:
            self.__setattr__( _ , kw[_] )
        self._field = [x for x in kw]

    def __str__(self):
        return self.full

    def __repr__(self):
        return str( self.full )
    
    @property
    def attribute(self):
        return { x : getattr( self , x ) for x in self._field }

@unique
class Language( Enum ):
    GNUCPP = _meta(
        full = 'GNU G++',
        version = '7.3.0',
        image = 'osiris-gcc:7.3.0',
        extension = '.cpp',
        compile = True,
        compile_command = 'g++ -w -O2 -DONLINE_JUDGE -fmax-errors=15 --std=gnu++17 \
                            {sourcefile}.cpp -lm -o {sourcefile}.bin',
        running_command = './{sourcefile}.bin',
        running_extension = '.bin'
    )
    GNUGCC = _meta(
        full = 'GNU GCC',
        version = '7.3.0',
        image = 'osiris-gcc:7.3.0',
        extension = '.c',
        compile = True,
        compile_command = 'gcc -w -O2 -DONLINE_JUDGE -fmax-errors=15 --std=c11 \
                            {sourcefile}.c -lm -o {sourcefile}.bin',
        running_command = './{sourcefile}.bin',
        running_extension = '.bin'
    )
    CLANG = _meta(
        full = 'Clang',
        version = '6.0.0',
        image = 'osiris-clang:6.0.0',
        extension = '.cpp',
        compile = True,
        compile_command = 'clang++-6.0 {sourcefile}.cpp -o {sourcefile}.bin -w -O2 -DONLINE_JUDGE -fmax-errors=15 --std=c++17 -lm',
        running_command = './{sourcefile}.bin',
        running_extension = '.bin'
    )
    PYTHON = _meta(
        full = 'Python',
        version = '3.6.5',
        image = 'osiris-python:3.6.5-stretch',
        extension = '.py',
        compile = False,
        running_command = 'python3 {sourcefile}.py',
        running_extension = '.py'
    )
    JAVA = _meta(
        full = 'Java',
        version = '10',
        image = 'osiris-java:10',
        extension = '.java',
        compile = True,
        compile_command = 'javac {sourcefile}.java',
        running_command = 'java {sourcefile}',
        running_extension = '.class'
    )
    GO = _meta(
        full = 'Go',
        version = '1.10.2',
        image = 'osiris-go:1.10.2',
        extension = '.go',
        compile = False,
        running_command = 'go run {sourcefile}.go',
        running_extension = '.go'
    )
    RUBY = _meta(
        full = 'Ruby',
        version = '2.5.1',
        image = 'osiris-ruby:2.5.1',
        extension = '.rb',
        compile = False,
        running_command = 'ruby {sourcefile}.rb',
        running_extension = '.rb'
    )
    RUST = _meta(
        full = 'Rust',
        version = '1.26.1',
        image = 'osiris-rust:1.26.1',
        extension = '.rs',
        compile = True,
        compile_command = 'rustc -O {sourcefile}.rs -o {sourcefile}.bin',
        running_command = './{sourcefile}.bin',
        running_extension = '.bin'
    )

def get_language( language ):
    for each_lang in Language:
        if each_lang.value.full == language:
            return each_lang
    return None