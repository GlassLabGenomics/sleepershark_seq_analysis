#!/bin/bash
#SBATCH --partition=t1small
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=100MB
#SBATCH --array=1-10

set -o errexit
#set -o nounset

module --quiet purge
module load GCCcore/11.3.0
module load BioPerl/1.7.8

ulimit -l unlimited

### Read in K, S values based on array ID
INFILE=$1
IDX=($SLURM_ARRAY_TASK_ID)
echo "Run in array #: $IDX"
pair=$(sed -n ${IDX}p $INFILE)
echo "Read in k, s pair: $pair"
arrPAIR=($pair)

KVAL=${arrPAIR[0]}
SVAL=${arrPAIR[1]}

REF='reference.fasta'
IN='ingroup.fasta'
OUT='outgroup.fasta'
TSV=1 

eval "$(conda shell.bash hook)"
conda activate bioenv

unikseq.pl -r $REF -i $IN -o $OUT -k $KVAL -s $SVAL -v $TSV
