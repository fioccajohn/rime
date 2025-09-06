# Rime

## Project Overview

This project is a command-line tool named `rime` for finding rhymes and other phonetic relationships in the CMU Pronouncing Dictionary. It is written in Python and uses the Click library for the command-line interface, pandas for data manipulation, and tabulate for pretty-printing tables.

The project is structured into three main directories:
- `src`: Contains the main source code for the `rime` tool (`rime.py`) and the CMU dictionary parser (`cmu_parser.py`).
- `data`: Contains the raw CMU Pronouncing Dictionary (`CMU Pronouncing Dictionary.txt`) and the parsed CSV file (`cmu_dict.csv`).
- `tests`: Contains unit tests for the `rime` tool.

## Building and Running

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

3.  **Run the `rime` tool:**

    The `rime` tool is installed as a symbolic link in `~/.local/bin`, so it can be run directly from the command line.

    ```bash
    rime <command> [options]
    ```

    For example:

    ```bash
    rime rhyme time
    rime consonance gemini --fields 'word|phonemes' --format csv
    ```

## Development Conventions

*   **Code Style**: The code follows the general conventions of Python, with a focus on readability and maintainability.
*   **Testing**: The project uses the `unittest` module for testing. Tests are located in the `tests` directory and can be run with the following command:

    ```bash
    python3 -m unittest discover tests
    ```

*   **Dependencies**: Project dependencies are managed in the `requirements.txt` file.
*   **File Structure**: The project is organized into `src`, `data`, and `tests` directories to separate source code, data, and tests.
