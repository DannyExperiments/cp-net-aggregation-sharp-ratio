# Reproduce the checks

Use an existing Python 3.11 or compatible interpreter. The exact replay has no external dependencies.

    python3 -B -I scripts/verify_repository.py
    python3 -B -I verification/src/replay.py

The replay checks every expanded context, every restricted fiber, each prior input's distance, and the upper-bound counting inequality in the stated finite ranges. The complete evidence ZIP contains the same files as the Git tree and includes the checksum ledger.

Use Lean 4.30.0 with its bundled standard library for the partial certificate.

    lean -DwarningAsError=true formal/Q868Certificate.lean

The five declarations check the four-input unrestricted cost, every restricted cost, the two zero-visible fiber costs, the strict four-thirds violation and the general natural-number vote inequality. The compiler reports only the standard axiom propext. The proof that the family is sharp at every input count is given in the manuscript.

[Paper build](paper/BUILD.md) · [Visualization guide](visualization/README.md)
