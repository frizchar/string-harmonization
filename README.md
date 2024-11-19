# String harmonization
### Overview
We provide python code to harmonize a set of strings $B=(B_1, B_2,...,B_m)$ against another set of strings $A=(A_1, A_2,...,A_n)$.<br>
Specifically :
1. for each element $A_i$ we find the element $B_j$ for which the measure _Levenshtein distance_ is _max_
1. to implement this we use the [fuzzywuzzy]([https://oracle.github.io/python-cx_Oracle/](https://pypi.org/project/fuzzywuzzy/)) python package 
1. the code outputs each _i_{th}_ string value from set _A_ in the following format: $(A_i, B_j, L_{ij})$, where $1\leq i \leq n$ and $1\leq j \leq m$

### Dependencies
The required packages are included in file ```requirements.txt```.<br>
Python interpreter version used for this project: **3.9.4**
