# Exercise 3 - Bedtools

In this exercise we want to compare the association ("similarity") between the SNPs and multiple different open chromatin tracks.

## 1: Prepare the data
First, make a new folder for this exercise and position yourself in that folder.

Copy the SNPs associated with Multiple Sclerosis that you used in [Exercise 1](Exercise1-Galaxy.md) into this directory.

Download [this compressed file](https://github.com/uio-bmi/statistical_genomics_exercises/raw/master/open_chromatin_data/open_chromatin_data.tar.gz) that contains multiple open chromatin bed files for different cells. You can do this using wget:

```
wget https://github.com/uio-bmi/statistical_genomics_exercises/raw/master/open_chromatin_data/open_chromatin_data.tar.gz
``` 

This will give you a file `open_chromatin_data.tar.gz`. Uncompress the file:
```
tar xvzf open_chromatin_data.tar.gz
```

You should now have a lot of files ending in ".broadpeak". These are bed-files even though the file extension says ".broadpeak". You can list all these files:
```
ls *.broadpeak
```

You can have a look at parts of some of these files if you want, e.g.:
``` 
head NB4.broadpeak
```


### 2: Check similarity with one track
As described in the lecture, when comparing one track against multiple tracks, we will need to use a suitable similarity measure, since simply counting the overlap will be biased towards tracks with lots of data.

Beedtools has a subcommand **jaccard** that computes the Jaccard similiarity between two tracks. Read the documentation on **bedtools jaccard** and compute the jaccard similarity between the SNPs and one of the open chromatin tracks (you choose which).

### 3: Checking similarity between multiple tracks
Unfortunately, **bedtools jaccard** cannot take multiple files as input, so we will have to run this command once for every open chromatin track. We can do this with a for-loop in unix. The following bash code goes through all the lines in this directory ending with *.broadpeak*, and performs the operation on each such file (wich then is accessed through $i variable):

```
for i in *.broadpeak;
    do 
    echo $i;
    bedtools jaccard -a ms_associated_snps.bed -b $i; 
done
```

When running this, you should get a filename printed before the results from bedtools. The jaccard similarity is in column 3. Find manually by looking through this which open chromatin track has highest jaccard similarity to the SNPs.

