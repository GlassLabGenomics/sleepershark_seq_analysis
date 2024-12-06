Sleeper Shark (in silico) barcoding
===================================

This repository contains scripts and example files to run unikseq on sleeper shark mitogenomes, with the purpose of finding identifying regions for target species to amplify with qPCR.

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

1. From $CENTER1, start a interactive job: `srun -p debug --nodes=1 --exclusive --pty /bin/bash`
2. Activate your virtual environment where you have unikseq installed: `mamba activate bioenv`
3. Run unikseq from the command line, with defaults:\
   `unikseq.pl -k 25 -r microcephalus_mitogenome_NC_049864.1.fasta -i microcephalus.fasta -o antarcticus_pacificus.fasta`
4. Check your output, you should get `.bed`, `.log`, and `unique.fa` files.
   ```
   unikseq_v1.3.5-r_microcephalus_mitogenome_NC_049864.1.fasta-i_microcephalus.fasta-o_antarcticus_pacificus.fasta-k25-c0-s100-p0-l0-u90-m0.bed
   unikseq_v1.3.5-r_microcephalus_mitogenome_NC_049864.1.fasta-i_microcephalus.fasta-o_antarcticus_pacificus.fasta-k25-c0-s100-p0-l0-u90-m0.log
   unikseq_v1.3.5-r_microcephalus_mitogenome_NC_049864.1.fasta-i_microcephalus.fasta-o_antarcticus_pacificus.fasta-k25-c0-s100-p0-l0-u90-m0-unique.fa
   ```
