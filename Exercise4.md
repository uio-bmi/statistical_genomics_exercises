# Exercise 4

In this exercise, we will investigate how many of SNPs associated with Multiple Sclerosis are positioned inside open chromatin areas. 
In this task, we will only look at SNPs and open chromatin on chromosome 6 (to make things more simple). 

# a: Read the SNPs
[This BED-file]() contains the SNPs we will investigate. Each line represents one SNP (first column is chromosome and second column is the position).

We want to read this file and put all the SNP positions in a Python list so that we end up with a list of numbers. You can ignore the chromosome, since all SNPs are on chromosome 6.

**Task: Write a simple Python program that reads this file and creates a list with all the SNP positions. How many SNPs are there?**

PS: You can create an empty list with `my_list = []` and append an position to that list with `my_list.append(position)`.

<details>
<summary>View solution</summary>

```python
# Initialize an empty list that we will use to store the positions
snp_positions = []

# Open the file and go through the lines
snps_file = open("ms_associated_snps_chr6.bed")
for line in snps_file:
    # Split the line and get the SNP position
    splitted_line = line.split()
    snp_position = int(splitted_line[1])
    
    # Add this position to the list
    snp_positions.append(snp_position)

print("Number of snps: ", len(snp_position))
```
</details> 


# b: Read the open chromatin regions
Similarly, we want to read the open chromatin regions into a list. But since these are segments and not points, we want to store
both the start and end coordinate of each region. We can do this by representing each open chromatin segment with a tuple. 
For instance, if there are two open chromatin regions, our list could look like this:

```python
open_chromatin_segments = [(0, 10), (50, 60)]
```

**Task: Write a Python program that reads all the open chromatin segments into a list where each element is a tuple  (or list) containing the start and end position.**

PS: You can add a tuple to a list like this: `my_list.append((start_position, end_position))`


<details>
<summary>View solution</summary>

```python
# Initialize an empty list that we will use to store the positions
open_chromatin_segments = []

# Open the file and go through the lines
open_chromatin_file = open("open_chromatin_chr6.bed")
for line in open_chromatin_file:
    # Split the line and get the start and end coordinate
    splitted_line = line.split()
    start_position = int(splitted_line[1])
    end_position = int(splitted_line[2])
    
    # Add the start and end position to the list
    open_chromatin_segments.append((start_position, end_position))
```
</details> 


**Question: How many segments (open chromatin regions) are there?**
<details>
<summary>View solution</summary>

```python
print("Number of segments: ", len(open_chromatin_segments))
```

</details>


**Question: How many base pairs do these segments cover?** 
<details>
<summary>View solution</summary>

```python
n_basepairs_covered = 0
for segment in open_chromatin_segments:
    start = segment[0]
    end = segment[1]
    
    n_basepairs_covered += start - end
    
print("Number of base pairs covered: ", n_basepairs_covered)
```

</details>


# c
**Task: Write python code to find out how many of the SNPs are within open chromatin regions?**

*PS:* The easiest way to do this is by using two for-loops (one inside the other). The first for-loop can go throuh all the open chromatin regions, and for each region a new for-loop goes through all the SNPs and checks whether the SNP is inside the region or not.

Some skeleton-code that can be used to get started:
```python
n_snps_inside_open_chromatin = 0

for open_chromatin_region in open_chromatin_regions:
    start = open_chromatin_region[0]
    end = open_chromatin_region[1]
    for snp in snp_positions:
        # Check here whether the SNP is inside the region, increase the counter if it is     
```

<details>
<summary>View full solution</summary>

```python
n_snps_inside_open_chromatin = 0

for open_chromatin_region in open_chromatin_regions:
    start = open_chromatin_region[0]
    end = open_chromatin_region[1]
    for snp in snp_positions:
        # Check here whether the SNP is inside the region, increase the counter if it is     
        if snp >= start and snp < end:
            n_snps_inside_open_chromatin += 1

print("Number of SNPs inside open chromatin regions: %d", )
```
</details>



