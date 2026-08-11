# Technical Test - Regression Model Evaluation

This project is a technical assessment focused on evaluating a regression model's predictions against a trained baseline using the R² metric.

## Objective
The script loads a time-indexed dataset, engineers date-based features (month, quarter, year), trains a `GradientBoostingRegressor` on the rows without an existing prediction, and compares its R² score against the R² of the dataset's own `prediction` column.

## Project Structure
- **testr2.py:** Loads and prepares the data, trains the model, and prints both R² scores.
- **dados_analise_process_seletivo.csv:** Source dataset with `period`, `target`, and `prediction` columns.
- **requirements.txt:** Python dependencies (pandas, scikit-learn).

## Tech Stack and Concepts
- Language: Python 3
- Data Handling: pandas (datetime parsing, sorting, feature engineering).
- Machine Learning: scikit-learn `GradientBoostingRegressor` and `r2_score`.

## How to run
1. Create and activate a virtual environment.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the script: `python testr2.py`
4. The R² scores for the existing predictions and the trained model will be printed to the terminal.
