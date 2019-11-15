# Acoustical-Society-of-America-Trend-Extractor

A python script that extracts the number of search results per year for a given search term, start date, and end date.
The table of values is saved as a CSV file 'out.csv' in the current directory.

To run with the command line, enter the following:

python extract_occurences_JASA.py '\<search term>' \<start date> \<end date>

If you want to search for terms in quotations, connect terms with +

For example: "climate change" should be entered as climate+change

Example:

python extract_occurences_JASA.py 'climate+change' 2000 2019
