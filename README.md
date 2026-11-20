# Mini Banking System — Python OOP

Educational CLI supporting savings and current accounts, deposits, withdrawals, transfers and transaction history.

## Run
```bash
cd oop-banking-system
python cli.py
```

## Tests
```bash
cd oop-banking-system
python -m unittest discover -s tests -v
```

## Structure
- `oop-banking-system/cli.py`: CLI
- `oop-banking-system/src/account.py`: account types
- `oop-banking-system/src/bank.py`: account collection and transfers
- `oop-banking-system/tests/test_bank.py`: unit tests

Uses Python standard library only. This is a simulation, **not a real banking application**: it does not provide persistence, secure authentication or financial-grade decimal accounting.

Author: Mohsin Atta.
