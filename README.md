# Tugas-besar-TBFO

## Table Of Contents

* [Problem Description](#problem-description)
* [Project Summary](#project-summary)
* [Members and Responsibilities](#members-and-responsibilities)
* [Program Structure](#program-structure)
* [How To Run](#how-to-run)


## Problem Description 

Dalam proses pembuatan program dari sebuah bahasa menjadi instruksi yang dapat dieksekusi oleh mesin, terdapat pemeriksaan sintaks bahasa atau parsing yang dibuat oleh programmer untuk memastikan program dapat dieksekusi tanpa menghasilkan error. Parsing ini bertujuan untuk memastikan instruksi yang dibuat oleh programmer mengikuti aturan yang sudah ditentukan oleh bahasa tersebut. Baik bahasa berjenis interpreter maupun compiler, keduanya pasti melakukan pemeriksaan sintaks. Perbedaannya terletak pada apa yang dilakukan setelah proses pemeriksaan (kompilasi/compile) tersebut selesai dilakukan.
Dibutuhkan grammar bahasa dan algoritma parser untuk melakukan parsing. Sudah sangat banyak grammar dan algoritma yang dikembangkan untuk menghasilkan compiler dengan performa yang tinggi. Terdapat CFG, CNF-e, CNF+e, 2NF, 2LF, dll untuk grammar yang dapat digunakan, dan terdapat LL(0), LL(1), CYK, Earley’s Algorithm, LALR, GLR, Shift-reduce, SLR, LR(1), dll untuk algoritma yang dapat digunakan untuk melakukan parsing.

## Project Summary

This project is a Formal Language and Automata Theory Project that implements a JavaScript Syntax Parser, using Python. The base theory of the project is that a JavaScript Syntax can be intrepreted as a Context-Free Language, thus can be represented by a Context-Free Grammar, this CFG can then be converted to the CNF and then use the CYK Algorithm to know whether the syntax is accepted by the language or not. Finite Automata is also used to check for invalid variables naming, mathematical expression, etc.

## Members and Responsibilities

| NIM      | NAME                       | RESPONSIBILITIES                                         |
| -------- | -------------------------- | -------------------------------------------------------- |
| 13521045 | Fakhri Muhammad Mahendra   | Context-Free Grammar, Finite Automata                    |
| 13521089 | Kenneth Ezekiel Suprantoni | Context-Free Grammar, Input Parsing, CYK Algorithm       |
| 13521101 | Arsa Izdihar Islam         | Context-Free Grammar, CFG To CNF Converter, Optimization |

## Program Structure 

```
│ .gitignore
│ README.md
│ cfg_to_cnf.py
│ cfg.py
│ cnf.py
│ cyk.py
│ driver_fa_mathexp.py
│ driver_fa_var.py
│ fa_mathexp.py
│ fa_var.py
│ fa.py
│ inputreader.py
│ run.py
│
├─── data
│       │cfg.txt
│       │cnf.txt
│       │func_cfg.txt
│       │func_cnf.txt
│       │function_terminals.txt
│       │loopnswitch_cfg.txt
│       │loopnswitch_cnf.txt
│       │loopnswitch_terminals.txt
│       │terminals.txt
│       
├─── test
```

## How To Run

The program can be executed by following these steps:

1. input the CFG in `data/CFG.txt` `data/func_cfg.txt` `data/loopnswitch_cfg.txt`
2. convert the CFG to CNF by executing `python cfg_to_cnf.py` the CNF will be stored at `data/CNF.txt` `data/func_cnf.txt` `data/loopnswitch_cnf.txt`
3. input test files into the `test` folder
4. run the program by executing `run.py` then `./test/acc/filename.js` or `./test/err/filename.js` or `test/acc` or `./test/err` to test the whole accepted or error folder
5. the program will output the result, whether it is accepted or rejected

1. To run the driver for FA checking for variable name checking and math expression, do `python driver_fa_mathexp.py` for math expression, and `python driver_fa_var.py` for variable name checking
2. The program will ask for an input of variable name or mathematical expression
3. After the input is provided, the program will output whether it is a valid variable name or mathematical expression
