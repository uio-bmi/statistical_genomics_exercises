# Exercise 1 - Bedtools


## 1: Log in to the server
Log in to the server, create a folder to work in:

```
ssh yourusername@bioint01.hpc.uio.no
# Make sure you are in your home directory:
cd
# Make a directory for doing the exercises, e.g.
mkdir statistical_genomics
cd statistical_genomics
mkdir exercise1
cd exercise1
```

Check that Bedtools is working by just typing bedtools. If everything works, you will see a list of possible subcommands:
```
bedtools
```


## 2: Download the data you need
The open chromatin and SNP files are hosted here:
* [this BED file with open chromatin regions](https://raw.githubusercontent.com/uio-bmi/statistical_genomics_exercises/master/open_chromatin_th1.bed) 
* [this BED file with SNP positions](https://raw.githubusercontent.com/uio-bmi/statistical_genomics_exercises/master/ms_associated_snps.bed) 

When on the server, you can download these files using the `wget` command:
```
wget https://raw.githubusercontent.com/uio-bmi/statistical_genomics_exercises/master/open_chromatin_th1.bed
wget https://raw.githubusercontent.com/uio-bmi/statistical_genomics_exercises/master/ms_associated_snps.bed 
```

## 3: How many SNPs are there?

How many SNPs are there? You do not need Bedtools to answer this question. Instead, you can count the number of lines in the SNPs bed file by using the unix `wc` command (word count). Try to find out how you can use this command to find the number of lines in the file (not number of words) by looking at the command help text:

```
wc --help
```

## 4: How many open chromatin regions are there?
Use the `wc` command again to answer this question.

## 5: How much of the genome is covered by the open chromatin?
For some reason, Bedtools does not have a command to find this easily, so you will not need to do this task. This is pretty straightforward to answer using Pyton (see the [Python exercise](Exercise1-Python.md)).

## 5: How many SNPs are inside open chromatin regions?
Finally, we will be using Bedtools. Answering this question using bedtools is as simple as:

```
bedtools intersect -a ms_associated_snps.bed -b open_chromatin_th1.bed > intersecting_regions.bed
```

Running the above will write the intersecting regions of the file specified by `-a` to intersecting_regions.bed.


## 6: Bonus question
Assume you want to find all open chromatin regions that have one or more SNPs inside, and only report those regions once.

Are you able, by reading the [bedtools intersect documentation](https://bedtools.readthedocs.io/en/latest/content/tools/intersect.html) to find out how to do that?

How many of the open chromatin regions have one or more SNPs inside them?



