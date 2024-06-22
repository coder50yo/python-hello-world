# Hello World Python Project

This is a simple Python project that prints "Hello, world!" to the console. This project is a great starting point for beginners to learn how to create a Python script, set up a Git repository, use a `.gitignore` file, and implement basic unit testing.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Setting Up the Project](#setting-up-the-project)
- [Running the Script](#running-the-script)
- [Running the Tests](#running-the-tests)
- [Explanation of the Code](#explanation-of-the-code)
- [Using `.gitignore`](#using-gitignore)
- [Additional Resources](#additional-resources)

## Prerequisites

- [Python](https://www.python.org/downloads/) installed on your system
- [Git](https://git-scm.com/downloads) installed on your system

## Project Structure

The project has the following structure:

```
hello-world/
│
├── .gitignore
├── hello_world.py
├── test_hello_world.py
└── README.md
```

- `hello_world.py`: The main Python script that prints "Hello, world!".
- `test_hello_world.py`: The unit tests for the main script.
- `.gitignore`: A file specifying which files and directories to ignore in the Git repository.
- `README.md`: A comprehensive tutorial on how to set up and run the project.

## Setting Up the Project

1. **Clone the Repository**

   First, clone the repository to your local machine. Open your terminal and run the following command:

   ```sh
   git clone https://github.com/coder50yo/python-hello-world.git
   ```

2. **Navigate to the Project Directory**

   Change into the project directory:

   ```sh
   cd hello-world
   ```

## Running the Script

To run the script, simply execute the following command in your terminal:

```sh
python3 hello_world.py
```

You should see the following output:

```
Hello, world!
```

## Running the Tests

To run the unit tests, execute the following command in your terminal:

```sh
python3 -m unittest test_hello_world.py
```

You should see output indicating that the tests passed:

```
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

## Explanation of the Code

Let's break down the `hello_world.py` script:

```python
def main():
    return "Hello, world!"

if __name__ == "__main__":
    print(main())
```

- `def main():` defines a function named `main` that returns the string "Hello, world!".
- `if __name__ == "__main__":` checks if the script is being run directly (as opposed to being imported as a module). If it is, it calls the `main()` function and prints its return value.

The `test_hello_world.py` script contains a simple unit test for the `main` function:

```python
import unittest
from hello_world import main

class TestHelloWorld(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main(), "Hello, world!")

if __name__ == "__main__":
    unittest.main()
```

- `import unittest`: Imports the `unittest` module.
- `from hello_world import main`: Imports the `main` function from `hello_world.py`.
- `class TestHelloWorld(unittest.TestCase):` Defines a test case class that inherits from `unittest.TestCase`.
- `def test_main(self):` Defines a test method to test the `main` function.
- `self.assertEqual(main(), "Hello, world!")`: Asserts that the return value of `main` is "Hello, world!".
- `if __name__ == "__main__": unittest.main()`: Runs the unit tests if the script is executed directly.

## Using `.gitignore`

The `.gitignore` file tells Git which files (or patterns) it should ignore. This is useful for excluding temporary files, build artifacts, and other files that are not part of the source code.

Here are some common entries in the `.gitignore` file:

- `__pycache__/`: Python's bytecode cache directory
- `*.pyc`: Compiled Python files
- `env/`, `venv/`: Virtual environment directories

## Additional Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [Git Official Documentation](https://git-scm.com/doc)
- [unittest Documentation](https://docs.python.org/3/library/unittest.html)
