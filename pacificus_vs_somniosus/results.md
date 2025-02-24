## _How does varying the k-mer size and minimum sequence length affect results?_

### K-mer size and minimum sequence length (k, s)

#### We start with running the with default k-mer size 25 and minimum sequence length 100.

(k=25, s=100): default, no unique sequence segments returned

#### We try decreasing the minimum sequence length while holding the k-mer size constant, to search for roughly the longest stretch of unique sequence segment resulting from searches with 25-mers.

(k=25, s=80): no unique sequence segments returned

(k=25, s=70): no unique sequence segments returned

(k=25, s=60): no unique sequence segments returned

(k=25, s=50): no unique sequence segments returned

<details>
  <summary>(k=25, s=40)</summary>
>NC_022734.1region15893-15932_size40_propspcIN25.0_propunivsOUT100.0_avgOUTentries0.0
TAAAAATTCATAACCCACATTAATTTATAATCAATATATT
</details>

<details>
  <summary>(k=25, s=30)</summary>
>NC_022734.1region13651-13687_size37_propspcIN28.2_propunivsOUT100.0_avgOUTentries0.0
TCTTATCCAACAAACACCTCTAATCAAATTATCTACA
>NC_022734.1region14795-14828_size34_propspcIN25.6_propunivsOUT100.0_avgOUTentries0.0
CACAGTTATTACTAATCTTCTTTCAGCCTTCCCA
>NC_022734.1region15893-15932_size40_propspcIN25.0_propunivsOUT100.0_avgOUTentries0.0
TAAAAATTCATAACCCACATTAATTTATAATCAATATATT
</details>

#### Then, the total number of unique 25-mers is 25, with the segments shown below: 
<details>
  <summary>(k=25, s=25)</summary>
>NC_022734.1region1167-1191_size25_propspcIN57.1_propunivsOUT100.0_avgOUTentries0.0
ACATTTTACACCTTTTAGTATGGGC
>NC_022734.1region2301-2325_size25_propspcIN14.3_propunivsOUT100.0_avgOUTentries0.0
TAATTTAATTGTTTTTGGTTGGGGC
>NC_022734.1region2943-2967_size25_propspcIN28.6_propunivsOUT100.0_avgOUTentries0.0
GGGCTACATACAATTCCGTAAAGGC
>NC_022734.1region4417-4441_size25_propspcIN57.1_propunivsOUT100.0_avgOUTentries0.0
TCTAGCCACCTGACAAAAACTTGCC
>NC_022734.1region5771-5795_size25_propspcIN28.6_propunivsOUT100.0_avgOUTentries0.0
TTGATTACTCCCCCCCTCTCTCCTG
>NC_022734.1region5858-5882_size25_propspcIN57.1_propunivsOUT100.0_avgOUTentries0.0
CCTTGCAGGTAATATAGCCCACGCC
>NC_022734.1region7077-7101_size25_propspcIN49.7_propunivsOUT100.0_avgOUTentries0.0
CACTCTGTCACTTTCTTTGTAAGAC
>NC_022734.1region7608-7632_size25_propspcIN57.1_propunivsOUT100.0_avgOUTentries0.0
AGAATCCCCCATTCGTGTTCTAGTA
>NC_022734.1region7758-7782_size25_propspcIN57.1_propunivsOUT100.0_avgOUTentries0.0
TTCAGAGATTTGTGGTGCTAACCAC
>NC_022734.1region8148-8172_size25_propspcIN57.1_propunivsOUT100.0_avgOUTentries0.0
ATTAATTGCCCTAGCAATTATAATT
>NC_022734.1region8355-8379_size25_propspcIN71.4_propunivsOUT100.0_avgOUTentries0.0
TTTACTACCATATACTTTTACACCC
>NC_022734.1region8476-8500_size25_propspcIN14.3_propunivsOUT100.0_avgOUTentries0.0
CACCTACTACCAGAAGGCACTCCAG
>NC_022734.1region8539-8563_size25_propspcIN14.3_propunivsOUT100.0_avgOUTentries0.0
AGCCTCTTTATTCGACCTTTAGCAC
>NC_022734.1region9092-9116_size25_propspcIN71.4_propunivsOUT100.0_avgOUTentries0.0
CCTTGCCCCCACACCAGAATTGGGC
>NC_022734.1region9794-9818_size25_propspcIN56.6_propunivsOUT100.0_avgOUTentries0.0
ACTGCGCTTCTTCCTTGTGGCGATC
>NC_022734.1region10598-10622_size25_propspcIN14.3_propunivsOUT100.0_avgOUTentries0.0
CCACATTTCCACTGAACCTATTATG
>NC_022734.1region11965-11989_size25_propspcIN57.1_propunivsOUT100.0_avgOUTentries0.0
CTTCCTCCTCATCTTCATTATCCTG
>NC_022734.1region13651-13687_size37_propspcIN28.2_propunivsOUT100.0_avgOUTentries0.0
TCTTATCCAACAAACACCTCTAATCAAATTATCTACA
>NC_022734.1region13930-13954_size25_propspcIN50.9_propunivsOUT100.0_avgOUTentries0.0
CATCTCCTCAACCCCCGCTCAACCA
>NC_022734.1region14768-14792_size25_propspcIN28.6_propunivsOUT100.0_avgOUTentries0.0
ATGAGGACAAATATCTTTCTGAGGA
>NC_022734.1region14795-14828_size34_propspcIN25.6_propunivsOUT100.0_avgOUTentries0.0
CACAGTTATTACTAATCTTCTTTCAGCCTTCCCA
>NC_022734.1region15260-15284_size25_propspcIN71.4_propunivsOUT100.0_avgOUTentries0.0
CTTTATCCTCATATTGGTTCCAATA
>NC_022734.1region15310-15334_size25_propspcIN14.3_propunivsOUT100.0_avgOUTentries0.0
ATACCTTCCGACCCCCAGCCCAAAC
>NC_022734.1region15893-15932_size40_propspcIN25.0_propunivsOUT100.0_avgOUTentries0.0
TAAAAATTCATAACCCACATTAATTTATAATCAATATATT
>NC_022734.1region16300-16324_size25_propspcIN28.6_propunivsOUT100.0_avgOUTentries0.0
ATCCTCGGACTCTGGTCATTAAGTA
</details>

#### Then we try increasing the k-mer size while holding the minimum sequence length constant at 60.

<details>
  <summary>(k=30, s=60)</summary>
>NC_022734.1region14763-14828_size66_propspcIN26.0_propunivsOUT100.0_avgOUTentries0.0
CTACCATGAGGACAAATATCTTTCTGAGGAGCCACAGTTATTACTAATCTTCTTTCAGCCTTCCCA
</details>

<details>
  <summary>(k=35, s=60)</summary>
>NC_022734.1region14758-14828_size71_propspcIN25.2_propunivsOUT100.0_avgOUTentries0.0
ATGTCCTACCATGAGGACAAATATCTTTCTGAGGAGCCACAGTTATTACTAATCTTCTTTCAGCCTTCCCA
</details>

<details>
  <summary>(k=40, s=60)</summary>
>NC_022734.1region14753-14828_size76_propspcIN24.4_propunivsOUT100.0_avgOUTentries0.0
GGGTTATGTCCTACCATGAGGACAAATATCTTTCTGAGGAGCCACAGTTATTACTAATCTTCTTTCAGCCTTCCCA
</details>

<details>
  <summary>(k=45, s=60)</summary>
>NC_022734.1region11930-11995_size66_propspcIN57.1_propunivsOUT100.0_avgOUTentries0.0
GCAAGAGCTATGAATATAATTATCTTTAACTCAGCCTTCCTCCTCATCTTCATTATCCTGTTATAC
>NC_022734.1region14748-14828_size81_propspcIN23.8_propunivsOUT100.0_avgOUTentries0.0
TTCGTGGGTTATGTCCTACCATGAGGACAAATATCTTTCTGAGGAGCCACAGTTATTACTAATCTTCTTTCAGCCTTCCCA
>NC_022734.1region15873-15932_size60_propspcIN21.4_propunivsOUT100.0_avgOUTentries0.0
TAATCAACAAATTCATTTCATAAAAATTCATAACCCACATTAATTTATAATCAATATATT
</details>

<details>
  <summary>(k=50, s=60)</summary>
>NC_022734.1region10573-10634_size62_propspcIN14.3_propunivsOUT100.0_avgOUTentries0.0
CATTAATGATTTTAGCAAGTCAAAACCACATTTCCACTGAACCTATTATGCGCCAACGAATT
>NC_022734.1region11925-11995_size71_propspcIN57.1_propunivsOUT100.0_avgOUTentries0.0
TCCAAGCAAGAGCTATGAATATAATTATCTTTAACTCAGCCTTCCTCCTCATCTTCATTATCCTGTTATAC
>NC_022734.1region13626-13687_size62_propspcIN22.6_propunivsOUT100.0_avgOUTentries0.0
ACGAAAAAATTGGCCCAAAAAGTACTCTTATCCAACAAACACCTCTAATCAAATTATCTACA
>NC_022734.1region14743-14828_size86_propspcIN23.3_propunivsOUT100.0_avgOUTentries0.0
CAGCCTTCGTGGGTTATGTCCTACCATGAGGACAAATATCTTTCTGAGGAGCCACAGTTATTACTAATCTTCTTTCAGCCTTCCCA
>NC_022734.1region15235-15334_size100_propspcIN41.9_propunivsOUT100.0_avgOUTentries0.0
GGGTTCTAGCCCTCCTATTCTCAATCTTTATCCTCATATTGGTTCCAATACTTCACACCTCAAAACAACGAAGCAATACCTTCCGACCCCCAGCCCAAAC
>NC_022734.1region15845-15932_size88_propspcIN19.2_propunivsOUT100.0_avgOUTentries0.0
ATACTATGATTAACCCACACTTCCTTAATAATCAACAAATTCATTTCATAAAAATTCATAACCCACATTAATTTATAATCAATATATT
</details>

<details>
  <summary>(k=55, s=60)</summary>
>NC_022734.1region10568-10634_size67_propspcIN14.3_propunivsOUT100.0_avgOUTentries0.0
CCTCCCATTAATGATTTTAGCAAGTCAAAACCACATTTCCACTGAACCTATTATGCGCCAACGAATT
>NC_022734.1region11920-11995_size76_propspcIN57.1_propunivsOUT100.0_avgOUTentries0.0
GCAACTCCAAGCAAGAGCTATGAATATAATTATCTTTAACTCAGCCTTCCTCCTCATCTTCATTATCCTGTTATAC
>NC_022734.1region13345-13453_size109_propspcIN60.0_propunivsOUT100.0_avgOUTentries0.0
CTTAATCATTACACTTAACCTCCCACCAACAAAAACCCAAATTATGACCATAACCCCATTACTAAAATTATCCGCCCTCCTAGTAACTATTATTGGCCTGCTAGTAGCA
>NC_022734.1region13621-13687_size67_propspcIN22.0_propunivsOUT100.0_avgOUTentries0.0
CTGAAACGAAAAAATTGGCCCAAAAAGTACTCTTATCCAACAAACACCTCTAATCAAATTATCTACA
>NC_022734.1region14738-14828_size91_propspcIN22.8_propunivsOUT100.0_avgOUTentries0.0
AGCAACAGCCTTCGTGGGTTATGTCCTACCATGAGGACAAATATCTTTCTGAGGAGCCACAGTTATTACTAATCTTCTTTCAGCCTTCCCA
>NC_022734.1region15212-15334_size123_propspcIN47.2_propunivsOUT100.0_avgOUTentries0.0
CTCTATCCCAAATAAACTTGGGGGGGTTCTAGCCCTCCTATTCTCAATCTTTATCCTCATATTGGTTCCAATACTTCACACCTCAAAACAACGAAGCAATACCTTCCGACCCCCAGCCCAAAC
>NC_022734.1region15840-15932_size93_propspcIN18.9_propunivsOUT100.0_avgOUTentries0.0
ATTACATACTATGATTAACCCACACTTCCTTAATAATCAACAAATTCATTTCATAAAAATTCATAACCCACATTAATTTATAATCAATATATT
</details>

<details>
  <summary>(k=60, s=60)</summary>
>NC_022734.1region1132-1191_size60_propspcIN57.1_propunivsOUT100.0_avgOUTentries0.0
TATCAATTATACCCACCATTAATTATTAAATTAAAACATTTTACACCTTTTAGTATGGGC
>NC_022734.1region2266-2325_size60_propspcIN14.3_propunivsOUT100.0_avgOUTentries0.0
TAATCCCCTGGGAATAATCACTCATACAATATTTCTAATTTAATTGTTTTTGGTTGGGGC
>NC_022734.1region2908-2967_size60_propspcIN28.6_propunivsOUT100.0_avgOUTentries0.0
ACAGCTTTTTTAACCTTAGTTGAACGAAAAATTCTGGGCTACATACAATTCCGTAAAGGC
>NC_022734.1region4382-4441_size60_propspcIN57.1_propunivsOUT100.0_avgOUTentries0.0
GTACTTCAAGGATTAGACCTTACCACAGGTTTAATTCTAGCCACCTGACAAAAACTTGCC
>NC_022734.1region5736-5795_size60_propspcIN28.6_propunivsOUT100.0_avgOUTentries0.0
GACATAGCTTTCCCGCGAATAAATAACATAAGCTTTTGATTACTCCCCCCCTCTCTCCTG
>NC_022734.1region5823-5882_size60_propspcIN57.1_propunivsOUT100.0_avgOUTentries0.0
GCAGGAGCCGGAACCGGCTGAACGGTCTATCCCCCCCTTGCAGGTAATATAGCCCACGCC
>NC_022734.1region7042-7101_size60_propspcIN44.3_propunivsOUT100.0_avgOUTentries0.0
ACCCCCGTATATTGATTTCAAGTCAATCACATCACCACTCTGTCACTTTCTTTGTAAGAC
>NC_022734.1region7573-7632_size60_propspcIN57.1_propunivsOUT100.0_avgOUTentries0.0
TTGTTAGAAACCGACCACCGAATAATTGTACCTATAGAATCCCCCATTCGTGTTCTAGTA
>NC_022734.1region7723-7782_size60_propspcIN57.1_propunivsOUT100.0_avgOUTentries0.0
ATTATTTCCCGACCAGGTGTTTATTATGGTCAATGTTCAGAGATTTGTGGTGCTAACCAC
>NC_022734.1region8113-8172_size60_propspcIN57.1_propunivsOUT100.0_avgOUTentries0.0
GACCAATTCTTAAGCCCCTCACTCCTTGGAATCCCATTAATTGCCCTAGCAATTATAATT
>NC_022734.1region8320-8379_size60_propspcIN65.2_propunivsOUT100.0_avgOUTentries0.0
CTAATATTATTTTTAATTACTATTAACCTTCTTGGTTTACTACCATATACTTTTACACCC
>NC_022734.1region8441-8500_size60_propspcIN14.3_propunivsOUT100.0_avgOUTentries0.0
TTGGGGTACTCAATCAACCCACCATTGCTCTTGGGCACCTACTACCAGAAGGCACTCCAG
>NC_022734.1region8504-8563_size60_propspcIN14.3_propunivsOUT100.0_avgOUTentries0.0
TATTAATCCCAATTTTAATTATTATCGAAACTATCAGCCTCTTTATTCGACCTTTAGCAC
>NC_022734.1region9057-9116_size60_propspcIN71.4_propunivsOUT100.0_avgOUTentries0.0
TTCCTCGGCTTTTTCTGGGCCTTCTACCACTCAAGCCTTGCCCCCACACCAGAATTGGGC
>NC_022734.1region9759-9818_size60_propspcIN48.6_propunivsOUT100.0_avgOUTentries0.0
TTTGACCCATTAGGAAGTGCACGCCTCCCATTCTCACTGCGCTTCTTCCTTGTGGCGATC
>NC_022734.1region10563-10634_size72_propspcIN14.3_propunivsOUT100.0_avgOUTentries0.0
TGGCTCCTCCCATTAATGATTTTAGCAAGTCAAAACCACATTTCCACTGAACCTATTATGCGCCAACGAATT
>NC_022734.1region11915-11995_size81_propspcIN57.1_propunivsOUT100.0_avgOUTentries0.0
TTGGTGCAACTCCAAGCAAGAGCTATGAATATAATTATCTTTAACTCAGCCTTCCTCCTCATCTTCATTATCCTGTTATAC
>NC_022734.1region13340-13453_size114_propspcIN59.3_propunivsOUT100.0_avgOUTentries0.0
GCTGGCTTAATCATTACACTTAACCTCCCACCAACAAAAACCCAAATTATGACCATAACCCCATTACTAAAATTATCCGCCCTCCTAGTAACTATTATTGGCCTGCTAGTAGCA
>NC_022734.1region13616-13687_size72_propspcIN21.4_propunivsOUT100.0_avgOUTentries0.0
CTAACCTGAAACGAAAAAATTGGCCCAAAAAGTACTCTTATCCAACAAACACCTCTAATCAAATTATCTACA
>NC_022734.1region13895-13954_size60_propspcIN46.2_propunivsOUT100.0_avgOUTentries0.0
CCACCAAAATCCCCTCGAACCATTTCTAAATTACTCATCTCCTCAACCCCCGCTCAACCA
>NC_022734.1region14733-14828_size96_propspcIN22.3_propunivsOUT100.0_avgOUTentries0.0
CTAATAGCAACAGCCTTCGTGGGTTATGTCCTACCATGAGGACAAATATCTTTCTGAGGAGCCACAGTTATTACTAATCTTCTTTCAGCCTTCCCA
>NC_022734.1region15207-15334_size128_propspcIN45.9_propunivsOUT100.0_avgOUTentries0.0
CTACGCTCTATCCCAAATAAACTTGGGGGGGTTCTAGCCCTCCTATTCTCAATCTTTATCCTCATATTGGTTCCAATACTTCACACCTCAAAACAACGAAGCAATACCTTCCGACCCCCAGCCCAAAC
>NC_022734.1region15835-15932_size98_propspcIN18.7_propunivsOUT100.0_avgOUTentries0.0
CCTTCATTACATACTATGATTAACCCACACTTCCTTAATAATCAACAAATTCATTTCATAAAAATTCATAACCCACATTAATTTATAATCAATATATT
>NC_022734.1region16265-16324_size60_propspcIN28.6_propunivsOUT100.0_avgOUTentries0.0
CATCTAGACCTAAATTGAGATATTAAATAAATGAAATCCTCGGACTCTGGTCATTAAGTA
</details>

## _Do the unique sequence segments match with primers found visually?_

The region corresponding to cytochrome B in the _S.pacificus_ mitogenome is from 14365-15510. From the unikseq analysis, one recurrent unique region extends from approximately 14740-14828 (found in all runs where minimum sequence length s is held at 60), which encompasses part of the cytochrome B region. Another region that is found is region 15873-15932, which overlaps with an annotated D-loop. When k=60 and s=60, unique segments are found in the COXI region (5500-7000) but one would have to verify closely if these are unique enough to be truly identifying somniosus. 

Refer to the annotated mitochondrial genome from the [MitoFish database](https://mitofish.aori.u-tokyo.ac.jp/species/result/?q=Somniosus+pacificus). 

## _What are the main unique zones as visualised with the butterfly plot?_
The butterfly plot shows on the y-axis each position of the reference sequence, so every base of the _S.pacificus_ mitogenome, and on the x-axis the proportion that the base was found in a unique k-mer in the ingroup (left, teal), vs the proportion that the base was found to be in a non-unique k-mer (right, salmon). In this way, one can get an overall visualisation of which regions of the reference genome are unique to the reference, to what extent they are found in the ingroup, and which regions are very similar between the target and the outgroup. If one wants a unique sequence segment that is found in a higher proportion of the ingroup sequences, one would choose a region that is having the longest left-wards facing teal lines, that ideally does not have too much of a rightward facing, salmon colored cluster of lines.

We can see that the _S.pacificus_ mitogenome is very similar to other Somniosids species, as the majority of k-mers are containing non-unique bases.

### 25-mer

<p align="center">
<img src="https://github.com/GlassLabGenomics/sleepershark_seq_analysis/blob/main/pacificus_vs_others/output/kmer25_butterflyplot.png" width="1000">
</p>

### 30-mer 

<p align="center">
<img src="https://github.com/GlassLabGenomics/sleepershark_seq_analysis/blob/main/pacificus_vs_others/output/kmer30_butterflyplot.png" width="1000">
</p>
