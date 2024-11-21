# String harmonization
### Overview
We provide a method to harmonize a set of strings $B=\\{B_1, B_2,...,B_m\\}$ against another set of strings $A=\\{A_1, A_2,...,A_n\\}$.<br>
Specifically :
1. to implement this we use the [fuzzywuzzy](https://pypi.org/project/fuzzywuzzy/) python package that utilizes the [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance) measure $L_{ij}$ between two strings $(s_i, s_j)$. The more $(s_i, s_j)$ are alike the highest the value of $L_{ij}$, where $0 \leq L_{ij} \leq 100$
2. for each element $A_i$ we find the closest match $B_j$ for which the [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance) measure $L_{ij}$ is _max_, hence:<br>
<p align="center">
$L_{ij}=max(\{L_{ik}|k\in \\{1,2,\dots,m\\} \})$
</p>

3. the code outputs $n$ pairs in the form $(A_i, B_j, L_{ij})$, where
   -  $A_i$ is the $i_{th}$ element of set $A$
   -  $B_j$ is its best match from set $B$ and
   -  $L_{ij}$ is their _Levenshtein distance_

### Dependencies
The required packages are included in file ```requirements.txt```.<br>
Python interpreter version used for this project: **3.9.4**
