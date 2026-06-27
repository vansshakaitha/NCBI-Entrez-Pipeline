from Bio import Entrez, SeqIO
import pandas as pd
from Bio.SeqUtils import gc_fraction

#INPUT
GENE="TP53"
ORG="Homo sapiens"
RMAX=10

##SEARCH
Entrez.email="vanssha@gmail.com"

handle=Entrez.esearch(db="nucleotide",term=f"{GENE}[Gene] AND {ORG}[Organism]",retmax=RMAX)
record=Entrez.read(handle)
handle.close()

##FETCH
id_list=record["IdList"]
fetch_handle=Entrez.efetch( 
    db="nucleotide",
    id=id_list,
    rettype="gb",
    retmode="text"
)
recs=list(SeqIO.parse(fetch_handle,"genbank"))
fetch_handle.close()

##DataFrame
data=[]
for r in recs:
    accession=r.id
    organism=r.annotations.get("organism","unknown")
    length=len(r.seq)
    gc=round(gc_fraction(r.seq)*100,2)

    data.append({
        "Accession"   : accession,
        "Organism"    : organism,
        "Length"      : length,
        "GC %"        : gc
    })

df=pd.DataFrame(data)
print(df)

##CSV File
df.to_csv(f"{GENE.lower()}_entrez_results.csv", index=False)

