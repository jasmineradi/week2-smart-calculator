# week2-smart-calculator
This project creates a calculator that uses search to solve simple equations and practice using GitHub Copilot effectively. This project combines practical coding with search algorithm concepts.

# Smart Calculator with Search
## Features
- Basic arithmetic operations
- Equation solver using search algorithms
- Visualization of search process
- Interactive menu system

## How Search Works in This Calculator
The Smart Calculator works by letting you perform normal math or solve for an unknown value, x, in simple equations. When solving for x, it uses a search algorithm that tries many possible numbers for x (from –100 to 100) until it finds one that makes the equation true. This process is called a brute-force search, because it checks each option step by step. Once it finds a number close enough to the correct answer, it returns that as the solution.

## How to Run
1. Clone the repository
2. Run: `python calculator_with_search.py`
3. Follow the menu options

## Sample Equations to Try
- x + 5 = 10 (answer: 5)
- x * 3 = 21 (answer: 7)
- 100 - x = 75 (answer: 25)

## What I Learned About Search
I learned that Brute Force Search, Depth-First Search, A* are all smart algorithms that look for the best path forward. Additionally, I learned that search algorithms are a way for computers to find answers by exploring varying possibilities step-by-step. In this assignment, I learned that (especially for this assignment) Brute-force search tries every possible value until it finds one that works and makes the equation true. Overall, computers use BFS, A* and DFS to find the best possible solutions to equations using differing techniques. BFS looks for the shortest path but will use more memory, while DFS explores one specific path as deeply as possible before it will back up, and lastly A* will try to find not only the best but fastest path to the goal.

## How the Code Works
The main file, `calculator_with_search.py`, contains a `SmartCalculator` class that organizes all the calculator’s functions.  

- The `__init__` method sets up a dictionary of math operations (`+`, `-`, `*`, `/`, `^`) so they can be easily called.  

- The `basic_calculate()` method performs normal math by looking up the correct operation from that dictionary.  

- The `solve_for_x()` method uses a **brute-force search** to test many possible values of `x` until the equation becomes true. It includes protection for divide-by-zero errors and rounds the answer neatly.  

- The `equation_solver_menu()` function interacts with the user, asking for input (the equation, operation, known number, and side of x) and displays the final answer.  

- The `visualize_search()` function shows how the search algorithm checks different `x` values before finding the best one.  

- Finally, the `main()` loop runs the menu so the user can choose between basic calculation, solving equations, or learning about search algorithms.