# Exercise 4

In this exercise, we will investigate how many of SNPs associated with Multiple Sclerosis are positioned inside open chromatin areas. 
In this task, we will only look at SNPs and open chromatin on chromosome 6 (to make things more simple). 

# 4a: Read the SNPs
[This BED-file]() contains the SNPs we will investigate. Each line represents one SNP (first column is chromosome and second column is the position).

We want to read this file and put all the SNP positions in a Python list so that we end up with a list of numbers. You can ignore the chromosome, since all SNPs are on chromosome 6.

Write a simple Python program that reads this file and creates a list with all the SNP positions.

PS: You can create an empty list with `my_list = []` and append an position to that list with `my_list.append(position)`.

<details>
<summary>View solution</summary>

```python
# Initialize an empty list that we will use to store the positions
snp_positions = []

# Open the file and go through the lines
snps_file = open("ms_associated_snps.bed")
for line in snps_file:
    # Split the line and get the SNP position
    splitted_line = line.split()
    snp_position = splitted_line[1]
    
    # Add this position to the list
    snp_positions.append(snp_position)

print("Number of snps: ", len(snp_position))
```


</details> 