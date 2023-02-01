from cgitb import reset


def identify_genes(k):
    # replace this function with your algorithm
    return ['MYC', 'PTGES3', 'HCFC1', 'BRCA1', 'HTT', 'BRCA2', 'EED', 'WT1', 'RPL5', 'NRAS', 'FLT3', 'IDH2', 'TUBA1A', 'PTEN', 'RAG2', 'MAGEC3',  'CREBBP', 'NXF1', 'TRIM25', 'ASXL1'][:k]

def run(parameter=5):
    result = identify_genes(parameter)
    return result