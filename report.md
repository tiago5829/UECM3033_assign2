UECM3033 Assignment #2 Report
========================================================

- Prepared by: ** Yang Guang Tsong **
- Tutorial Group: T2

--------------------------------------------------------

## Task 1 --  $LU$ Factorization or SOR method

The reports, codes and supporting documents are to be uploaded to Github at: 

[https://github.com/your_github_id/UECM3033_assign1](https://github.com/your_github_id/UECM3033_assign1)

Explain your selection criteria here.

The condition is set to be np.count_nonzero(A) > 1/2*len(A). If the none zero elements in matrix A is greater than half of the length of matrix A, it will perform LU factorization, else it will perform SOR method. 

Explain how you implement your `task1.py` here.

First of all, we make a self-defined funtion lu. It is for solving the LU. Then, we make another self-defined duntion sor. We set a iteration limit as 10 and initiate omega as 1.03. The length of A is use len.
Sparse matrix is a matrix which the most elements are zero. If the matrix is most consist of most zero matrix, it is more accurate that use SOR to solve it. We use np.array to make the A and b to be a matrix, and use astype float to convert it to float. Then, used np.linalg.solve(A,b) and solve(A,b) to check with the condition. Use print() to display the answer. 

---------------------------------------------------------

## Task 2 -- SVD method and image compression

Put here your picture file (Lenna.png)

![Lenna.png](Lenna.png)

How many non zero element in $\Sigma$?

Put here your lower and better resolution pictures. Explain how you generate
these pictures from `task2.py`.

What is a sparse matrix?


-----------------------------------

<sup>last modified: change your date here</sup>
