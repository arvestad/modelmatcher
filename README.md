# modelmatcher: Rapid identification of evolutionary models

This tool reads multiple sequence alignments and determines a suitable sequence
evolution model for your phylogenetic analysis.

## Usage

Example usage:

``` shell
$ modelmatcher inputfile.fasta
```

### Options


### Input formats

Input format is detected automatically from the following list, but can also be
requested specifically.

* FASTA
* Phylip
* Nexus
* Clustal
* Stockholm

### Output

Output is given as a simple text table, or in JSON format for easy parsing by
other scripts, ranking possible models in preference order. For example, the command above may yield a table looking like:

```
WAG             7.972
VT              8.238
BLOSUM62        8.478
JTT             8.864
JTT-DCMUT       8.917
LG              9.984
DCMUT          10.467
Dayhoff        10.495
FLU            11.211
HIVb           12.853
RtREV          14.048
cpREV          14.186
HIVw           17.338
MtZoa          18.476
MtMAM          21.453
mtArt          21.741
MtREV          22.059
```
Each model is given with its modelmatcher score.

Alternatively, the same analysis can look like:

``` shell
$ modelmatcher  --json  inputfile.fasta
{"n_observations": 863692, "infile": "inputfile.fasta", "n_seqs": 66, "model_ranking": [["WAG", 7.972410383355675], ["VT", 8.238362164888876], ["BLOSUM62", 8.478000205922985], ["JTT", 8.863578165338444], ["JTT-DCMUT", 8.917496451351846], ["LG", 9.983874357603963], ["DCMUT", 10.466872509785343], ["Dayhoff", 10.49522598111376], ["FLU", 11.21137482805874], ["HIVb", 12.852877789672046], ["RtREV", 14.047539707772572], ["cpREV", 14.18648653904322], ["HIVw", 17.338193829402], ["MtZoa", 18.475515151949153], ["MtMAM", 21.452528293860837], ["mtArt", 21.740741039472418], ["MtREV", 22.058622800684176]]}
```


## Install

Recommended installation is:
```
pip install --upgrade pip
pip install alv
```
