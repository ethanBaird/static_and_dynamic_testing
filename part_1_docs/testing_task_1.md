### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    # cannot use assignment operator to check equality, '==' required.
    if card.value = 1:
      return True
    # line should end with colon
    else
      return False
   

  # keywork dif does not exist, should be def
  # comma seperator missing where defining parameters, should be (self, card1, card2)
  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    # card variable undefinined, should be 'card1'
    return card
  else:
    return card2
  # missing return for instance where cards have the same value
  

# missing indentation, method not definined in class CardGame
def cards_total(self, cards):
  # total variable not assigned a value, should begin at 0 'total = 0'
  total
  for card in cards:
    total += card.value
    # return statement should be written outside the loop, in this case it will stop the function after checking only the first card object in the list
    return "You have a total of" + total
  
```
