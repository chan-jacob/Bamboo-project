# Problem
Consider the following situation: A supplement company has only one product, but it
offers them in a variety of unique packaging sizes indicated by the number of supplied
servings (for example, 10 days, 14 days, 30 days). Depending on the required servings
for each customer, the company combines a variety of its packages to fulfill the
customer's order.

Due to the limited number of packaging sizes available, often the company has to ship
more than the original order volume to fulfill the customer’s request. An order is called
perfectly purchasable if it can be exactly fulfilled with a combination of multiple
packages. For example, assuming the company only offers two different packages for 5
days and 14 days support, an order request for 19 days is perfectly purchasable, but an
order request for 20 days is not. Your task is to write a program that can find the largest
order volume that is NOT perfectly purchasable.

In other words, given a list of positive integer numbers, write a program that returns the
largest number that cannot be expressed as a linear combination of input values with
positive integer weights.

You can work with the programming language of your choice, but using external
libraries/modules are not allowed. Please include an executive summary of the overall
approach as well as test cases considered to solve the problem in your submission.

# Solution
This is a mathematicial problem called Frobenius coin problem. 
Where it state if the input value greatest common divisor is equal to 1, then there is a largest order volumn that is not perforectly purchasable. Else, there would be infinite output. 

## Step 1: Find the greatest common divisor
In the inital approach, I did not have this function in place. And only the function in step 2. But this is needed to confirm that the input has non-perfectly purchasable number to avoid increase in compute.

The Euclidean algorithm is an efficient method for finding the greatest common divisor (GCD) of two numbers. For example, given the example input [14, 5]:

14 divided by 5 has a remainder of 4.
5 divided by 4 has a remainder of 1.
The GCD of 14 and 5 is 1. Therefore, the input has a largest order volume that is not perfectly purchasable. If the GCD is equal to 1, we proceed to find the largest order volume that is not perfectly purchasable. If the GCD is greater than 1, the input can have infinite output, and we return -1 instead.
 
## Step 2: Find the largest number that cannot be expressed as a linear combination
After confirming that the input has a non-perfectly purchasable number, we need to find the maximum amount that is not purchasable.

1. Calculate the Upper Bound Limit:
* Compute the upper bound limit of possible values by max(self.input) * max(self.input).
*  Create a boolean array possible_order of size max_order_volume + 1, initialized to False except for possible_order[0] since an order of 0 is always possible.

* If an order volume i can be expressed as a linear combination of the inputs, set possible_order[i] to True. For example if i = 5, i-5 = 0 possible_order[0] is True therefore possible_order[5] = True.
However i= 11, i-5 = 6 but possible_order[6] is False, therefore 11 = False.

3. Find the Largest Non-Purchasable Order Volume:
* Iterate over each possible order volume from max_order_volume to 0 in reverse to find the largest integer that is False in the possible_order array.

# Testing
This project includes unit test written in pytest. These test covers the following:
1. Empty input: if input is empty it will raise an error
2. Coprime numbers: Testing number that are coprime, it does have Non pursable amount
3. Duplicate numbers: 
4. Mixed of small and large_numbers:
5. Non coprime numbers: 
This solution has a time complexity of O(n * m), 
where n is the maximum possible order volume and m is the number of packaging sizes. The space complexity is O(n).

# Time and Space Complexity
## Time complexity
This program runs in O(n * m), where n is the number of input denominations and m is the maxium order volumn

## Space Complexity
This has space complexity of O(m), where m is the maxium order volumn

# Possible Bug
Upper bound becoming too larger. Since there is not a limit of maxium order volumn. If the input has a large number, it will increase computation.

# Reference
[Greatest Common Divisor Wikipedia](https://en.wikipedia.org/wiki/Greatest_common_divisor)
[Frobenius Coin Problem Wikipedia](https://en.wikipedia.org/wiki/Coin_problem)
