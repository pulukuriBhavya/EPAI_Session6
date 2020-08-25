# session6
Session 6 is concentarted on **First Class Functions Part 1**
***
- This project is 2 players playing Poker game. A deck of cards consists of 52 cards (4 suites and 13 values). Each player is given either 3 or 4 or 5 cards, and the winner is choosen among the 2 players
based on the winning rules. There are 10 hierarchial rules among which Royal Flush is the highest and HighF Card is the least.
- 1. Royal Flush
- 2. Straight Flush
- 3. Four of a kind
- 4. Full House
- 5. Flush
- 6. Straight
- 7. Three of a Kind
- 8. Two Pair
- 9. One Pair
- 10.High Card

## Getting Started
***
These instructions will get you a copy of the project up and running on your local machine for development and testing purpose.

### Prerequisites
***
Before string session check if all the required packages (pytest) are installed. Packages can be installed using the following code.
```
 pip install pytest
 ```

### Session 6.py
***

Session6.py implements poker game with 2 players with the help of First Class Functions.

- create_cards_lambda() function creates a deck of cards using lamba, map and zip functions. Input parameters for create_cards_lambda() are values and suits
- create_cards() function creates a deck of cards manually. Input parameters for create_cards() are values and suits
- cards_eval() function takes a set of cards and returns the rank of the set of cards according to the hierarchial order. Input parameters for cards_eval() function is a set of cards
- cards_conversion() function converts special values of cards like king etc to numerical values. Input parameters for cards_conversion() function is a set of cards
- poker() function returns the winner among the two players. Input parameters for poker() function are set of cards of 2 palyers. 

### test_session6.py

***

test_session5.py consists of 26 test cases which needs to be cleared.

- test_fourspace to check for indentation.
- test_function_name_had_cap_letter function name having capital letter.
- test_functions_avaiable to check if all the functions are implemeted.
- test_readme_exists to check if the README file exists
- test_readme_contents to check if the README content is exceding 400 words
- test_readme_file_for_formatting() to check for proper formatting
- test_lamda_manual_check to check if the deck of cards are created correct
- test_create_cards_manual_check to check if the deck of cards are created correct
- test_annotations_poker_check cheks for annotations of poker function
- test_docstring_poker_check checks for docstrings of poker function
- test_docstring_create_cards_check checks for docstrings of create cards function
- test_random_tests_20_check checks if the program gives right winner among the 2 players for 20 random sets of cards
- test_3_card_set checks if the program gives right result for sets of 3 cards 
- test_4_card_set checks if the program gives right result for sets of 4 cards
- test_5_card_set checks if the program gives right result for sets of 5 cards
- test_royal_flush checks for Royal Flush
- test_straight_flush checks for straight flush
- test_four_of_a_kind checks for four of a kind
- test_full_house checks for a full house
- test_flush checks for flush
- test_straight checks for straight
- test_three_of_a_kind checks for three of a kind
- test_two_pair checks for two pairs
- test_one_pair checks for one pair