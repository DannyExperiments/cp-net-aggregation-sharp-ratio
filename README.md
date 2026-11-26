# The sharp approximation ratio for parent-restricted CP-net aggregation

For $t\ge 3$ complete binary conditional preference tables, Algorithm 1 of Ali, Yang and Zilles has exact worst-case ratio **2 − 2/t**. It re-optimizes each input parent set. Four leave-one-out OR tables give cost **6** against optimum **4**, answering the source's four-thirds question. The family lifts the representative-voter example of Endriss and Grandi. [Original question, p. 10439](https://ojs.aaai.org/index.php/AAAI/article/download/28911/29733#page=7)

[Paper PDF](paper/manuscript.pdf) · [LaTeX source](paper/manuscript.tex) · [Proof outline](proof/PROBLEM_AND_PROOF.md)

[![Repository verification](https://github.com/DannyExperiments/cp-net-aggregation-sharp-ratio/actions/workflows/verify.yml/badge.svg?branch=main)](https://github.com/DannyExperiments/cp-net-aggregation-sharp-ratio/actions/workflows/verify.yml)
[![Replay verification](https://github.com/DannyExperiments/cp-net-aggregation-sharp-ratio/actions/workflows/replay.yml/badge.svg?branch=main)](https://github.com/DannyExperiments/cp-net-aggregation-sharp-ratio/actions/workflows/replay.yml)
[![PDF build](https://github.com/DannyExperiments/cp-net-aggregation-sharp-ratio/actions/workflows/pdf.yml/badge.svg?branch=main)](https://github.com/DannyExperiments/cp-net-aggregation-sharp-ratio/actions/workflows/pdf.yml)
[![Partial Lean verification](https://github.com/DannyExperiments/cp-net-aggregation-sharp-ratio/actions/workflows/lean.yml/badge.svg?branch=main)](https://github.com/DannyExperiments/cp-net-aggregation-sharp-ratio/actions/workflows/lean.yml)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24572579.svg)](https://doi.org/10.5281/zenodo.24572579)

## The pair that changes the result

![Two rotating cubes of three visible bits, one for each value of the omitted parent. At the highlighted all-zero visible pair, choosing output zero costs three disagreements and choosing output one costs five. The total restricted cost is six and the unrestricted cost is four.](visualization/parent-context-fibers.gif)

When the visible bits are all zero, Algorithm 1 must use one output for the origin and the singleton on the omitted coordinate. The pooled votes choose 0, even though the singleton alone favors 1. Choosing any input parent set incurs this same penalty. The full proof combines the exact construction with the standard averaged best-input upper bound.

[Download the offline explorer ZIP](https://raw.githubusercontent.com/DannyExperiments/cp-net-aggregation-sharp-ratio/v1.0.0/visualization/cp-net-aggregation-sharp-ratio-explorer.zip) · [Worked example and rendering guide](visualization/README.md)

## Scope and checks

The result concerns binary target-attribute swap disagreement under this parent-set restriction. The compatible $4/3$ result for input indegree at most one is due to Ali, Ogundare, Yang and Zilles. [Exact scope](CLAIM_SCOPE_AND_LIMITATIONS.md) · [Literature audit](audits/public_safe_reports/LITERATURE_AUDIT.md)

The exact Python replay enumerates all contexts in the family through 12 inputs. A partial Lean 4 certificate checks the four-input costs, the violating ratio and a vote-count inequality. Internally reviewed, not peer reviewed. [Replay and Lean commands](REPRODUCIBILITY.md) · [Technical disclosure](AI_DISCLOSURE.md) · [Review status](STATUS.md)

DannyExperiments is the preferred citation identity. [Release v1.0.0](https://github.com/DannyExperiments/cp-net-aggregation-sharp-ratio/releases/tag/v1.0.0) · [Version DOI](https://doi.org/10.5281/zenodo.24572579) · [Citation metadata](CITATION.cff)
