# Reference model

Run from the repository root:

```bash
python -m unittest discover -s tests -v
python simulations/arithmetic_model.py
```

The model explicitly propagates decimal carries and implements multiplication as repeated addition. It is an oracle for testing the intended arithmetic, not a controller and not a component of the physical calculator.
