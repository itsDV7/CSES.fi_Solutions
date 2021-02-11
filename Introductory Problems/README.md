# Introductory Problems

## Problem 1 - Weird Algorithm

Consider an algorithm that takes as input a positive integer n. If n is even, the algorithm divides it by two, and if n is odd, the algorithm multiplies it by three and adds one. The algorithm repeats this, until n is one. For example, the sequence for n = 3 is as follows:<br>
3 → 10 → 5 → 16 → 8 → 4 → 2 → 1<br>
Your task is to simulate the execution of the algorithm for a given value of n.

Input<br>
The only input line contains an integer n.

Output<br>
Print a line that contains all values of n during the algorithm.

Constraints<br>
1 ≤ n ≤ 10<sup>6</sup>

Example<br>
Input:
```
3
```
Output:
```
3 10 5 16 8 4 2 1
```

### [View Solution](https://github.com/itsDV7/CSES.fi_Solutions/blob/main/Introductory%20Problems/Weird%20Algorithm.py)

## Problem 2 - Missing Number

You are given all numbers between 1, 2 , …, n except one. Your task is to find the missing number.

Input<br>
The first input line contains an integer n.<br>
The second line contains n − 1 numbers. Each number is distinct and between 1 and n (inclusive).

Output<br>
Print the missing number.

Constraints<br>
2 ≤ n ≤ 2⋅10<sup>5</sup>

Example<br>
Input:
```
5
2 3 1 5
```

Output:
```
4
```

### [View Solution](https://github.com/itsDV7/CSES.fi_Solutions/blob/main/Introductory%20Problems/Missing%20Number.py)

## Problem 3 - Repetitions

You are given a DNA sequence: a string consisting of characters A, C, G, and T. Your task is to find the longest repetition in the sequence. This is a maximum-length substring containing only one type of character.

Input<br>
The only input line contains a string of n characters.

Output<br>
Print one integer: the length of the longest repetition.

Constraints<br>
1 ≤ n ≤ 10<sup>6</sup>

Example<br>
Input:
```
ATTCGGGA
```
Output:
```
3
```

### [View Solution](https://github.com/itsDV7/CSES.fi_Solutions/blob/main/Introductory%20Problems/Repetitions.py)

## Problem 4 - Increasing Array

You are given an array of n integers. You want to modify the array so that it is increasing, i.e., every element is at least as large as the previous element.<br>
On each move, you may increase the value of any element by one. What is the minimum number of moves required?

Input<br>
The first input line contains an integer n: the size of the array.<br>
Then, the second line contains n integers x1 , x2, …, xn: the contents of the array.

Output<br>
Print the minimum number of moves.

Constraints<br>
1 ≤ n ≤ 2⋅10<sup>5</sup><br>
1 ≤ xi ≤ 10<sup>9</sup>

Example<br>
Input:
```
5
3 2 5 1 7
```
Output:
```
5
```

### [View Solution](https://github.com/itsDV7/CSES.fi_Solutions/blob/main/Introductory%20Problems/Increasing%20Array.py)

## Problem 5 - Permutations

A permutation of integers 1, 2, …, n is called beautiful if there are no adjacent elements whose difference is 1.<br>
Given n, construct a beautiful permutation if such a permutation exists.

Input<br>
The only input line contains an integer n.

Output<br>
Print a beautiful permutation of integers 1, 2, …, n. If there are several solutions, you may print any of them. If there are no solutions, print "NO SOLUTION".

Constraints<br>
1 ≤ n ≤ 10<sup>6</sup>

Example 1<br>
Input:
```
5
```
Output:
```
4 2 5 3 1
```
Example 2<br>
Input:
```
3
```
Output:
```
NO SOLUTION
```

### [View Solution](https://github.com/itsDV7/CSES.fi_Solutions/blob/main/Introductory%20Problems/Permutations.py)

## Problem 6 - Number Spiral

A number spiral is an infinite grid whose upper-left square has number 1. Here are the first five layers of the spiral:<br>

![Image - first five layers of the spiral](https://cses.fi/file/bba36f2601b99c7edc15865aa2a49e680a271075f30e86aa0e4e18d00a779c21)<br>

Your task is to find out the number in row y and column x.

Input<br>
The first input line contains an integer t: the number of tests.<br>
After this, there are t lines, each containing integers y and x.

Output<br>
For each test, print the number in row y and column x.

Constraints<br>
1 ≤ t ≤ 10<sup>5</sup><br>
1 ≤ y , x ≤ 10<sup>9</sup>

Example<br>
Input:
```
3
2 3
1 1
4 2
```

Output:
```
8
1
15
```

### [View Solution](https://github.com/itsDV7/CSES.fi_Solutions/blob/main/Introductory%20Problems/Number%20Spiral.py)

## Problem 7 - Two Knights

Your task is to count for k = 1, 2, …, n the number of ways two knights can be placed on a k×k chessboard so that they do not attack each other.

Input<br>
The only input line contains an integer n.

Output<br>
Print n integers: the results.

Constraints<br>
1 ≤ n ≤ 10000

Example<br>
Input:
```
8
```
Output:
```
0
6
28
96
252
550
1056
1848
```

### [View Solution](https://github.com/itsDV7/CSES.fi_Solutions/blob/main/Introductory%20Problems/Two%20Knights.py)

## Problem 8 - Two Sets

Your task is to divide the numbers 1, 2 , …, n into two sets of equal sum.

Input<br>
The only input line contains an integer n.

Output<br>
Print "YES", if the division is possible, and "NO" otherwise.<br>
After this, if the division is possible, print an example of how to create the sets. First, print the number of elements in the first set followed by the elements themselves in a separate line, and then, print the second set in a similar way.

Constraints<br>
1 ≤ n ≤ 10<sup>6</sup>

Example 1<br>
Input:
```
7
```
Output:
```
YES
4
1 2 4 7
3
3 5 6
```

Example 2<br>
Input:
```
6
```
Output:
```
NO
```

### [View Solution](https://github.com/itsDV7/CSES.fi_Solutions/blob/main/Introductory%20Problems/Two%20Sets.py)

## Problem 9 - Bit Strings

Your task is to calculate the number of bit strings of length n.<br>
For example, if n = 3, the correct answer is 8, because the possible bit strings are 000, 001, 010, 011, 100, 101, 110, and 111.

Input<br>
The only input line has an integer n.

Output<br>
Print the result modulo 10<sup>9</sup> + 7.

Constraints<br>
1 ≤ n ≤ 10<sup>6</sup>

Example<br>
Input:
```
3
```
Output:
```
8
```

### [View Solution](https://github.com/itsDV7/CSES.fi_Solutions/blob/main/Introductory%20Problems/Bit%20Strings.py)

## Problem 10 - Trailing Zeros

Your task is to calculate the number of trailing zeros in the factorial n!.<br>
For example, 20! = 2432902008176640000 and it has 4 trailing zeros.

Input<br>
The only input line has an integer n.

Output<br>
Print the number of trailing zeros in n!.

Constraints<br>
1 ≤ n ≤ 10<sup>9</sup>

Example<br>
Input:
```
20
```
Output:
```
4
```

### [View Solution](https://github.com/itsDV7/CSES.fi_Solutions/blob/main/Introductory%20Problems/Trailing%20Zeros.py)

## Problem 11 - Coin Piles

You have two coin piles containing a and b coins. On each move, you can either remove one coin from the left pile and two coins from the right pile, or two coins from the left pile and one coin from the right pile.<br>
Your task is to efficiently find out if you can empty both the piles.

Input<br>
The first input line has an integer t: the number of tests.<br>
After this, there are t lines, each of which has two integers a and b: the numbers of coins in the piles.

Output<br>
For each test, print "YES" if you can empty the piles and "NO" otherwise.

Constraints<br>
1 ≤ t ≤ 10<sup>5</sup><br>
0 ≤ a, b ≤ 10<sup>9</sup>

Example<br>
Input:
```
3
2 1
2 2
3 3
```
Output:
```
YES
NO
YES
```

### [View Solution](https://github.com/itsDV7/CSES.fi_Solutions/blob/main/Introductory%20Problems/Coin%20Piles.py)

## Problem 12 - Palindrome Reorder

Given a string, your task is to reorder its letters in such a way that it becomes a palindrome (i.e., it reads the same forwards and backwards).

Input<br>
The only input line has a string of length n consisting of characters A – Z.

Output<br>
Print a palindrome consisting of the characters of the original string. You may print any valid solution. If there are no solutions, print "NO SOLUTION".

Constraints<br>
1 ≤ n ≤ 10<sup>6</sup>

Example<br>
Input:
```
AAAACACBA
```
Output:
```
AACABACAA
```

### [View Solution](https://github.com/itsDV7/CSES.fi_Solutions/blob/main/Introductory%20Problems/Palindrome%20Reorder.py)

## Problem 13 - Gray Code

A Gray code is a list of all 2n bit strings of length n, where any two successive strings differ in exactly one bit (i.e., their Hamming distance is one).<br>
Your task is to create a Gray code for a given length n.

Input<br>
The only input line has an integer n.

Output<br>
Print 2n lines that describe the Gray code. You can print any valid solution.

Constraints<br>
1 ≤ n ≤ 16

Example<br>
Input:
```
2
```
Output:
```
00
01
11
10
```

### [View Solution](https://github.com/itsDV7/CSES.fi_Solutions/blob/main/Introductory%20Problems/Gray%20Code.py)

## Problem 14 - Tower of Hanoi

The Tower of Hanoi game consists of three stacks (left, middle and right) and n round disks of different sizes. Initially, the left stack has all the disks, in increasing order of size from top to bottom.<br>
The goal is to move all the disks to the right stack using the middle stack. On each move you can move the uppermost disk from a stack to another stack. In addition, it is not allowed to place a larger disk on a smaller disk.<br>
Your task is to find a solution that minimizes the number of moves.

Input<br>
The only input line has an integer n: the number of disks.

Output<br>
First print an integer k: the minimum number of moves.<br>
After this, print k lines that describe the moves. Each line has two integers a and b: you move a disk from stack a to stack b.

Constraints<br>
1 ≤ n ≤ 16

Example<br>
Input:
```
2
```
Output:
```
3
1 2
1 3
2 3
```

### [View Solution](https://github.com/itsDV7/CSES.fi_Solutions/blob/main/Introductory%20Problems/Tower%20of%20Hanoi.py)

## Problem 15 - Creating Strings

Given a string, your task is to generate all different strings that can be created using its characters.

Input<br>
The only input line has a string of length n. Each character is between a – z.

Output<br>
First print an integer k: the number of strings. Then print k lines: the strings in alphabetical order.

Constraints<br>
1 ≤ n ≤ 8

Example<br>
Input:
```
aabac
```
Output:
```
20
aaabc
aaacb
aabac
aabca
aacab
aacba
abaac
abaca
abcaa
acaab
acaba
acbaa
baaac
baaca
bacaa
bcaaa
caaab
caaba
cabaa
cbaaa
```

### [View Solution](https://github.com/itsDV7/CSES.fi_Solutions/blob/main/Introductory%20Problems/Creating%20Strings.py)

## Problem 16 - Apple Division

There are n apples with known weights. Your task is to divide the apples into two groups so that the difference between the weights of the groups is minimal.

Input<br>
The first input line has an integer n: the number of apples.<br>
The next line has n integers p1, p2, …, pn: the weight of each apple.

Output<br>
Print one integer: the minimum difference between the weights of the groups.

Constraints<br>
1 ≤ n ≤ 20<br>
1 ≤ p<sub>i</sub> ≤ 10<sup>9</sup>

Example<br>
Input:
```
5
3 2 7 4 1
```
Output:
```
1
```
Explanation: Group 1 has weights 2, 3 and 4 (total weight 9), and group 2 has weights 1 and 7 (total weight 8).

### [View Solution](https://github.com/itsDV7/CSES.fi_Solutions/blob/main/Introductory%20Problems/Apple%20Division.py)

## Problem 17 - Chessboard and Queens

## Problem 18 - Digit Queries

Consider an infinite string that consists of all positive integers in increasing order:

12345678910111213141516171819202122232425...

Your task is to process q queries of the form: what is the digit at position k in the string?

Input<br>
The first input line has an integer q: the number of queries.<br>
After this, there are q lines that describe the queries. Each line has an integer k: a 1-indexed position in the string.

Output<br>
For each query, print the corresponding digit.

Constraints<br>
1≤q≤1000<br>
1≤k≤10<sup>18</sup>

Example<br>
Input:
```
3
7
19
12
```
Output:
```
7
4
1
```

### [View Solution](https://github.com/itsDV7/CSES.fi_Solutions/blob/main/Introductory%20Problems/Digit%20Queries.py)

## Problem 19 - Grid Paths
