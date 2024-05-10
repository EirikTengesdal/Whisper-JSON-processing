#!/usr/bin/env python3
"""
Script for converting Whisper JSON output to CSV file.

This script converts a JSON file containing captions into a CSV file.
The present purpose is to prepare the data for further analysis in R.
Change attributes in `csv.writer(f)` (e.g., `delimiter=";"`) to fit your needs.
Change attributes in `writer.writerow()` to fit your needs.

File:
    Whisper-JSON_to_CSV.py

History (DD.MM.YYYY):
    10.05.2024 / Created script.
    
Author:
    Eirik Tengesdal¹˒²

Affiliations:
    ¹ OsloMet – Oslo Metropolitan University (Assistant Professor of Norwegian)
    ² University of Oslo (Guest Researcher of Linguistics)

Email:
    eirik.tengesdal@oslomet.no
    eirik.tengesdal@iln.uio.no
    eirik@tengesdal.name

Licence:
    MIT License

    Copyright (c) 2024 Eirik Tengesdal

    Permission is hereby granted, free of charge, to any person obtaining a
    copy of this software and associated documentation files (the "Software"),
    to deal in the Software without restriction, including without limitation
    the rights to use, copy, modify, merge, publish, distribute, sublicense,
    and/or sell copies of the Software, and to permit persons to whom the
    Software is furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
    DEALINGS IN THE SOFTWARE.
"""

import csv
import json
import os

# Define the path to the folder containing the JSON file(-s) and the name of the JSON file(-s)
path = "C:/Users/eirik/OneDrive - OsloMet/Documents/Github/Whisper-JSON-processing/"

# By default, all JSON files in the folder are converted into one CSV file containing all the captions
# If the user wants to convert a specific JSON file in the folder, the user can specify the file name.
# If so, set the `jsonfilelist_enabled` variable to `False` and update the `jsonfile` variable with the name of the specific JSON file you want to convert
jsonfilelist_enabled = True

if jsonfilelist_enabled:
    jsonfilelist = [f for f in os.listdir(path) if f.endswith(".json")]
if not jsonfilelist_enabled:
    jsonfile = "NO0170dbWhisper"

# Now we export the captions into a CSV file that can be imported into R for further analysis.
# We use `caption["text"].strip()`` to remove leading and trailing whitespaces from the input `text` field.

# If the user wants to convert all JSON files present in the folder, we loop through the JSON files and convert them into one CSV file containing all the captions
if jsonfilelist_enabled:
    with open(f"{path}Whisper_results.csv", "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "id", "seek", "start", "end", "text", "tokens", "temperature", "avg_logprob", "compression_ratio", "no_speech_prob"])
        for file in jsonfilelist:
            captions = json.load(open(f"{path}{file}"))
            for caption in captions:
                writer.writerow([file[:-5],  # Remove the last five characters (".json") from the filename, for ID
                                 caption["id"],
                                 caption["seek"],
                                 caption["start"],
                                 caption["end"],
                                 caption["text"].strip(),
                                 caption["tokens"],
                                 caption["temperature"],
                                 caption["avg_logprob"],
                                 caption["compression_ratio"],
                                 caption["no_speech_prob"]]
                                 )
            print(f"Wrote contents from '{file}' to CSV file.")
        print(f"Conversion from JSON file(-s) to the following CSV file completed.\n'{path}Whisper_results.csv'.")

if not jsonfilelist_enabled:
    with open(f"{path}{jsonfile}.csv", "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(["name","id", "seek", "start", "end", "text", "tokens", "temperature", "avg_logprob", "compression_ratio", "no_speech_prob"])
        captions = json.load(open(f"{path}{jsonfile}.json"))
        for caption in captions:
            writer.writerow([jsonfile,  # Do not add the file extension (".json") to the filename, for ID
                             caption["id"],
                             caption["seek"],
                             caption["start"],
                             caption["end"],
                             caption["text"].strip(),
                             caption["tokens"],
                             caption["temperature"],
                             caption["avg_logprob"],
                             caption["compression_ratio"],
                             caption["no_speech_prob"]]
                             )
        print(f"Wrote contents from '{jsonfile}' to the following CSV file:\n'{path}{jsonfile}.csv'.")
        print("Conversion from JSON file to CSV file completed.")