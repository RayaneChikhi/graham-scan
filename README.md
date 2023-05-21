Implementation and illustration of the Graham scan algorithm. (Inspired by an entrance exam for ENS)

Enter a list tab of the form [[x coordinates], [y coordinates]]. The program plots the convex hull of this set of points using Graham scan.

Note: It is a known fact that, given A_1,...,A_n n points randomly chosen on the unit circle, the probability of the event "the center O of the circle lies within the convex hull of A_1,..A_n" has probability
      1 - n/(2^{n-1}). You may use my probability simulator toolkit to illustrate this result using various laws to pick A_1,...,A_n.

Here's an example of the code running on the following set of points:

tab = [[0,1,1,4,4,5,5,7,7,8,11,13],[0,4,8,1,4,9,6,-1,2,5,6,1]]


![Figure_1](https://github.com/RayaneChikhi/graham-scan/assets/128234596/3c4cf004-2f3b-472a-8c92-e6705a5c3d1d)
