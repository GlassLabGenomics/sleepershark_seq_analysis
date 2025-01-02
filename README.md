Sleeper Shark (in silico) barcoding
===================================

This repository contains scripts and example files to run unikseq on sleeper shark mitogenomes, with the purpose of finding identifying regions for target species to amplify with qPCR. Unikseq is designed to help with an initial screening of regions that could be considered for primer design, but it isn't written with biological considerations (GC content, length, melting temp, etc.) in mind, which means that the user has to keep these in mind when performing the parameter tuning step. See section on Parameter Considerations below for a more detailed discussion of this.

The link to the tool is given here: [unikseq tool](https://github.com/bcgsc/unikseq), and the corresponding publication: [Allison et al. 2023](https://onlinelibrary.wiley.com/doi/full/10.1002/edn3.438).

Installation
------------

Here are the installation and setup instructions for the chinook server. The best way is to create a virtual environment, ideally with mamba, or install unikseq into an existing mamba environment that you use to analyse bio data.

See Installation on [mamba setup](https://uaf-rcs.gitbook.io/uaf-rcs-hpc-docs/third-party-software/miniconda#best-practices-on-chinook) to create a mamba environment. In the example, my virtual environment is called `bioenv`.

Once you have this, log into chinook and navigate to $CENTER1. Then follow the steps below. Remember to substitute bioenv with the name of your environment.

```sh
# Activate your environment, so you can install unikseq into it.
mamba activate bioenv

# Install unikseq and bioconda, type in Y when prompted
mamba install -c bioconda unikseq
```

### What this all looks like:
<details>
  <summary>expand</summary>
  
```
(base) [yhsieh@chinook04 yhsieh]$ mamba activate bioenv
(bioenv) [yhsieh@chinook04 sleepershark_primers]$ mamba install -c bioconda unikseq

Looking for: ['unikseq']

bioconda/linux-64 (check zst)                       Checked  0.3s
bioconda/noarch (check zst)                         Checked  0.1s
bioconda/linux-64                                    4.7MB @  11.8MB/s  0.7s
bioconda/noarch                                      4.4MB @   6.0MB/s  1.0s
conda-forge/noarch                                  17.6MB @  12.9MB/s  2.4s
conda-forge/linux-64                                40.4MB @  15.2MB/s  5.3s

Pinned packages:
  - python 3.12.*


Transaction

  Prefix: /home/yhsieh/miniforge3/envs/bioenv

  Updating specs:

   - unikseq
   - ca-certificates
   - certifi
   - openssl


  Package    Version  Build             Channel           Size
────────────────────────────────────────────────────────────────
  Install:
────────────────────────────────────────────────────────────────

  + perl      5.32.1  7_hd590300_perl5  conda-forge       13MB
  + links      1.8.7  pl5321h7d875b9_3  bioconda          74kB
  + unikseq    2.0.0  hdfd78af_0        bioconda          26kB

  Upgrade:
────────────────────────────────────────────────────────────────

  - openssl    3.3.2  hb9d3cd8_0        conda-forge     Cached
  + openssl    3.4.0  hb9d3cd8_0        conda-forge        3MB

  Summary:

  Install: 3 packages
  Upgrade: 1 packages

  Total download: 16MB

────────────────────────────────────────────────────────────────


Confirm changes: [Y/n] Y
unikseq                                             26.4kB @  64.0kB/s  0.4s
links                                               73.9kB @ 147.2kB/s  0.5s
openssl                                              2.9MB @   3.1MB/s  1.0s
perl                                                13.3MB @   7.7MB/s  1.9s

Downloading and Extracting Packages:

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
```

</details>


Usage
--------
Unikseq is written in Perl, and the main script to run it is `unikseq.pl`. 

From the documentation, the options for running it are given below. More detailed explanation of each parameter can be found on [unikseq's source page on GitHub](https://github.com/bcgsc/unikseq).
```
Usage: unikseq.pl
-----input files-----
 -r reference FASTA (required)
 -i ingroup FASTA (required)
 -o outgroup FASTA (required)
-----k-mer uniqueness filters-----
 -k length (option, default: -k 25)
 -l [leniency] min. non-unique consecutive k-mers allowed in outgroup (option, default: -l 0)
 -m max. [% entries] in outgroup tolerated to have a reference k-mer (option, default: -m 0 % [original behaviour])
-----output filters-----
 -t print only first t bases in tsv output (option, default: -t [k])
 -c output conserved FASTA regions between reference and ingroup entries (option, -c 1==yes -c 0==no, [default, original unikseq behaviour])
 -s min. reference FASTA region [size] (bp) to output (option, default: -s 100 bp)
 -p min. [-c 0:region average /-c 1: per position] proportion of ingroup entries (option, default: -p 0 %)
 -u min. [% unique] k-mers in regions (option, default: -u 90 %)
 -v output tsv files (option, -v 1==yes -v 0==no [default])
```

Workflow
--------
A typical workflow is described below, using data from our [testdata](testdata) folder. 
Before you do start, make sure you organise your files such that you have a reference, ingroup (target species), and outgroup (non-target species).

In our example, the NCBI Somniosus microcephalus mitogenome is the reference (microcephalus_mitogenome_NC_049864.1.fasta), our ingroup has 3 mitogenomes from S.microcephalus (microcephalus.fasta), and our outgroup has 6 mitogenomes from S.pacificus and S.antarcticus (antarcticus_pacificus.fasta).

1. From $CENTER1, start a interactive job: `srun -p debug --nodes=1 --exclusive --pty /bin/bash`.\
   If you get slurmstepd errors, or you get redirected to the tmp folder, run this instead `srun --pty bash -i`.
3. Activate your virtual environment where you have unikseq installed: `mamba activate bioenv`, navigate to your testdata folder if you haven't already done so.
4. Run unikseq from the command line, with defaults:\
   `unikseq.pl -k 25 -r microcephalus_mitogenome_NC_049864.1.fasta -i microcephalus.fasta -o antarcticus_pacificus.fasta`
5. Check your output, you should get `.bed`, `.log`, and `unique.fa` files.
   ```
   unikseq_v1.3.5-r_microcephalus_mitogenome_NC_049864.1.fasta-i_microcephalus.fasta-o_antarcticus_pacificus.fasta-k25-c0-s100-p0-l0-u90-m0.bed
   unikseq_v1.3.5-r_microcephalus_mitogenome_NC_049864.1.fasta-i_microcephalus.fasta-o_antarcticus_pacificus.fasta-k25-c0-s100-p0-l0-u90-m0.log
   unikseq_v1.3.5-r_microcephalus_mitogenome_NC_049864.1.fasta-i_microcephalus.fasta-o_antarcticus_pacificus.fasta-k25-c0-s100-p0-l0-u90-m0-unique.fa
   ```
   
Optional Parameter Considerations
------------------------
Setting up your basic unikseq run only requires the reference, ingroup, and outgroup sequence fasta files. However, to find usable unique regions you usually have to adjust the optional parameters. From here on, sequence refers to the complete sequence and segment refers to a sequence segment, usually a k-mer.

Here the most important parameters to tune are explained, in order: 

### K-mer size (`-k`)
The first parameter to pay attention to is your k-mer size (`-k` option), which controls the window size to slide across your reference sequence to search for unique segments. For primer design, the ideal size ranges between 8 and 30 bases, which is why the default k-mer value is 25. 

### Level of uniqueness, tuned by leniency (`-l`), uniqueness (`-u`), and max  (`-m`) values, controls on the outgroup
How strictly unique you want your sequence segments to be can be tuned by the leniency (`-l` option) and max  (`-m` option) parameters. Leniency controls the minimum number of non-unique, consecutive k-mers allowed in the outgroup. If you set this to 1 it means that your unique segment consists of unique k-mer segments interspersed by maximum one non-unique k-mer segment, and if you set this value to 5 it means that up to 5 non-unique k-mers will be found somewhere in your unique sequence segment. This would most likely then be 5 non-unique bases found in the total unique sequence segment, but they could be non-consecutive. Then, the `-m` option is intended for when outgroup sequences are highly similar, and controls the maximum proportion of outgroup sequences tolerated before the reference sequence is considered unique, so if you have it at 50 then you tolerate up to 50% of the outgroup sequences having a particular segment of the refseq. The `-u` value controls the percentage unique the final sequence segment should be.

### Length of output unique sequence (`-s`)
The minimum length of output unique sequence sets the size of the sequence segment to report in the unique seqs fasta file, so if you set this to 25 all the unique k-mers passing your uniqueness filters mentioned above will be output in the fasta file. In practice it's recommended to have your s value larger than your k value, since unikseq does not take into account biological characteristics of barcoding or primer design, so to have as large of a sequence outputted as possible allows for more of a suitable sequence region to be selected, depending on your purpose.

### Controls on the ingroup (`-p`)
The proportion `-p` option controls the proportion of ingroup sequences that have the sequence segment. 
