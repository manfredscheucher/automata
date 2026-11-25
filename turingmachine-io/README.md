# Examples from turingmachine.io

The examples of [turingmachine.io](https://turingmachine.io/) by Andy Li ([turing-machine-viz](https://github.com/aepsilon/turing-machine-viz), BSD 3-Clause, see [LICENSE](LICENSE)), converted to the format of [turingmachinesimulator.com](https://turingmachinesimulator.com/). The comments and exercises are kept.

The `.yaml` files are generated from the `.txt` files with [txt2yaml.py](../simulator/txt2yaml.py), not the original files of turing-machine-viz.

Differences to the originals:

- The blank is always `_`. In `busy-beaver-3`, `busy-beaver-4` and `copy-1s` the blank was `0`, so there `0` is written as `_`. The comments still use the original blank.
- turingmachine.io has no accepting states. Here the states without rules are accepting, except `reject`.
- `repeat-01` never halts, so it has no accepting state (`accept: none`).

Run one, for example:

```bash
python3 ../simulator/minituring.py binary-add.txt 1011+11001
```

`convert.py` did the conversion, with [yaml2txt.py](../simulator/yaml2txt.py):

```bash
python3 convert.py <turing-machine-viz>/src/examples .
```
