# Overview

This assessment evaluates your ability to perform the following tasks in accordance with ICTPRG547 Apply advanced programming skills in another language:

 - **Performance elements**:
    - 1.4 Code sorting algorithm using programming techniques
    - 3.2 Detect and resolve errors of syntactical, logical and design origin
    - 3.3 Design and document required tests
    - 4.1 Develop and document solution according to debugging test results

You will demonstrate your performance by providing evidence that you can "code at least one sorting algorithm", and "test and debug the code to resolve errors of a syntactical, logical, or design origin".

To succeed you must use a "systematic, analytical processes in complex, non-routine situations, setting goals, gathering relevant information, and identifying, and evaluating, options against the agreed criteria".

## 2. General instructions

> CRITICAL: Failure to follow these instructions will lead to an NYC

- Copy this file into a `docs` folder in your assessment repo (that is, the repo you created for POR1/POR2)
- Add and commit this file to your repository and associate the tag `por3-start`:
  - Copy and `add` this file to your repository under the `docs` folder
  - `git commit -m "chore: add task overview to my repo"
  - `git tag por3-start`
  - `git push origin main --tags`
  - Optional: you may want to complete this work in a branch
  - On your last commit, add an **annotated** tag `por3-finish`:
    - `git tag -a por3-finish -m "marks my original submission completed in class"`
    - `git push origin main --tags`
- Commit changes after you complete each task
- Push changes to your GitHub repository
- Ensure that your original tests still pass as well as any additional tests
- Ensure you submit your git repo (`.git/`) along with your assessment submission

> **IMPORTANT:** While some aspects of this task are done under exam-like conditions, this is **not** an exam.
> You are _encouraged_ to ask questions of your assessor both about the test itself and its coding requirements. You can also ask your neighbors for help, but you must not copy their work. If you are unsure about anything, ask your assessor.


### 2.1 What if I can't complete this work in class?

It is expected that the majority of this work will be completed in class, under supervision.
Therefore, even if your work is incomplete at the close of class you will need to submit it with:
- The code and `.git/' folder at the state it was in at 17:00 on the day of your class.
- An annotated tag `por3-incomplete` on your last commit
- A comment highlighting that the work is incomplete and what you managed to do
- A completed statement of authenticity (see below)

Submit the work within a week of class. Your assessor will determine if a significant enough portion of the work was done in class. If it is not, you may need to undertake additional validation before a CO is attained.


## 3. Players have scores now

### 3.1. Task: Add scores to players

Add a private instance variable to the Player class that will hold the score (a positive integer value).

Since we want our existing tests to pass, we will make this parameter optional and set a default value of 0.

Provide a getter (property) and a setter method for this value.

> **Recommended:** If you don't already have a `__repr__` method in your Player class, add one now to help with debugging. It should present as follows: `Player(name='Alice', uid='01', score=10)` and ideally get the class name dynamically: `self.__class__.__name__`

#### 3.1.1. Success criteria
You can mark this task as complete when you have (your assessor will use a similar list):
- [x] Correct use of private instance variable
- [x] Score is optional (in the constructor) and defaults to 0
- [x] Use of properties to create a getter and setter
- [x] Raising ValueError if someone attempts to set a non-positive value
- [x] Existing tests pass
- [x] At least one (and ideally only one) commit showing the above changes

## 4. Sorting players

### 4.1. Task: Add unit tests for sorting players

Add the following unit tests to the `test_player.py` file:

```python
def test_sort_players(self):
    players = [Player("Alice", uid='01', score=10), Player("Bob", uid='02', score=5), Player("Charlie", uid='03', score=15)]
    # note: ensure initialization code is valid for **your** implementation.
    # For example, is your parameter called uid? is the first parameter name?

    # do **not** change the following code:
    sorted_players = sorted(players)

    # players must be sorted by score as shown here:
    manually_sorted_players = [Player("Bob", uid='02', score=5), Player("Alice", uid='01', score=10), Player("Charlie", uid='03', score=15)]

   self.assertListEqual(sorted_players, manually_sorted_players)

```

> **Note:** If you have made other changes to the initializer of your player update the above code to reflect this change - you must not make any other changes to the test code above.

### 4.2. Task: Interpret unit tests

What was the outcome of running the above unit test, copy paste the output **for just this particular test** below:

```text
======================================================================
ERROR: test_sort_players (test.player_test.PlayerTest.test_sort_players)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/var/home/lilli/Source/Repos/SRUS-LH-Games/test/player_test.py", line 25, in test_sort_players
    sorted_players = sorted(players)
TypeError: '<' not supported between instances of 'Player' and 'Player'

----------------------------------------------------------------------

```

### 4.3. Success criteria

- [x] Unit test added to `test_player.py`
- [x] Unit test output provided
- [x] Unit test output reflects the error in `sorted(players)` (if you are getting another error read the instructions CAREFULLY)

#### 4.3.1. Question: What dunder method is required for Python to sort players?

The tests checks that calling sorted on a list of players will sort them by score.

What is the **only** magic method that must be implemented in the player class for the `sorted` function to succeed?

**Hint:** if you don't recall this from class, the error message you got when you ran the test will help you.
-------
> The __lt__ magic method is the only one required for python's sorted() function to work, however it is recommended all of the 'rich comparison' operators are implemented so that other built in methods work correctly.
> Source 1: https://docs.python.org/3/library/functions.html#sorted
> Source 2: https://docs.python.org/3/reference/datamodel.html#object.__lt__
-------
#### 4.3.2. Task: Implement the magic method in the Player class

Add a test case to test_player to test the comparison operator you are about to add - ensure you do not test a dunder method directly!

```python
def test_players_can_be_compared_by_score(self):
    # note: ensure initialization code is valid for **your** implementation
    alice = Player("Alice", uid='01', score=10)
    bob = Player("Bob", uid='02', score=5)

    # Add the appropriate expression to the following assert test
    self.assertTrue(<your comparison expression>)
    # or, event better
    self.assert<AppropriateComparisonMethod>(alice, bob)
```

Run the test and confirm that your error resembles the previous error

```text
======================================================================
ERROR: test_players_can_be_compared_by_score (test.player_test.PlayerTest.test_players_can_be_compared_by_score)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/var/home/lilli/Source/Repos/SRUS-LH-Games/test/player_test.py", line 39, in test_players_can_be_compared_by_score
    self.assertLess(bob, alice)
    ~~~~~~~~~~~~~~~^^^^^^^^^^^^
  File "/usr/lib64/python3.14/unittest/case.py", line 1295, in assertLess
    if not a < b:
           ^^^^^
TypeError: '<' not supported between instances of 'Player' and 'Player'

```

- Implement the appropriate magic method in the Player class and ensure you pass this test
- It is likely (indeed desirable) that you still won't pass the `test_sort_players` test
- Commit your changes

#### 4.3.3. Success criteria

- [x] Unit test added to `test_player.py`
- [x] Magic method implemented in `Player` class
- [x] Initial Failed Unit test output provided
- [x] Unit test runs successfully with submitted code
- [x] Dunder method not employed directly
- [x] At least one commit capturing the above changes

#### 4.3.4. Task: Are we sorted yet?

Rerun `test_sort_players` does the test pass? If not, include the output below:

```text
======================================================================
FAIL: test_sort_players (test.player_test.PlayerTest.test_sort_players)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/var/home/lilli/Source/Repos/SRUS-LH-Games/test/player_test.py", line 31, in test_sort_players
    self.assertListEqual(sorted_players, manually_sorted_players)
    ~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Lists differ: [Play[57 chars]id='01', score=10), Player(name='Charlie', uid='03', score=15)] != [Play[57 chars]id='01', score=10), Player(name='Charlie', uid='03', score=15)]

First differing element 0:
Player(name='Bob', uid='02', score=5)
Player(name='Bob', uid='02', score=5)

  [Player(name='Bob', uid='02', score=5),
   Player(name='Alice', uid='01', score=10),
   Player(name='Charlie', uid='03', score=15)]

```

##### 4.3.4.1 Question: why did the equality comparison fail?
Why did the test fail (note: if it doesn't fail, it means there is something you have already done before you were asked to do so - if that's the case, you need to figure out what that is!)?
-------
> While the values of the players are the same, the player objects are not the same.
> So I need to implement __eq__ to compare two objects as equal.
-------
Add the necessary code to the Player class to ensure that the `test_sort_players` test passes.

#### 4.3.5. Success criteria

- [x] Correct explanation of why `test_sort_players` failed/passed
- [x] Correct implementation of the magic method in the `Player` class
- [x] `test_sort_players` passes when run against the submitted code
- [x] At least one commit capturing the above changes

## 5. Implement a custom sorting algorithm

The senior developer on your team believes that a custom sorting algorithm would be more efficient than the built-in `sorted` function (you grit your teeth, sigh, and realize you need this job!).

They have asked you to implement a custom sorting algorithm that will sort a list of players by score.

To help you get started they have provided you with some example code that they wrote in their undergraduate days.

Unless something goes wrong, you will need to remain faithful to the algorithm they have provided - you can change variable names, but you must not change the algorithm itself.

Remember, they wrote it at university, so they probably didn't use PEP8 or adhere to professional coding standards. If only they had gone to TAFE!

```python
def sort_quickly(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = []
    right = []
    for x in arr[1:]:
        if x < pivot:
            left.append(x)
        else:
            right.append(x)
    return sort_quickly(left) + [pivot] + sort_quickly(right)
```

### 5.1. Question: complexity

What is the expected time and space complexity of the above algorithm? You can answer using big O or in plain English but in both cases you MUST justify your answer.

> AVERAGE/EXPECTED TIME COMPLEXITY
> The average time complexity of the algorithm is O(n log n). To explain how much time complexity this algorithm takes, we can multiply the number of recursions by the operations per recursion.
> Number of recursions: The first recursion takes one array, the second recursion takes two arrays, which are (on average) half the size of the original array minus 1 (for the first pivot), the third recursion takes four arrays, which are on average quarter the size of the original array minus 2 (for the last recursion's pivots), and so on until there is no more than one item per array. So the number of recursions is log(n) minus the pivots, which are ignored as we only consider the highest order term of n in big O notation.
> Number of operations in each recursion: The first recursion will have n-1 comparisons, because it compares the pivot against every other item. The second recursion will have n-3 operations, because every item except the pivot from the first and second recursions will be compared against the two new pivots, although it will be split into two sides of the recursion. The next recursion will have n-7 operations and so on, until all items are compared. Since we only consider the highest order term of n in the function, we can say there are n comparisons per recursion.
> The worst case time complexity would occur if the list is already sorted and we choose the largest or smallest item as the pivot each time. In this case, one side of the array will have 0 items and the other will have the remaining n-1 items. In this case there will be n recursions each with n operations, so the worst case is O(n^2).
>
> EXPECTED SPACE COMPLEXITY
> The original array is of length n, which is already held in the heap. The first recursion will allocate each item into one of two arrays which are also stored on the heap, for a total of n-1 items stored. The next recursion will split each into two more arrays minus the pivots, so in that round another n-2 items are stored. Ignoring all but the highest order term of n, the expected space complexity is log n recursions multiplied by n items stored, meaning the space complexity will be (n log n). However, for the worst case scenario where there are n recursions, the space complexity will be n^2. The stack height will add another up to n operations, however this is lower order than (n log n) or n^2 so it can be ignored.
> The quick sort algorithm can be implemented in a more timeand space efficient way than the above.

### 5.2. Task: Implement the custom sorting algorithm

#### 5.2.1. Create a new method in the Player class

Use the sample above (and its algorithm) as a starting point to implement a `classmethod` in the Player class that takes a list of players and returns a list of players sorted by score in **descending** order. Top scores come first!

#### 5.2.2. Create a test cases

Add a separate test case to `test_player.py` to test your custom sorting algorithm

Include your code below:

```python
    @classmethod
    def sort_players(_cls, arr):
        """Accepts an array of Players and returns a sorted array"""
        if len(arr) <= 1:
            return arr
        pivot = arr[0]
        left = []
        right = []
        for x in arr[1:]:
            if x > pivot:
                left.append(x)
            else:
                right.append(x)
        return Player.sort_players(left) + [pivot] + Player.sort_players(right)
```

#### 5.2.3. Success criteria

- [x] Custom sorting algorithm implemented in the `Player` class as `classmethod`
- [x] Custom sorting algorithm sorts in descending order
- [x] Custom sorting algorithm compares players using their score (via the rich comparison operators)
- [x] Custom sorting algorithm tested in `test_player.py` and tests passed
- [x] At least one commit capturing the above changes

### 5.3. Test your custom sorting algorithm at scale

The senior developer is impressed with your work and asks you to test your custom sorting algorithm with a list of 1000 players. They provide you with a script that will generate a list of 1000 players with random scores.

```python
import random
from player import Player


players = [Player(f"Player {i}", uid=f"{i:03}", score=random.randint(0, 1000)) for i in range(1000)]
```

#### 5.3.1. Task: Create a test case to sort 1000 players

Using the code above as a starting point, create a test case to test your custom sort algorithm - you can test it against the `sorted` function to ensure it is working correctly.

Include your test case below:

```python

    def test_sort_1000_players_custom_algorithm(self):
        players = [Player(f"{i:03}", f"Player {i}", player_score=random.randint(0, 1000)) for i in range(1000)]
        # builtin method vs custom
        self.assertEqual(sorted(players, reverse=True), Player.sort_players(players))

```

#### 5.3.2. Success criteria

- [x] Test case added to `test_player.py`
- [x] Test case sorts 1000 players correctly when compared to `sorted` function
- [x] Test case passes when run against the submitted code
- [x] At least one commit capturing the above changes

#### 5.3.3. Task: Testing sorting sorted players

You had a scary thought - and decided to test your custom sorting algorithm against a list of players that are already sorted by score. You are worried that your algorithm might not be efficient in this case.

#### 5.3.4. Task: Create a test case to sort 1000 sorted players

Create a test case that tries to sort 1000 players that are already sorted.

If you get a failure, include the failure below:

```text
RecursionError: maximum recursion depth exceeded
FAILED (errors=1)
```

##### 5.3.4.1 Question: Why does the algorithm fail on presorted values?

Provide a reason why this test failed (if you got a recursion errors, you need to explain **why** that happened with a sorted list, but not an unsorted list).

If your implementation did not fail, you must nevertheless explain why the senior developers algorithm has worse space complexity for presorted values.

> The default maximum recursion limit in python is 1000, and I checked this with sys.getrecursionlimit().
> Source: https://docs.python.org/3/library/sys.html#sys.getrecursionlimit
> In addition to the recursions, python uses some stackframes for running the code itself.
> Source: https://www.reddit.com/r/learnpython/comments/lsr3yw/how_does_the_recursion_limit_work/
> When using a sorted array and a pivot at one end of the array, the array is not partitioned in a balanced way as all items are either larger or smaller than the pivot. as such, the recursion must happen n times, where n is the size of the list. In this case, including stackframes used by python itself and setting up the code, with 1000 items, the 1000 recursion limit is reached.
> On average for an unsorted array, there will be log(n) recursions, so the recursion limit might be reached on a dataset of close to 1,000,000 items but also likely fewer items will reach the recursion limit sometimes.
> In addition after solving the recursion error, the failures are due to items with the same score may be ordered differently in the built in sorted function than the custom function, even if either order is acceptable.

Propose a fix to your sorting algorithm that fixes this issue.

```python
# Fix for the stack overflow is choosing a different pivot:
    def sort_players(_cls, arr):
        """Accepts an array of Players and returns a sorted array"""
        if len(arr) <= 1:
            return arr
        # Choose a pivot near the middle of the dataset.
        # This should work for near-random and already sorted lists.
        pivot_index = int(len(arr)/2)
        pivot = arr[pivot_index]
        left = []
        right = []
        # Sort all but the pivot
        for x in (arr[:pivot_index] + arr[pivot_index+1:]):
            if x < pivot:
                right.append(x)
            else:
                left.append(x)
        return Player.sort_players(left) + [pivot] + Player.sort_players(right)

# Fix for comparing two players are less than (the orders were different but the scores still in order)
    def __lt__(self, other: Player):
        is_lt = False
        if self.score < other.score:
            is_lt = True
        elif self.score == other.score:
            # If the score is the same, compare uid instead
            is_lt = self.uid < other.uid
        return is_lt

```

#### 5.3.5. Success criteria

- [x] Test case added to `test_player.py`
- [x] Test case passes only when changes above are added
- [x] Explanation of why the algorithm fails on presorted values
- [x] Fix to the algorithm provided
- [x] At least one commit capturing the above changes

## 6. Task: Authenticity of in class work

Complete the following snippet before you submit:

```text
I, Lilli Hooper 20175438, completed this work in class 303 and 260, on 7 September and 8 September, under the supervision of Para (and the remainder during my other class).
```

Or (if not completed in class):

```text
I, <name and student number>, completed this work outside of the scheduled hours. I emailed <assessors name>, on <date>, along with my documented reason for non-attendance, and have scheduled a time to meet to discuss my work.

I understand that until I meet my assessor to confirm that this work is a valid and true representation of my abilities to write and debug a sorting algorithm in Python, this submission cannot be considered complete.

```

## 7. Submit your work

- [x] Ensure all tasks are complete and tests pass
- [x] Answer all questions in your own words
- [x] Complete the statement of authenticity
- [x] Include `.git` showing each task committed (you must show at least 5 commits)
- [x] Annotated tag of your last commit as `por3-finish`
- [x] Push your changes to your GitHub repository
- [x] Submit a zip of your repository to the LMS (ensure you do not add the `.venv` or `__pycache__` folders)

---
End of assessment task
