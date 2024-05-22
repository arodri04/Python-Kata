# Python-Kata
This is a start to me doing python katas, I'll save them here. Test change

1: Will you make it?

URL: https://www.codewars.com/kata/5861d28f124b35723e00005e/python

Description:You were camping with your friends far away from home, but when it's time to go back, you realize that your fuel is running out and the nearest pump is 50 miles away! You know that on average, your car runs on about 25 miles per gallon. There are 2 gallons left.
Considering these factors, write a function that tells you if it is possible to get to the pump or not.
Function should return true if it is possible and false if not.

2: Bit Counting(binaryconvert)

URL: https://www.codewars.com/kata/526571aae218b8ee490006f4/solutions/python

Description: Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative. Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

3: Interactive Dictionary

URL: https://www.codewars.com/kata/57a93f93bb9944516d0000c1/solutions/python

Description: In this kata, your job is to create a class Dictionary which you can add words to and their entries.

4: Sum of Digits

URL: https://www.codewars.com/kata/541c8630095125aba6000c00

Description: Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.

5:Descending Order

URL: https://www.codewars.com/kata/5467e4d82edf8bbf40000155/solutions/python

Description: Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

6: Find the odd int

URL: https://www.codewars.com/kata/54da5a58ea159efa38000836/solutions/python

Description: Given an array of integers, find the one that appears an odd number of times. There will always be only one integer that appears an odd number of times.

7: Morse Code

URL: https://www.codewars.com/kata/54b724efac3d5402db00065e/solutions/python

Description: In this kata you have to write a simple Morse code decoder. While the Morse code is now mostly superseded by voice and digital data communication channels, it still has its use in some applications around the world.
The Morse code encodes every character as a sequence of "dots" and "dashes". For example, the letter A is coded as ·−, letter Q is coded as −−·−, and digit 1 is coded as ·−−−−. The Morse code is case-insensitive, traditionally capital letters are used. When the message is written in Morse code, a single space is used to separate the character codes and 3 spaces are used to separate words. For example, the message HEY JUDE in Morse code is ···· · −·−−   ·−−− ··− −·· ·.

NOTE: Extra spaces before or after the code have no meaning and should be ignored.

In addition to letters, digits and some punctuation, there are some special service codes, the most notorious of those is the international distress signal SOS (that was first issued by Titanic), that is coded as ···−−−···. These special codes are treated as single special characters, and usually are transmitted as separate words.

Your task is to implement a function that would take the morse code as input and return a decoded human-readable string.

8: High and Low

URL: https://www.codewars.com/kata/554b4ac871d6813a03000035

Description: In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

9: Calculating with functions

URL: https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/solutions/python

Description:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Division should be integer division. For example, this should return 2, not 2.666666...:

10: Even or Odd

URL: https://www.codewars.com/kata/53da3dbb4a5168369a0000fe/solutions/python

Description: Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

11: Domain Name

URL: https://www.codewars.com/kata/514a024011ea4fb54200004b/python

Description: Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. 

12: Who likes it

URL: https://www.codewars.com/kata/5266876b8f4bf2da9b000362

Description: You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

13: Categorize New Member

URL: https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/python

Description: The Western Suburbs Croquet Club has two categories of membership, Senior and Open. They would like your help with an application form that will tell prospective members which category they will be placed.

To be a senior, a member must be at least 55 years old and have a handicap greater than 7. In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.

14: The Observed PIN

URL: https://www.codewars.com/kata/5263c6999e0f40dee200059d/python

Description:

Alright, detective, one of our colleagues successfully observed our target person, Robby the robber. We followed him to a secret warehouse, where we assume to find all the stolen stuff. The door to this warehouse is secured by an electronic combination lock. Unfortunately our spy isn't sure about the PIN he saw, when Robby entered it.

The keypad has the following layout:

┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┼───┼───┘
    │ 0 │
    └───┘
He noted the PIN 1357, but he also said, it is possible that each of the digits he saw could actually be another adjacent digit (horizontally or vertically, but not diagonally). E.g. instead of the 1 it could also be the 2 or 4. And instead of the 5 it could also be the 2, 4, 6 or 8.

He also mentioned, he knows this kind of locks. You can enter an unlimited amount of wrong PINs, they never finally lock the system or sound the alarm. That's why we can try out all possible (*) variations.

* possible in sense of: the observed PIN itself and all variations considering the adjacent digits

Can you help us to find all those variations? It would be nice to have a function, that returns an array (or a list in Java/Kotlin and C#) of all variations for an observed PIN with a length of 1 to 8 digits. We could name the function getPINs (get_pins in python, GetPINs in C#). But please note that all PINs, the observed one and also the results, must be strings, because of potentially leading '0's. We already prepared some test cases for you.

Detective, we are counting on you!

15: How Good Are You Really

URL: https://www.codewars.com/kata/5601409514fc93442500010b/python

Description:

There was a test in your class and you passed it. Congratulations!

But you're an ambitious person. You want to know if you're better than the average student in your class.

You receive an array with your peers' test scores. Now calculate the average and compare your score!

Return true if you're better, else false!

16: Plays Banjo

URL: https://www.codewars.com/kata/53af2b8861023f1d88000832/python

Description:
Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!

17: IP to int 32

URL: https://www.codewars.com/kata/52ea928a1ef5cfec800003ee/python

Description: 
Take the following IPv4 address: 128.32.10.1. This address has 4 octets where each octet is a single byte (or 8 bits).

1st octet 128 has the binary representation: 10000000
2nd octet 32 has the binary representation: 00100000
3rd octet 10 has the binary representation: 00001010
4th octet 1 has the binary representation: 00000001
So 128.32.10.1 == 10000000.00100000.00001010.00000001

Because the above IP address has 32 bits, we can represent it as the 32 bit number: 2149583361.

Write a function ip_to_int32(ip) ( JS: ipToInt32(ip) ) that takes an IPv4 address and returns a 32 bit number.

18: Naughty Or Nice

URL: https://www.codewars.com/kata/585eaef9851516fcae00004d

Description: In this kata, you will write a function that receives an array of string and returns a string that is either 'naughty' or 'nice'. Strings that start with the letters b, f, or k are naughty. Strings that start with the letters g, s, or n are nice. Other strings are neither naughty nor nice.

If there is an equal amount of bad and good actions, return 'naughty'

19: Is pangram

URL: https://www.codewars.com/kata/545cedaa9943f7fe7b000048

Description: A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.