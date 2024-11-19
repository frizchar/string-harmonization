# String harmonization
### Overview
We provide python code to harmonize a set of strings $B=(B_1, B_2,...,B_m)$ against another set of strings $A=(A_1, A_2,...,A_n)$.<br>
Specifically :
1. for each element $A_i$ we find the closest match $B_j$ for which the [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance) measure $L_{ij}$ is _max_, hence:<br>
<p align="center">
$L_{ij}=max(L_{ik})$, where $1\leq k \leq m$
</p>

2. to implement this we use the [fuzzywuzzy](https://oracle.github.io/python-cx_Oracle/](https://pypi.org/project/fuzzywuzzy/)) python package 
3. the code outputs each value $A_i$ in the following form: $(A_i, B_j, L_{ij})$, where $1\leq i \leq n$ and $1\leq j \leq m$

### Dependencies
The required packages are included in file ```requirements.txt```.<br>
Python interpreter version used for this project: **3.9.4**
