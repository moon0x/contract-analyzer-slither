# contract-analyzer
Analyzer of contracts on Etherscan using slither

## Prerequisite
```
Python ^3.6
slither
solc
solc-select
```

## How to use
1. Prepare csv file for contract info from Etherscan and name to `contracts.csv`
2. Run this command to analyze contracts.
    `python analyzer.py`
3. Analyze result file is created at `result.csv`
4. Check output folder for each contract address.

## References

```
https://github.com/crytic/slither
https://github.com/crytic/solc-select

