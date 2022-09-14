# Algorithms and Data Structures
My plan is to go through different algorithms (and data structures) books and implement
those algorithms and data structures with tests, analysis, visualizations.

Book list:
- [Algorithms Illuminated](https://www.algorithmsilluminated.org/)
  * Algorithms Illuminated: Part 1: The Basics [Tim Roughgarden, 2017] ([sample](https://www.algorithmsilluminated.org/won1sample.pdf))


## Python

### Setup
- `/book/*` and `/tests/*` use only standard library for now
- `/analysis` uses Jupyter Notebooks so use [conda](https://docs.conda.io/en/latest/) environment instead for the kernel
  * there is some problem with kernel setup under Windows using `venv`, hence conda

Virtual environment:
- `python -m venv algos-ds-venv`
- activate: `algos-ds-venv\scripts\activate.ps1`

If `pip install` fails add this: `--trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org`

### Testing
`python -m unittest`


# References
- [number of digits](https://mathworld.wolfram.com/NumberLength.html)
- [merge sort](https://en.wikipedia.org/wiki/Merge_sort)