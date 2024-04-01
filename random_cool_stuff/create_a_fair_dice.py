"""
Given a task() function which is equally probable to return 1 or 2, generate a
fair dice with it

Intuition:

000 - 111
 0  -  7

 But we need only [1,6]

 We can run a loop calling the function task() which returns the bit value
  result =  0
    for i in range(3):
      result = (result << 1) | task()

    # If the result>6, re-roll the dice
    while (result>6):
        result = (result & 7) + task()

    return result

3<<1 => 3 * (2*1) = 6
6<<2 => 6 * (2*2) = 24

25>>1 => 25/(2*1) = 12
25>>2 => 25/(2*2) = 6
"""