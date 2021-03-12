# Sorting and Searching

## Problem 1 - Distinct Numbers

You are given a list of n integers, and your task is to calculate the number of distinct values in the list.

Input

The first input line has an integer n: the number of values.

The second line has n integers x1,x2,…,xn.

Output

Print one integers: the number of distinct values.

Constraints<br>
1≤n≤2⋅10<sup>5</sup><br>
1≤xi≤10<sup>9</sup><br>

Example<br>
Input:
```
5
2 3 2 2 3
```
Output:
```
2
```

### [View Solution](https://github.com/itsDV7/CSES.fi_Solutions/blob/main/Sorting%20and%20Searching/Distinct%20Numbers.py)

## Problem 2 - Appartments

There are n applicants and m free apartments. Your task is to distribute the apartments so that as many applicants as possible will get an apartment.

Each applicant has a desired apartment size, and they will accept any apartment whose size is close enough to the desired size.

Input

The first input line has three integers n, m, and k: the number of applicants, the number of apartments, and the maximum allowed difference.

The next line contains n integers a1,a2,…,an: the desired apartment size of each applicant. If the desired size of an applicant is x, he or she will accept any apartment whose size is between x−k and x+k.

The last line contains m integers b1,b2,…,bm: the size of each apartment.

Output

Print one integer: the number of applicants who will get an apartment.

Constraints<br>
1≤n,m≤2⋅10<sup>5</sup><br>
0≤k≤10<sup>9</sup><br>
1≤ai,bi≤10<sup>9</sup><br>

Example<br>
Input:
```
4 3 5
60 45 80 60
30 60 75
```
Output:
```
2
```

### [View Solution](https://github.com/itsDV7/CSES.fi_Solutions/blob/main/Sorting%20and%20Searching/Apartments.py)

## Problem 3 - Ferris Wheel

There are n children who want to go to a Ferris wheel, and your task is to find a gondola for each child.

Each gondola may have one or two children in it, and in addition, the total weight in a gondola may not exceed x. You know the weight of every child.

What is the minimum number of gondolas needed for the children?

Input

The first input line contains two integers n and x: the number of children and the maximum allowed weight.

The next line contains n integers p1,p2,…,pn: the weight of each child.

Output

Print one integer: the minimum number of gondolas.

Constraints<br>
1≤n≤2⋅10<sup>5</sup><br>
1≤x≤10<sup>9</sup><br>
1≤pi≤x

Example<br>
Input:
```
4 10
7 2 3 9
```
Output:
```
3
```
### [View Solution](https://github.com/itsDV7/CSES.fi_Solutions/blob/main/Sorting%20and%20Searching/Ferris%20Wheel.py)

## Problem 4 - Concert Tickets

There are n concert tickets available, each with a certain price. Then, m customers arrive, one after another.

Each customer announces the maximum price he or she is willing to pay for a ticket, and after this, they will get a ticket with the nearest possible price such that it does not exceed the maximum price.

Input

The first input line contains integers n and m: the number of tickets and the number of customers.

The next line contains n integers h1,h2,…,hn: the price of each ticket.

The last line contains m integers t1,t2,…,tm: the maximum price for each customer.

Output

Print, for each customer, the price that they will pay for their ticket. After this, the ticket cannot be purchased again.

If a customer cannot get any ticket, print −1.

Constraints<br>
1≤n,m≤2⋅10<sup>5</sup><br>
1≤hi,ti≤10<sup>9</sup><br>

Example<br>
Input:
```
5 3
5 3 7 8 5
4 8 3
```
Output:
```
3
8
-1
```

### [View Solution]()
