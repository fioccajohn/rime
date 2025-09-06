# Rime

A command-line tool named `rime` for finding rhymes and other phonetic relationships in the CMU Pronouncing Dictionary.

This project is intended to be developed into a full-featured command-line tool. The recommended library for building the CLI is [Click](https://click.palletsprojects.com/), as it provides a simple and composable way to create a clean command-line interface with support for subcommands.

## Files

*   `cmu_parser.py`: A Python script that parses the `CMU Pronouncing Dictionary.txt` file and creates `cmu_dict.csv`.
*   `cmu_dict.csv`: A CSV file containing the parsed data from the CMU Pronouncing Dictionary, with columns for word, phonemes, syllable count, stress pattern, rhyme, alliteration, assonance, and consonance.
*   `CMU Pronouncing Dictionary.txt`: The raw data from the CMU Pronouncing Dictionary.
*   `TODO.md`: A list of planned features and improvements.

## Usage

To parse the dictionary, run the following command:

```bash
python3 cmu_parser.py
```

This will generate the `cmu_dict.csv` file.

## Future Features

Please see the `TODO.md` file for a list of features that are planned for this project.
