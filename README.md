# Personal Budget Tracker

#### Video Demo: <URL here>

#### Description:

The Personal Budget Tracker is a Python project designed to help users keep track of their money in a simple and organized way. The program allows a user to enter income, enter expenses, view all transactions, and display a budget summary. This project is useful because many people need a basic way to understand how much money they are earning, how much they are spending, and how much money they have left over after expenses.

When the program starts, it displays a menu with five options. The user can add income, add an expense, view transactions, view a budget summary, or exit the program. The menu keeps running until the user chooses to exit. This makes the program easy to use because the user does not have to restart it after each action.

The income feature allows the user to type in a category, a short description, and an amount. For example, a user may enter income from a job, a side job, or a gift. The expense feature works in a similar way, but it records money that has been spent. Expense categories may include food, rent, gas, bills, school supplies, or entertainment. The program checks that the amount entered is a valid number and that it is greater than zero. This helps prevent incorrect data from being saved.

The transaction viewing feature displays every saved transaction. Each transaction includes the date, type, category, description, and amount. This makes it easier for the user to review their financial activity. The budget summary feature calculates total income, total expenses, and the remaining balance. If the user has spent more than they earned, the program prints a warning message. If the user has money left over, the program gives a positive message.

This project includes three main files. The first file is `TermProject.py`, which contains the Python code for the program. This file includes the required `main()` function and several additional functions. The second file is `README.md`, which explains the project, how it works, and the purpose of each file. The third file is `requirements.txt`, which lists any required libraries. This project only uses built-in Python libraries, so no outside libraries are required.

One important design decision was to use functions to organize the program. Instead of placing all of the code in one long section, the program separates tasks into functions such as `add_income()`, `add_expense()`, `view_transactions()`, and `show_summary()`. This makes the code easier to read, test, and update. Another design decision was to save data in a CSV file. A CSV file is simple, readable, and works well for a beginner Python project. It also allows the user’s budget information to remain saved after the program closes.

Overall, this project demonstrates important Python skills such as functions, loops, conditionals, lists, dictionaries, file handling, user input, and error handling. It is more complex than a basic lab assignment because it combines several programming concepts into one working application.

#### Files Included:

- `TermProject.py`: The main Python program file. It contains the menu, functions, calculations, and file-saving features.
- `README.md`: The project documentation file. It explains what the project does, how it works, and why certain design choices were made.
- `requirements.txt`: The dependency file. No external libraries are needed for this project.
- `budget_data.csv`: This file is created automatically when the user saves transactions.

#### How to Run the Project:

1. Download or clone the project folder.
2. Open the folder in a code editor or terminal.
3. Run the program with this command:

```bash
python TermProject.py
```

4. Follow the menu options on the screen.
