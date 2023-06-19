
%% print_yellow | '# Binary Search simulation' %%

```text
Welcome to the binary search minigame!

Binary search is a simple yet powerful strategy for finding
values in a sorted list.

Counting from the start to the end is a strategy that quickly becomes expensive when the size of a list grows large.

Binary search on the other hand remains efficient regardless of how large a list is.


```

```code
n = get_number()
```

```text
{{ bs_simulate | n }}

{{ pause }}

As you can see each step, we get rid of approximately half the possible options.

When the list size is n,

for example,

for a list [5,8,2] n = 3
for a list [1,2,3,4,5] n = 5

------------------------------------------------------

What would n be for the list,
```

```code
random_list()
```

```text
?

{{ pause }}

------------------------------------------------------

To calculate the average number of steps, we can use the formula:

Average steps = log2(n) + 1

Here's the calculation for the examples you provided:

For a list of size 100:
Average steps = log2(100) + 1
= 6.64 + 1
≈ 7.64

For a list of size 1,000:
Average steps = log2(1,000) + 1
= 9.97 + 1
≈ 10.97

For a list of size 10,000:
Average steps = log2(10,000) + 1
= 13.29 + 1
≈ 14.29

For a list of size 1,000,000:
Average steps = log2(1,000,000) + 1
= 19.93 + 1
≈ 20.93

As you can see, even as n grows large, the average number of steps remains small.

Conclusion:

If there is a problem you can apply binary search on, it's very likely going to be efficient and consistent.

```