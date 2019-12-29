# Shuffle Cards
Compute the number of rounds it takes for the deck to return to its original order.

This is a test suite that helps you to find how many rounds needed to restore a pile of cards after shuffled.

1. Pull a card from the top of pile A, and put on pile B
2. Pull a card from the top of pile A, and put it in the bottom of pile A
3. Repeat steps 1 & 2 until pile A is empty.
This counts as one round.

Fixed 2 bugs in the original shuffle.py.
Refer to line 54 and 89.

## Testing Environment
Python version: `3.7.6`

## Code Organization  
```
shuffle.py                 -- Shulffing the deck and return rounds to restore  
verify.py                  -- Run the test cases  
cards.py                   -- Generate continuous number in number_of_cards.txt  
test_data.txt              -- sample test data  
test_data_result.txt       -- sample test data result  
number_of_cards_result.txt -- Rounds needed to restore for continuous number of cards result  
```

## Usage
Run verify.py to test sample test_data.txt and see the result at test_data_result.txt  
or  
Use command line and follow the command:  
	```$Usage: shuffle.py <deck size>```  
or  
Generate your own test data followed the fomat in `test_data.txt`.
Each row in the text file should only include one test case.
