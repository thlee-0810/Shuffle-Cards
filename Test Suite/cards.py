'''
This helps to generate text file for testing continuous number of cards.
'''
with open("number_of_cards.txt", 'w') as f:
    for i in range(5000 + 1):
        f.write(str(i) + '\n')
    