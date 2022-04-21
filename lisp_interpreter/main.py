import sys
from lisp_interpreter.mylis import env_from_args, run_file, multiline_repl
from lisp_interpreter.exceptions import UndefinedSymbol
from lisp_interpreter.colors import GREEN, RESET

PROMPT1 = GREEN + u"\u03BB " + u"\u276F " + RESET
PROMPT2 = '\N{MIDLINE HORIZONTAL ELLIPSIS}     '
ERROR_MARK = '\N{POLICE CARS REVOLVING LIGHT} '


def main(args: list[str] = sys.argv) -> None:
    if len(args) == 1:
        multiline_repl(PROMPT1, PROMPT2, ERROR_MARK)
    else:
        arg_env = env_from_args(args[1:])
        with open(args[1]) as source_file:
            try:
                run_file(source_file, arg_env)
            except UndefinedSymbol as exc:
                key = exc.args[0]
                print(f'{ERROR_MARK} {key!r} was not defined.')
                cmd = ' '.join(args)
                print('    You can define it as an option:')
                print(f'    $ {cmd} {key}=<value>')


if __name__ == '__main__':
    main()
