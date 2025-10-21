### Hexlet tests and linter status:
[![Actions Status](https://github.com/Scopp1337/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Scopp1337/python-project-49/actions)

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=Scopp1337_python-project-49&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=Scopp1337_python-project-49)

[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=Scopp1337_python-project-49&metric=bugs)](https://sonarcloud.io/summary/new_code?id=Scopp1337_python-project-49)

[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=Scopp1337_python-project-49&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=Scopp1337_python-project-49)

[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=Scopp1337_python-project-49&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=Scopp1337_python-project-49)

[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=Scopp1337_python-project-49&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=Scopp1337_python-project-49)

[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=Scopp1337_python-project-49&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=Scopp1337_python-project-49)

[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=Scopp1337_python-project-49&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=Scopp1337_python-project-49)

[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=Scopp1337_python-project-49&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=Scopp1337_python-project-49)

[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=Scopp1337_python-project-49&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=Scopp1337_python-project-49)

[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=Scopp1337_python-project-49&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=Scopp1337_python-project-49)


Demo links

[An example of a brain-calc game](https://asciinema.org/a/syHlfT91JTV2RtVvcyAnqYx8C)

[An example of a brain-even game](https://asciinema.org/a/QfMT4QMOJspQyUzNBFczazzTG)

[An example of a brain-gcd game](https://asciinema.org/a/m22IW8IDP4ycZ9KUfg7IJhrLF)

[An example of a brain-prime game](https://asciinema.org/a/VnilICFQbVdulQIjirPeGecHE)

[An example of a brain-progression game](https://asciinema.org/a/JXliSf8rYwmGCTV3cioY5Z984)


Brain Games - Description of games

1. Brain Even - "Even or odd?"
The essence of the game: Determine whether the proposed number is even or odd.

Task: Answer "yes" if the number is even, or "no" if it is odd.

What trains: Quick determination of the parity of numbers, mathematical intuition

Example: Number 15 → answer "no", number 24 → answer "yes"

2. Brain Calc - "Mathematical calculator"
The essence of the game: Solve a simple arithmetic expression.

Task: Calculate the result of an expression (addition, subtraction, multiplication)

What trains you: Oral counting, knowledge of arithmetic operations

Example: "5 + 3" → answer "8", "10 × 2" → the answer is "20"

3. Brain GCD - "Greatest Common Divisor"
The essence of the game: Find the largest number that divides both proposed numbers without remainder.

Task: Define a node for two numbers

What trains you: Understanding the divisibility of numbers, Euclid's algorithm

Example: Numbers 12 and 18 → NODE = 6

4. Brain Prime - "Simple or compound?"
The essence of the game: Determine whether a number is prime (divisible only by 1 and itself) or composite.

Task: Answer "yes" for prime numbers, "no" for composite numbers

What trains you: Recognizing prime numbers, understanding number theory

Example: Number 17 → "yes", number 15 → "no"

5. Brain Progression - "Arithmetic progression"
The essence of the game: Find the missing number in the arithmetic progression.

Task: Determine which number is hidden behind two dots in the sequence

What trains you: Understanding patterns, working with sequences

Example: "2, 5, 8, .., 14" → missing number 11

The common goal of all games:
Develop logical thinking, mathematical intuition and decision-making speed through a series of fascinating mathematical exercises!

Each game offers 3 rounds, and to win you need to answer all the questions correctly in a row. Perfect for warming up your mind and improving your math skills!


Installation

Clone the repository:

  git clone github.com/Scopp1337/python-project-49.git

Navigate to the project directory:

cd brain-games

Install the dependencies using Poetry:

make install


Launching a Game

To launch a specific game, use the following commands:

Brain Even:

  brain-even

Brain Calc:

  brain-calc

Brain GCD:

  brain-gcd

Brain Progression:

  brain-progression

Brain Prime:

  brain-prime
  

Example Commands

Build the project:

  make build

Install the package:

  make install

Lint the project:

  make lint
  
