
========================================================
fasta_format
=======================================================

usage: fasta_format.py [-h] -i INFILE -o OUTPUT [-w [WIDTH]]
                       [-f [FORMATHEADER [FORMATHEADER ...]]] [-inf INFO]

    ====================== Welcome =======================

    This program consists of :
    - Parser a fasta file
    - Format the headers
    - Write the new fasta file output
    ------------------------------------------------------
    Written by Ilyess RACHEDI, Samuel GRANJEAUD's intershiper at
    Centre de Recherche en Cancérologie de Marseille (CRCM), France
    27 Boulevard Lei Roure, 13009 Marseille

    

optional arguments:
  -h, --help            show this help message and exit

Required arguments:
  -i INFILE, --infile INFILE
                        Path of the fasta file
  -o OUTPUT, --output OUTPUT
                        Path of the fasta file

optional arguments:
  -w [WIDTH], --width [WIDTH]
                        Width of the fasta sequences lines
  -f [FORMATHEADER [FORMATHEADER ...]], --formatheader [FORMATHEADER [FORMATHEADER ...]]
                        You can choose what informations DON'T appear in the uniprot header of sequences : 
                        
                                                        OS : OrganismName
                        
                                                        GN : GeneName
                        
                                                        PE : ProteinExistence
                        
                                                        SV : SequenceVersion 
  -inf INFO, --info INFO
                        Path of info.txt. This file only exists if there are header doublons in fasta file, and give them


