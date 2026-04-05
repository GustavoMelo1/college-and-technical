# Algorithm Assignment - Integer Divisors Search

This project was developed for the Algorithms course and focuses on programming logic, file handling, and search optimization.

## Objective
The script receives integers greater than 1 and identifies the first pair of divisors (a, b) such that a * b = n. If the number is prime, the returned pair will be (1, n). At the end of the execution, the results are exported to a .txt file formatted as CSV.

## Project Structure
The repository contains two versions of the same logic, demonstrating different performance approaches:

1. **app.py (Optimized Version):**
   - Performs the divisor search up to the square root of the number (sqrt(n)).
   - More efficient for large numbers as it drastically reduces the number of iterations required.

2. **app2.py (Educational Version):**
   - Performs the search up to half of the number (n / 2).
   - Focused on logical clarity for academic purposes.

## Tech Stack and Concepts
- Language: Python 3
- Persistence: Text file manipulation (.txt / .csv)
- Error Handling: try/except blocks to validate user input.
- Optimization: Use of mathematical logic to reduce search complexity.

## How to run
1. Run the script: `python app.py`
2. Enter the desired numbers as prompted in the terminal.
3. Type -1 to exit and generate the 'atividade-gustavomelooliveira.txt' report.
