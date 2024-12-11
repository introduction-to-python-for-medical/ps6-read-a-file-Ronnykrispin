def create_codon_dict(file_path):
    d = {}
     file=open(file_path)
      rows=file.reaflines()
      file.close()
      for row in rows:
          codon = cells[0]
          amino_acid = cells[2]
          d[codon] = amino_acid
    return d
