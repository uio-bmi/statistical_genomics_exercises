import numpy as np
import matplotlib.pyplot as plt

file = open("open_chromatin_chr6.bed")
#file = open("ms_associated_snps_chr6.bed")

open_chromatin_regions = []
for line in file:
    line = line.split()
    chromosome = line[0]
    start = int(line[1])
    end = int(line[2])
    open_chromatin_regions.append((start, end))

file = open("ms_associated_snps_chr6.bed")
snp_positions = []
for line in file:
    snp_positions.append(int(line.split()[1]))

#print(open_chromatin_regions)

def compute_overlap(open_chromatin_regions, snp_positions):
    n_inside = 0
    for region in open_chromatin_regions:
        start, end = region
        for snp in snp_positions:
            if snp >= start and snp < end:
                n_inside += 1

    return n_inside


overlaps = []
for i in range(150):
    snps = np.random.randint(0, 171115067, 45)
    overlap = compute_overlap(open_chromatin_regions, snps)
    overlaps.append(overlap)

print(overlaps)
plt.hist(overlaps)
plt.show()

#print(compute_overlap(open_chromatin_regions, snp_positions))
