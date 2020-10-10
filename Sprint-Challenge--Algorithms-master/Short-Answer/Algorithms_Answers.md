#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Here is the case of **O(n)** (n * n) n times. **While** loop gets bigger as **n** number grows. It will run for a longer period of time as **n** incrcreases.


b) It is a **O(n^2)** complexity. Nested loops depends on the size of **n**. When **n** increases, number of iterations increases as well. Inner iterations will increase outer loop.


c) **O(n)** add bunnies to the Stack.

## Exercise II


**f >= breaks**

**f < not breaks**

**f == number of dropped + broken eggs is minimized**

I would implement a Binary search:

1 2 3 4 5 6 7 8 9

^       ^       ^
First start with middle 5 if it breaks take a middle from 1 to 5, if it doesn't take a middle between 5 and 9. Continue moving until 'not breaks' floor is found. Binary search has **O(log(n))** complexity.
