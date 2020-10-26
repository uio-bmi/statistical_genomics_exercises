# Exercise 2 - Python

This exercise continues from the [first Python exercise](Exercise1-Python.md) and requires that you have done that.



## 1: Put the code from the last part of the previous exercise inside a function
In the last part of the first Python exercise, we made code for counting number of SNPs inside the open chromatin regions. 

We now want to put that code into a function, so that we easily can run that code multiple times (on random data).

What we want is a function that can take a list of SNPs and a list of segments and returns the number of SNPs that are inside the segments.

**Task: Create a function with the code from exercise 4c. The function has two arguments (snp_positions and open_chromatin_regions):**
```python
def count_snps_inside_regions(snp_positions, open_chromatin_segments):
    # Your code here...
    
    return n_snps_inside_open_chromatin
    
# Call the function like this:
n_inside = count_snps_inside_regions(snp_positions, open_chromatin_segments)
print("Number of snps inside open chromatin regions: ", n_inside)
```

<details>
<summary>View full solution</summary>

```python
def count_snps_inside_regions(snp_positions, open_chromatin_segments):
    n_snps_inside_open_chromatin = 0

    for open_chromatin_region in open_chromatin_segments:
        start = open_chromatin_region[0]
        end = open_chromatin_region[1]
        for snp in snp_positions:
            # Check here whether the SNP is inside the region, increase the counter if it is     
            if snp >= start and snp < end:
                n_snps_inside_open_chromatin += 1
        
    return n_snps_inside_open_chromatin
    
# Call the function like this:
n_inside = count_snps_inside_regions(snp_positions, open_chromatin_segments)
print("Number of snps inside open chromatin regions: ", n_inside)
```
</details>


## 2: Run the function with random SNP position
With Python, we can easily draw random numbers. For instnace, we can draw 45 random positions on chromosome 6 with the following code (note that `171115067` is the size of chromosome 6):
```python
from numpy.random import randint
random_positions = randint(0, 171115067, 45)
```

**Task: Call the function you created with 45 random SNP positions (instead of the 45 SNP positions you read from the file). 
How many random SNPs are within the open chromatin regions? You can try running this multiple times.**

<details>
<summary>View solution</summary>

```python
from numpy.random import randint
random_positions = randint(0, 171115067, 45)

n_inside = count_snps_inside_regions(random_positions, open_chromatin_segments)
print(n_inside)
```

</details>


## 3: Bonus task
**Task: Run the `count_snps_inside_regions` function many times with random SNP positions. Draw a histogram of all the counts.**

<details>
<summary>View solution</summary>

```python
from numpy.random import randint
import matplotlib.pyplot as plt
counts = []

for i in range(0, 100):
    random_positions = randint(0, 171115067, 45)
    count = count_snps_inside_regions(random_positions, open_chromatin_segments)
    counts.append(count) 
    
# Plot the histogram
plt.plot(counts)
plt.show()
```
