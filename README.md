[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=14052623&assignment_repo_type=AssignmentRepo)
# Homework 5

Hello everyone.

As you know, the midterm is coming up. This repository contains exercises designed to help you prepare for it. The midterm will focus on solving logic problems and using lists in Python. 

Good luck 🍀!

<br>

## Reminders

- There are **7** exercises in total to complete.

- Make sure to read through the instructions carefully and run 
  `pytest yourTestNumber.py` to check that your answers are correct.

  Example: If you want to check if you are correct for Exercise 1, you run `pytest test1.py`

- Include a basic UI that is able to handle user input
  (loops are optional)

- Be creative, but remember, the main focus is on understanding the code logic. 

<br>

## Exercises

### Exercise 1: Duplicate Odd Numbers
---

You are asked to create a function that can duplicate the odd numbers in a list. Inside the function, you will also need to include logic that handles cases outside of just duplicating odd numbers to make sure you understand how the function's logic works. 

<br>

Please make sure to include **comments** to explain your code logic and review the test cases under `test1.py` to make sure these are addressed in your function.

<br>

### Exercise 2: Filter Non-Prime Numbers
---

In this task, you will make a function that will use a given list and output the numbers that aren't prime. 

<br>

Please make sure to include **comments** to explain your code logic and review the test cases under `test2.py` to make sure these are addressed in your function. If you are unsure about what a prime number is please refer to the reference below.

<br>

**Reference:** [What is a prime number?](https://www.splashlearn.com/math-vocabulary/algebra/prime-number)

<br>

### Exercise 3: Multiply List
---

For this exercise, you will be multiplying all of the given numbers from a list and the returning the output. 

<br>

Please make sure to include **comments** to explain your code logic and review the test cases under `test3.py` to make sure these are addressed in your function.

<br>

### Exercise 4: Pig Latin Translator
---

You will be creating a function to translate Pig Latin and it should be able to handle uppercase as well as lowercase letters.

<br>

These are the rules of Pig Latin:

1) If a word has a vowel **(A, E, I, O, U)** at the beginning, add **way** to the end.
   
   Example: `ant` -> `antway`

2) If a word has a consonant **(any letter that is not a vowel)** at the beginning, move the first letter to the end add **ay** to the end.
   
   Example: `cat` -> `atcay`

<br>

Please make sure to include **comments** to explain your code logic and review the test cases under `test4.py` to make sure these are addressed in your function.

<br>

**Reference:** [What is Pig Latin?](https://www.geeksforgeeks.org/encoding-word-pig-latin/)

<br>

### Exercise 5: Rhyming List
---

In this exercise, you will be given a list of words and a variable. Your task is to create a function that counts how many times the given variable rhymes with words in the list.

<br>

Example:

`my_list = ["need", "feed", "apple", "deed"]`
`word = "weed"`

In this example, the output should be **2** because weed rhymes with only 3 words in the list (excluding apple).

<br>

Please make sure to include **comments** to explain your code logic and review the test cases under `test5.py` to make sure these are addressed in your function.

<br>

**Reference:** [What is a rhyme?](https://www.grammarly.com/blog/rhyming-words/)

<br>

### Exercise 6: Identifying Patterns
---

You will be using math to determine the most common factor of a list. The output should be an integer.

<br>

Example: `my_list = [12, 18, 24]`

In the example, the function should return `6` because `6` is the most common factor for all the numbers in the list.


<br>

Please make sure to include **comments** to explain your code logic and review the test cases under `test6.py` to make sure these are addressed in your function.

<br>

**Reference:** [How do we find the most common factor in math?](https://www.splashlearn.com/math-vocabulary/fractions/common-factor)

<br>

### Exercise 7: Finding Missing Numbers
---

You have been given a list with missing numbers. Your task is to create a function that fills in what is missing.

<br>

Here's what your function should do:

1) Loop over the list, checking for gaps between numbers.

2) If a gap exists, return the missing number(s).
   For example, if the list is [1, 3, 4], the function should return `2`.

3) If there are no gaps between the list, the function should return nothing.
   For example, if the list is [1, 2, 3], the function should return `0`.

<br>

Please make sure to include **comments** to explain your code logic and review the test cases under `test7.py` to make sure these are addressed in your function.
