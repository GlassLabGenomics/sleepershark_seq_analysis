library(ggplot2)

dfa<-read.table("unikseq_v1.3.5-r_reference.fasta-i_ingroup.fasta-o_outgroup.fasta-k30-uniqueKmers.tsv", sep="\t", header = TRUE)
my_x_title <- expression(paste("Position of 30-mers on ", italic("S. pacificus"), " Mt genome"))

# Stacked
ggplot(dfa, aes(fill=condition, y=value, x=position)) + 
  geom_col() + labs(x=my_x_title) + ylab("Proportion of species with 30-mers") + coord_flip()



library(ggplot2)
library(ggallin)
library(scales)

dfa<-read.table("unikseq_v1.3.5-r_reference.fasta-i_ingroup.fasta-o_outgroup.fasta-k30-uniqueKmers.tsv", sep="\t", header = TRUE)
my_x_title <- expression(paste("Position of 25-mers on ", italic("C. maximus"), " Mt genome"))

# Stacked
ggplot(dfa, aes(fill=condition, y=value*1000, x=position)) + 
  scale_y_continuous(trans = pseudolog10_trans,breaks=c(-1000,-100,-10,-1,0,1,10,100,1000)) +
  geom_col() + labs(x=my_x_title) + ylab("Proportion (x10) of species with 25-mers") + coord_flip()

unikseq_v1.3.5-r_reference.fasta-i_ingroup.fasta-o_outgroup.fasta-k30-uniqueKmers.tsv