from numpy.random import randint

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

print("Number of snps: ", len(snp_positions))

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


print("Number of segments: ", len(open_chromatin_segments))

n_basepairs_covered = 0
for segment in open_chromatin_segments:
    start = segment[0]
    end = segment[1]

    n_basepairs_covered += end - start

print("Number of base pairs covered: ", n_basepairs_covered)


# Count number of snps inside the open chromatin
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

n_inside = count_snps_inside_regions(snp_positions, open_chromatin_segments)
print("Number of snps inside open chromatin regions: ", n_inside)



from numpy.random import randint
random_positions = randint(0, 171115067, 45)
n_inside = count_snps_inside_regions(random_positions, open_chromatin_segments)
print("Number of RANDOM snps inside open chromatin regions: ", n_inside)

# Run this 100 times with 100 random SNP sets
import matplotlib.pyplot as plt

counts = []

for i in range(0, 100):
    random_positions = randint(0, 171115067, 45)
    count = count_snps_inside_regions(random_positions, open_chromatin_segments)
    counts.append(count)

# Plot the histogram
plt.hist(counts, bins=5)
print(counts)
plt.show()
