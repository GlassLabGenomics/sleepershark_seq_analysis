#!/usr/env/bin python3
"""
parse_unique_seqs.py

Parses out k, s values and unique sequences (if any)
from unikseq result file ending in *unique.fa

Potential to-dos: replace splitting with regex
"""

from pathlib import Path

class UnikseqResult():
    """Object to store results of unikseq.
    Reads input from pathfile"""

    def __init__(self, paths):
        
        # input paths
        self.fastapath = ''

        self._read_paths(paths)

        self.kval = ''
        self.sval = ''
        self.uniqueseqs = ''

    def _read_paths(self, paths):
        """Reads paths from paths.txt"""
        pass


def parse_fasta(lines):
    """
    Return dict of {label:seq} from FASTA file
    lines: list of lines, open file object
    res: dict {label:seq}
    """
    res = {}  # result
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith('>'):
            label = line[1:]
            res[label] = []
        else:
            res[label].append(line)
    for k, v in res.items():
        res[k] = ''.join(v)
    return res

def get_params_from_filename(infile):
    params = infile.split('fasta')[3].split('-')
    kval = int(params[1][1:])
    sval = int(params[3][1:])
    return kval, sval

def read_fasta(infile):
    with open(infile, 'r') as f:
        fastadict = parse_fasta(f.readlines())
    return fastadict

def get_region_from_str(headerstr):
    region = headerstr.split('region')[1]
    region = region.split('_')[0] 
    region = region.split('-')
    return (int(region[0]), int(region[1]))

def parse_header(fastadict):
    """Takes in a fastadict and parses out info
    from the header, returns regions as a list"""
    regionlist = []
    for entry in fastadict:
        start, stop = get_region_from_str(entry)
        regionlist.append((start, stop))
    return regionlist

def combine_params_regions(infile):
    """Parses out k and s values, finds regions"""
    # prep input
    f_dict = read_fasta(infile)
    k_val, s_val = get_params_from_filename(infile)
    # get regions
    reg_list = parse_header(f_dict)
    return k_val, s_val, reg_list


if __name__ == "__main__":

    import argparse
    parser = argparse.ArgumentParser(usage="python3 %(prog)s [-h] pathfile")
    parser.add_argument("pathfile", help="file with paths to files")
    parser.add_argument("outfile", help="file name of output table")
    args = parser.parse_args()

    pathfile = args.pathfile
    outfile = args.outfile

    fastafiles = []
    with open(pathfile, 'r') as p:
        for fasta in p.readlines():
            fastafiles.append(fasta.strip())

    combined_dict = {}
    for fasta in fastafiles:
        K, S, regions = combine_params_regions(fasta)
        combined_dict[(K, S)]=regions

    with open(outfile, 'w+') as w:
        w.write(f'K-val\tS-val\tRegions\n')
        for key, val in combined_dict.items():
            w.write(f'{key[0]}\t{key[1]}\t{val}\n')
