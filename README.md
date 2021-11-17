# Zipf's Law

These Zipf's Law scripts tally the occurrences of words in text
files and plot each word's rank versus its frequency.

## Analyses
The software requirements for the analyses is provided in the `requirements.txt` file. It is managed using [conda](https://conda.readthedocs.io/en/latest/), a package manager.
### Installation
- Install Conda
- Download this repo and activate a pre-configured `conda` environment from the supplied `environment.yml`:
```
git clone https://github.com/forthstate/zipfLaw.git
cd zipfLaw
```
Creation of a virtual environment is advised:
```
conda create -f environment.yml
```
  **OR**   
just install the requirements:
```
pip install -r requirements.txt
```
- Data : Some ebooks are already available in the `data` folder, which also has a markdown file with instructions on how to ge them.

- To process the data and build the figure:
```
make all
```
This should give a `csv` file with the counts of all the words, collated from all the data files; a `png` file with a log-log plot of counts with a curve-fit.  

#### Contributors:
- forthstate
