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

### What this all looks like on my computer:

```sh
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

Workflow
--------
Unikseq is written in Perl, and the main script to run it is `unikseq.pl`. 
