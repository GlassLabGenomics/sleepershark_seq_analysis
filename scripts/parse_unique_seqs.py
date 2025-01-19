#!/usr/env/bin python3
"""
parse_unique_seqs.py

Parses out k, s values and unique sequences (if any)
from unikseq results: *unique.fa
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

def read_fasta(infile):
    with open(infile, 'r') as f:
        fastadict = parse_fasta(f.readlines())
    return fastadict

def get_region_from_str(headerstr):
    region = headerstr.split('region')
    region = region[1].split('_')[0]
    region = region[0].split('-')
    return (region[0], region[1])

def parse_header(fastadict):
    """Takes in a fastadict and parses out info
    from the header, returns regions as a list"""
    regionlist = []
    for entry in fastadict:
        header = next(iter(entry))
        start, stop = get_region_from_str(header)
        regionlist.append((start, stop))
    return regionlist



if __name__ == "__main__":

    import argparse
    parser = argparse.ArgumentParser(usage="python3 %(prog)s [-h] pathfile")
    parser.add_argument("pathfile", help="file with paths to files")
    args = parser.parse_args()

    pathfile = args.pathfile
