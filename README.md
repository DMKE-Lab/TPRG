## TPRG
TPRG: Multi-Hop Temporal Knowledge Graph Reasoning with Temporal Path Rules Guidance
This repository contains the implementation of the TPRG architectures described in the paper.
## Installation
* JDK1.8
* IDEA
* Python 3.x (tested on Python 3.6)
* pycharm
* xshell
* xftp
## How to use?
After installing the requirements, run the following command to reproduce results for TPRG:
```
$ java -jar HitBest.jar -train yago1/train.txt -valid yago1/valid.txt -test yago1/test.txt -rule yago1/groundings2.txt -m 10 -n 10585 -k 300 -d 0.01 -c 0.01 -ne 10 -ge 0.025 -gr 0.025 -# 500 -skip 25
$ java -jar 1-Hit1Test.jar -train gdeltROAN/train.txt -valid gdeltROAN/valid.txt -test gdeltROAN/test.txt -rule gdeltROAN/two.txt -m 20 -n 500 -k 300 -d 0.01 -c 0.01 -ne 10 -ge 0.1 -gr 0.1 -# 500 -skip 20
$ java -jar 2-Hit13510Test.jar -train gdeltROAN/train.txt -valid gdeltROAN/valid.txt -test gdeltROAN/test.txt -rule gdeltROAN/two.txt -m 20 -n 500 -k 300 -d 0.01 -c 0.01 -ne 10 -ge 0.1 -gr 0.1 -# 500 -skip 20
```
## Baselines
| Baselines                           | Code                                                         |
| ----------------------------------- | ------------------------------------------------------------ |
| MINERVA                             | [link](https://github.com/shehzaadzd/MINERVA)                |
| TTransE                             | [link](https://github.com/INK-USC/RE-Net)                    |
| HyTE                                | [link](https://github.com/malllabiisc/HyTE)                  |
| TA-TransE / TA-DistMult             | [link](https://github.com/INK-USC/RE-Net)                    |
| DE-TransE / DE-DistMult / DE-SimplE | [link](https://github.com/BorealisAI/DE-SimplE)              |
