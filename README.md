# NCBI Entrez Gene Pipeline

A Python pipeline that searches NCBI's nucleotide database for any gene of interest,
fetches the top GenBank records, and exports key sequence metadata to a CSV file.

## What it does

- Searches NCBI's nucleotide database using the Entrez API
- Fetches the top 10 GenBank records for a given gene and organism
- Extracts accession number, organism, sequence length, and GC content
- Exports results to a CSV file named after the gene

## Why BRCA1 and TP53?

BRCA1 and TP53 are two of the most well-studied genes in cancer biology.
BRCA1 is associated with hereditary breast and ovarian cancer, while TP53 is a
tumour suppressor gene mutated in over 50% of all human cancers. These genes were
used to validate the pipeline against real, clinically relevant data.

## Tools & Libraries

- Python 3
- Biopython (`Bio.Entrez`, `Bio.SeqIO`, `Bio.SeqUtils`)
- pandas

## How to run

1. Clone the repo
2. Install dependencies: `pip install biopython pandas`
3. Open `entrez_pipeline.py` and set your parameters at the top:

```python
    GENE = "TP53"          # change to any gene
    ORG = "Homo sapiens"   # change to any organism
    RETMAX = 10            # number of records to fetch
```

4. Run: `python entrez_pipeline.py`
5. Output CSV will be saved as `{gene}_entrez_results.csv`

## Sample Output

| Accession | Organism | Length | GC % |
|---|---|---|---|
| NG_017013.2 | Homo sapiens | 32772 | 48.96 |
| PZ086170.1 | Homo sapiens | 123 | 65.04 |
| PX584652.1 | Homo sapiens | 1182 | 56.94 |
| PX584651.1 | Homo sapiens | 1182 | 56.85 |
| PX584650.1 | Homo sapiens | 1182 | 56.77 |
| NR_176326.1 | Homo sapiens | 2399 | 53.48 |

## Author

Vanssha Kaitha | Genomics Data Pipeline
