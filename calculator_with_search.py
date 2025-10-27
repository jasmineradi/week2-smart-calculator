# calculator_with_search.py
# Smart calculator with Equation Solver
# Uses search concepts from Chapter 3

import operator

class SmartCalculator:
    """
    A calculator that can solve simple equations using search
    """

    def __init__(self):
        # Create a dictionary of basic math operations
        self.operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
            '^': operator.pow
        }

    def basic_calculate(self, num1, op, num2):
        """
        Perform basic calculation
        """
        if op in self.operations:
            return self.operations[op](num1, num2)
        else:
            raise ValueError("Invalid operation")

    def solve_for_x(self, target, operation, known_value, x_position='left'):
        """
        Solve simple equations like 'x + 5 = 10' or '3 * x = 15'
        Uses a simple search approach to find x
        """
        min_x = -100
        max_x = 100
        step = 0.1
        tolerance = 1e-6

        current_x = min_x
        best_x = None
        best_difference = float('inf')

        while current_x <= max_x:
            # Safely compute result (handle division by zero)
            try:
                if x_position == 'left':
                    result = self.operations[operation](current_x, known_value)   # x op known
                else:
                    result = self.operations[operation](known_value, current_x)   # known op x
            except ZeroDivisionError:
                current_x = round(current_x + step, 10)
                continue

            # Skip NaN/Inf just in case
            if result == float('inf') or result == float('-inf') or result != result:
                current_x = round(current_x + step, 10)
                continue

            # Close enough?
            difference = abs(result - target)
            if difference < tolerance:
                return round(current_x, 6)

            # Track best-so-far
            if difference < best_difference:
                best_difference = difference
                best_x = current_x

            current_x = round(current_x + step, 10)

        return round(best_x, 6) if best_x is not None else None 
    #this function solves for x in simple equations using a search method
    def equation_solver_menu(self):
        """
        Interactive Menu for equation solver
        """
        print("\n" + "=" * 50)
        print("Equation solver (using search)")
        print("=" * 50)
        print("I can solve equations like:")
        print("x + 5 = 10")
        print("x * 3 = 15")
        print("10 - x = 7")
        print("20 / x = 4")

        # Get equation parts from user
        equation = input("\nEnter the equation (like x + 5 = 10): ").strip()
        target = float(input("Enter the number after the equals sign (=): "))
        operation = input("Enter the operation (+, -, *, /): ").strip()
        known_value = float(input("Enter the other number in the equation (the one next to x): "))

        # Ask where x is relative to the operator
        x_position = input("Is x on the left or right of the operator? (left/right): ").strip().lower()

        # Solve for x
        result = self.solve_for_x(target, operation, known_value, x_position)
        # Clean display: show an integer if it’s effectively an integer
        if abs(result - round(result)) < 1e-6: #this works by checking if the difference between result and its rounded value is very small
            result = int(round(result))
        print(f"\n\033[92m✅ Solution found: x = {result}\033[0m")

    def visualize_search(self, target, operation, known_value, x_position='left'): #this function visualizes the search process by showing step by step calculations
        """
        Show the search process step by step
        """
        print("\nVisualizing search process:")
        print(f"Goal: Find x where ", end="")
        if x_position == 'left':
            print(f"x {operation} {known_value} = {target}")
        else:
            print(f"{known_value} {operation} x = {target}")

        # Show first few search steps
        test_values = [-10, -5, 0, 5, 10, 15, 20]
        print("\nTesting values:")
        print("-" * 40)

        for x in test_values:
            if x_position == 'left':
                result = self.operations[operation](x, known_value)
            else:
                result = self.operations[operation](known_value, x)

            distance = abs(result - target)
            if distance < 0.0001:
                print(f"✅ x = {x:6.1f} => Result = {result:6.2f} (Exact match!)")
            else:
                print(f"x = {x:6.1f} => Result = {result:6.1f} [off by {distance:.1f}]")

        print("\n...continuing detailed search...")
        return self.solve_for_x(target, operation, known_value, x_position)


def main():
    """
    Main program loop
    """
    calc = SmartCalculator()

    while True:
        print("\n" + "=" * 50)
        print("Smart Calculator with AI assistance")
        print("=" * 50)
        print("1. Basic Calculation")
        print("2. Solve equation (using search)")
        print("3. See search visualization")
        print("4. About search algorithms")
        print("5. Exit")

        choice = input("\nChoose Option (1-5): ")

        if choice not in ['1', '2', '3', '4', '5']:
            print("\nInvalid choice. Please enter a number between 1 and 5.")
            continue

        if choice == '1':
            num1 = float(input("Enter first number: "))
            op = input("Enter operation (+, -, *, /, ^): ")
            num2 = float(input("Enter second number: "))
            try:
                result = calc.basic_calculate(num1, op, num2)
                print(f"Result: {num1} {op} {num2} = {result}")
            except ValueError as e:
                print(e)

        elif choice == '2':
            calc.equation_solver_menu()

        elif choice == '3':
            print("\nLet's solve: x + 5 = 12")
            result = calc.visualize_search(12, '+', 5, 'left')
            print(f"\nSolution: x = {result}")

        elif choice == '4':
            print("\nAbout Search Algorithms")
            print("-" * 40)
            print("This calculator uses a simple linear search:")
            print("It tries different values of x")
            print("Checks if each value solves the equation")
            print("Keeps track of the best answer")
            print("This is similar to 'brute-force' search")
            print("\nReal search algorithms (chapter 3) are smarter:")
            print("BFS: Explores all possibilities level by level")
            print("DFS: Explores one path deeply before trying others")
            print("A*: Uses heuristics to search more efficiently")

        elif choice == '5':
            confirm = input("\nAre you sure you want to exit? (y/n): ").strip().lower()
            if confirm == 'y':
                print("\nThanks for using Smart Calculator!")
                break
            else:
                print("\nReturning to menu...")
                continue


if __name__ == "__main__":
    main()