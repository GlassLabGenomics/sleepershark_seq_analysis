#!/bin/bash
#SBATCH --partition=bio
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=16
#SBATCH --mem-per-cpu=100MB

set -o errexit
#set -o nounset

module --quiet purge
module load GCCcore/11.3.0
module load BioPerl/1.7.8

ulimit -l unlimited

REF=$1
IN=$2
OUT=$3
KVAL=$4

eval "$(conda shell.bash hook)"
conda activate bioenv

unikseq.pl -r $REF -i $IN -o $OUT -k $KVAL -s $KVAL
