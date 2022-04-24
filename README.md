<p align="center"> Project information - LISP Interpreter </p>

<p align="center">
  <a href="#objective">Objective</a> •
  <a href="#technologies">Technologies</a> •
  <a href="#usage">Usage</a> •
  <a href="howitworks">How it works</a> •
  <a href="#license">License</a>
</p>

<h2 id="objective" > 🎯 Objectives </h2>

Lispy is a Scheme interpreter written in Python, inspired by the [lispy from Peter Norvig](http://norvig.com/lispy.html). This is a modified version from Luciano Ramalho's implementation of the [lispy](https://github.com/ramalho/mylis.py) with type checking and a few other features.

<h2 id="technologies"> 🛠 Technologies </h2>

The tools used in the construction of the project were:

- [Black](https://black.readthedocs.io/en/stable/), a formatter for Python code.
- [Dialogue-tester](https://package.wiki/dialogue-tester), a dialogue testing tool to help testing REPLs.
- [Pytest](https://docs.pytest.org/en/latest/), a testing framework for Python.
- [Python](https://www.python.org/), a powerful, easy to learn, and powerful programming language.
- [Setuptools](https://setuptools.readthedocs.io/en/latest/setuptools.html) to manage the dependencies of the project.

<h2 id="usage" > 👷 Usage </h2>

Install the project using the following command:

```bash
# Commands used to start the project.
pip install -e .
```

Now execute the lispy interpreter using the `lispy` command.

This should put you inside of the interpreter. Then you can exercise your scheme skills.

```sh
lispy
```

```scheme
(define x 1)
x
$ 1
```

Also you can run one of the scheme examples:

```sh
# Run the first example.
lispy examples/factorial.scm x=5
```

x stands for factorial of x (aka x!)

<h2 id="howitworks" > 📚 How it works </h2>

A language interpreter has two parts:

<h3> Parsing </h3>

  The parsing component takes an input program in the form of a sequence of characters, verifies it according to the syntactic rules of the language, and translates the program into an internal representation. In a simple interpreter the internal representation is a tree structure (often called an abstract syntax tree) that closely mirrors the nested structure of statements or expressions in the program. In a language translator called a compiler there is often a series of internal representations, starting with an abstract syntax tree, and progressing to a sequence of instructions that can be directly executed by the computer. The Lispy parser is implemented with the function parse.

<h3> Execution </h3>

The internal representation is then processed according to the semantic rules of the language, thereby carrying out the computation. Lispy's execution function is called eval (note this shadows Python's built-in function of the same name).

Here is a diagram of the interpretation process:

```sh
program ➡ parse ➡ abstract-syntax-tree ➡ eval ➡ result
```

<h2 id="license"> 📝 License </h2>

- [License File](./LICENSE)
