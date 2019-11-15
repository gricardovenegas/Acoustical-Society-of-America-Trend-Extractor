# Acoustical-Society-of-America-Trend-Extractor

## Summary
A python script that extracts the number of search results in asa.scitation.org per year for a given search term, start date, and end date.
The table of values is saved as a CSV file 'out.csv' in the current directory.

## Usage
To run with the command line, enter the following:

python extract_occurences_JASA.py '\<search term>' \<start date> \<end date>

If you want to search for terms in quotations, connect terms with +

For example: "climate change" should be entered as climate+change

## Example
python extract_occurences_JASA.py 'climate+change' 2000 2019

## Credit
extract_occurences_JASA.py was modified for the Acoustical Society of America 
from extract_occurences.py created by Volker Strobel - volker.strobel87@gmail.com http://doi.org/10.5281/zenodo.1218409

Please use the following citation:

Gabriel R. Venegas. (2019, November 15). gricardovenegas/acoustical-society-of-america-trend-extractor: First release (Version v1.0.0). Zenodo. http://dio.org/10.5281/zenodo.3543695
