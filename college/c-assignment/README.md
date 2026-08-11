# C Assignment - Product Registration and Discount

This project was developed for the college course covering the C language and focuses on structs, pointers, and pass-by-reference.

## Objective
The program registers a product (name, code, and price) and applies a discount percentage entered by the user, updating and displaying the product's data afterwards.

## Project Structure
- **trabalhofaculdadeestoque.c:** Defines the `Produto` struct and the `aplicarDesconto` function, which receives a pointer to the struct to apply the discount by reference.

## Tech Stack and Concepts
- Language: C
- Data Structures: `struct` for grouping product fields.
- Pointers: Pass-by-reference using the `->` operator to modify the struct in place.
- I/O: `scanf`/`printf` for interactive terminal input and output.

## How to run
1. Compile the program: `gcc trabalhofaculdadeestoque.c -o estoque`
2. Run the executable: `./estoque`
3. Enter the product name, code, and original price when prompted.
4. Enter the discount percentage to see the updated data.
