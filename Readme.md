# Statistical Genomics exercises

This repository contains material and exercises for the statistical genomics module.

## Excercise 1: Descriptive statistics
In this exercise we will work with SNPs known to be associated with the disease Multiple Sclerosis, and a genomic track containing regions with open chromatin. We will take a look at these datasets, get to know them, and compute som statistics. 

* [Exercise using Galaxy](Exercise1-Galaxy.md)
* [Exercise using Bedtools](Exercise1-Bedtools.md)
* [Excercise using Python (for those with programming experience or who want to learn)](Exercise1-Python.md)


## Exercise 2: Hypothesis testing
This exercise builds on the previous exercise. We now want to investigate whether the SNPs more often occur within regions of open chromatin that what we would expect by chance. For doing this, we will use the Genomic Hyperbrowser (which is similar to Galaxy, but has some additional tools for doing hypothesis testing). It will also be possible do do an optional exercise using Python:

* [Exercise using The Genomic Hyperbrowser (similar to Galaxy)](Exercise2-Hyperbrowser.md)
* [Exercise using Python (a bit advanced, for those experienced with Python wanting a challenge)](Exercise2-Python)

## Exercise 3: Multi-track analysis
We will now take the Multiple Sclerosis analysis one step further by performing the same analysis as in Exercise 2, but look at co-occurence between the SNPs and multiple tracks for open chromatin in different cells. Rather than investigating whether or not the association is significant for any of the tracks, we want to rank the tracks depending on how strong the association is.

* [Exercise using Bedtools](Exercise3-Bedtools.md)
* [Exercise using The Genomic Hyperbrowser](Excercise3-Hyperbrowser.md)
