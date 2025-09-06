# Rime

A command-line tool for finding rhymes and other phonetic relationships in the CMU Pronouncing Dictionary.

## Features

*   Find words with the same rhyme, consonance, alliteration, assonance, syllable count, or stress pattern.
*   Filter the output to show only the fields you want.
*   Output the results in a variety of formats, including a pretty table, CSV, and JSON.
*   Send the results directly to `visidata` for interactive exploration.

## Installation

1.  **Set up the environment and install dependencies:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

2.  **Parse the CMU Pronouncing Dictionary:**

    This step is only necessary if the `cmu_dict.csv` file is not present in the `data` directory.

    ```bash
    python3 src/cmu_parser.py
    ```

3.  **Install the `rime` tool:**

    ```bash
    ln -s "$(pwd)/src/rime.py" ~/.local/bin/rime
    ```

## Usage

```bash
# Get information about the dictionary
rime info

# Find words that rhyme with "time"
rime rhyme time

# Find words with the same consonance as "gemini", and show only the word and phonemes
rime consonance gemini --fields 'word|phonemes'

# Find words with the same alliteration as "test" and output in CSV format
rime alliteration test --format csv

# Find words with the same assonance as "hello" and open in visidata
rime assonance hello --visidata
```

### Commands

*   `info`: Prints information about the dictionary.
*   `rhyme <word>`: Finds words that rhyme with the given word.
*   `consonance <word>`: Finds words with the same consonance as the given word.
*   `alliteration <word>`: Finds words with the same alliteration as the given word.
*   `assonance <word>`: Finds words with the same assonance as the given word.
*   `syllable-count <word>`: Finds words with the same syllable count as the given word.
*   `stress-pattern <word>`: Finds words with the same stress pattern as the given word.

### Options

*   `--fields, -f`: Fields to return, e.g. `"*"` for all, or `"col1|col2"`. Defaults to `*`.
*   `--format`: Output format. Can be `df`, `csv`, or `json`. Defaults to `df`.
*   `--table-format`: Table format for df output. Can be any format supported by the `tabulate` library. Defaults to `simple`.
*   `--visidata`: Send output to `visidata`.

## Development

To run the tests, use the following command:

```bash
python3 -m unittest discover tests
```