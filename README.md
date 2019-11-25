Finish all the hands on sessions. Where applicable, make a python program with
the solution and add it to this repository.

Next, add a solution file for each exercise.

# 1. Iterate over a list

First we are going to make a list and fill it with a simple sequence. Then we
are going to use this list to print something.
- Make a list containing the numbers 0, 1, ... 9.
- Print the last 10 lines of the song ''99 bottles of beer'' using this list.

# 2. Analyse a repeat structure

We are going to make a repeating DNA sequence and extract some subsequences
from it.
- Make a short tandem repeat that consists of three "ACGT" units and five
"TTATT" units.
- Print all suffixes of the repeat structure.
  - **Note**: A suffix is an ending. For example, the word "spam" has five
  suffixes: "spam", "pam", "am", "m" and "".
- Print all substrings of length 3.
- Print all unique substrings of length 3.

**Hint**: All elements in a set are unique.

# 3. FizzBuzz

Write a program that prints the numbers from 1 to 100.
But for multiples of three print "Fizz" instead of the
number and for the multiples of five print “Buzz”.
For numbers which are multiples of both three and five print “FizzBuzz”.

# 4. Combining lists

Calculate all coordinates of the line x=y with x < 100.
- **Note**: This is the sequence (0, 0), (1, 1), ... (99, 99)

# 5. Dictionaries

We are going to store the output of a function (f(x)=x2) together with its
input in a dictionary.
- Make a dictionary containing all squares smaller than 100.
- Print the content of this dictionary in english, e.g., "4 is the square of 2".


# 5. Nested dictionaries

Assume a dictionary that has country names as keys and as values another
dictionary with the following keys: continent, capital, population. Example:

    {
      'The Netherlands': {
        'capital': 'Amsterdam',
        'population': 17283008,
        'continent': 'Europe',
      },
      'France': {
        'capital': 'Paris',
        'population': 67186638,
        'continent': 'Europe',
      },
      'USA': {
        'capital': 'Washington, D.C.',
        'population': 327167434,
        'continent': 'North America',
      }
    }

- Print the country with the largest population (both its name and its population).
- Print how many countries are from a particular continent, which is introduced
by the user.
- Allow for user input to add new countries in the dictionary.
