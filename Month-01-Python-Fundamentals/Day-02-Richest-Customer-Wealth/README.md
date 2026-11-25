# Day 02 - Richest Customer Wealth

## Problem
**LeetCode 1672 - Richest Customer Wealth**

Given a 2D list `accounts`, each row represents a customer and each value represents the money in a bank account.

The goal is to find the customer who has the maximum total wealth.

## Example

**Input:**
```python
accounts = [[1, 5], [7, 3], [3, 5]]
```

**Output:**
```python
10
```

**Explanation:**

- Customer 1: 1 + 5 = 6
- Customer 2: 7 + 3 = 10
- Customer 3: 3 + 5 = 8

The maximum wealth is 10.

## Approach

- Use a nested loop to iterate through each customer and their bank accounts.
- Calculate the total wealth of each customer.
- Compare the total with `maximum_wealth`.
- Update `maximum_wealth` if the current customer's wealth is greater.
- Return the maximum wealth.

## Complexity Analysis

- **Time Complexity:** O(n × m)
- **Space Complexity:** O(1) Auxiliary Space

Where:
- `n` = Number of customers
- `m` = Number of bank accounts per customer

## Concepts Practiced

- Python Lists
- Nested Loops
- Variables
- Conditional Statements
- Maximum Value
- Time and Space Complexity

## Language

Python 3
