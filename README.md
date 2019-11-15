# Acoustical-Society-of-America-Trend-Extractor

A python script that extracts the number of search results per year for a given search term, start date, and end date.
The table of values is saved as a CSV file 'out.csv' in the current directory.

To run with the command line, enter the following:

python extract_occurences_JASA.py '\<search term>' \<start date> \<end date>

If you want to search for terms in quotations, connect terms with +

For example: "climate change" should be entered as climate+change

Example:

python extract_occurences_JASA.py 'climate+change' 2000 2019

# Credit

extract_occurences_JASA.py was modified for the Acoustical Society of America 
from extract_occurences.py created by Volker Strobel - volker.strobel87@gmail.com

Volker Strobel. (2018, April 14). Pold87/academic-keyword-occurrence: First release (Version v1.0.0). Zenodo. http://doi.org/10.5281/zenodo.1218409
