#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Ilyess RACHEDI <ilyess.rachedi@etu.univ-amu.fr>
#
#    This program consists of :
#    - Parser a fasta file
#    - Format the headers
#    - Write the new fasta file output
#
#
# Usage:  python3 parser_fasta.py [-h] -i INFILE [-f FORMATHEADER [FORMATHEADER ...]]
#

import re
import argparse
import os.path
import collections

def parser_multi_fasta(fasta_file):
    '''
    Return a dictionnary dico_seq[ID]= seq
    nom_fichier: str : name of the fasta file
    '''
    ID=""
    seq=""
    liste_seq =[]

    while True :
        line=fasta_file.readline()           # Reading line by line
        if line == "" :                      # if it's the last line
            liste_seq.append([ID, seq])      # Add the last sequence
            break                            # End of the file, break the while loop
        elif line.startswith('>') and seq !="":   # If the line is a header
            ID = line.rstrip('\n\t ')        # New ID (current line)
            liste_seq.append([ID, seq])      # Add the previous sequence
            seq = ''                         # New seq (next line)
        elif line.startswith('>') and seq =="":   # If the line is a header
            ID = line.rstrip('\n\t ')        # New ID (current line)
            seq = ''                         # New seq (next line)
        else:
            seq = seq + line.rstrip('\n\t ') # Concatenate sequences lines removing line break
    return liste_seq


def format_header(liste_seq, liste_args = None):
    """
    Format the non conventional header
    Return a list of [id,sequence]
    liste_seq : list of [id,sequence]
    liste_args : list of information to remove of the uniprot header
    """
    liste_regex = [re.compile("^>[0-9a-zA-z.]+[^|]$"),                                            # CASE N°1 ex : >g1.t1
                   re.compile("^>[A-Za-z0-9]+\|[A-Za-z0-9]+\|[A-Za-z0-9]+_[A-Za-z0-9]+$"),        # CASE N°2 ex : >lcl|F1R2T3-LvH|vtg7_DANRE
                   re.compile("^>[A-Za-z0-9]+\|[A-Za-z0-9]+\|[A-Za-z0-9]+_[A-Za-z0-9]+[ \t]+.+")  # CASE N°3  conventional uniprot header
                  ]

    dico_regex = {"OS" : re.compile("OS=[A-Za-z0-9 ]+[ \t]+"),  # OrganismSpecies
                  "GN" : re.compile("GN=[A-Za-z0-9 ]+[ \t]+"),  # GeneName
                  "PE" : re.compile("PE=[0-9]+ "),              # ProteinExistence
                  "SV" : re.compile("SV=[0-9]+")                # SequenceVersion
                }
    for liste in liste_seq :                        # For each couple [id,seq] in the list
        ID = liste[0]                               # Extraction of the header
        if liste_regex[0].match(ID) :               # CASE N°1
            ID = ">usr" + "|" + ID[1:] + "|"  + ID[1:]  + " " + ID[1:]  # Formatting
            liste[0] = ID                           # Replacement of the old header by the new one
        elif liste_regex[1].match(ID) :             # CASE N°2
            ID = ID + " " + ID[1:].split("|")[-1]   # Formatting
            liste[0] = ID                           # Replacement of the old header by the new one
        elif liste_args != ['None'] and liste_args != None :   # CASE N°3 : we want to remove some informations from uniprot header
            if liste_regex[2].match(ID) :           # If the header is a uniprot header format
                for arg in liste_args:              # For each chosen arguments we want to remove
                    if arg in dico_regex :          # If the current arg is one defined
                        ID = re.sub(dico_regex[arg],"", ID) # The corresponding pattern is removed of the header
            liste[0] = ID                           # Replacement of the old header by the new one
    return liste_seq


def is_duplicate(liste_seq):
    """
    Check if there are duplicates header in fasta file.
    If it's the case, change of the header
    """
    dico_duplicate = {}
    liste_IDs = [ID for ID,seq in liste_seq]        # List comprehension to retrieve the IDs
    liste_duplicate_IDs = [[k,v] for k,v in collections.Counter(liste_IDs).items() if v > 1] # List comprehension to retrieve the IDs doublons
    if len(liste_duplicate_IDs) != 0:
        for ID, nbr_duplicate in liste_duplicate_IDs :
            i = 1                    # Number of same header seen
            for liste in liste_seq : # For each [header,seq] in list
                if ID == liste[0] :  # If the identical ID matches with the current ID
                    new_header = liste[0] + " identical header " + str(i) + "/" + str(nbr_duplicate)
                    if ID in dico_duplicate :
                        dico_duplicate[ID].append(new_header) # Add to the list of modificated header
                    else :                                    # If the ID is unknown
                        dico_duplicate[ID] = [new_header]     # Create a list associated to a key
                    liste[0] = new_header
                    i +=1

    return liste_seq, dico_duplicate


def write_output(file_name, liste_seq, width = 60):
    """
    Display output fasta format. Line width by default is 60
    Return a fasta file
    """
    with open(path_output,"w") as f:
        for ID, seq in liste_seq:
            f.write(ID + '\n')
            # ~ print(ID)
            nbr_lines, rest = divmod(len(seq),width) # Determination of the necessary number line
            start = 0
            end = width
            for i in range(nbr_lines):
                current_seq = seq[start:end] + '\n'  # Moving in the sequence with a frame read [start:end]
                f.write(current_seq)
                # ~ print(current_seq, end="")
                start += width                       # New value of start of the frame
                end   += width                       # New value of end of the frame read
            if rest != 0 :                           # If the sequence is not totally add (not multiple of width)
                current_seq = seq[start:] + '\n'     # Take the last elements of the sequence
                f.write(current_seq)
                # ~ print(current_seq, end="")


if __name__ == '__main__':

    # Definition of arguments
    program_description = """

    ====================== Welcome =======================

    This program consists of :
    - Parser a fasta file
    - Format the headers
    - Write the new fasta file output
    ------------------------------------------------------
    Written by Ilyess RACHEDI, Samuel GRANJEAUD's intershiper at
    Centre de Recherche en Cancérologie de Marseille (CRCM), France
    27 Boulevard Lei Roure, 13009 Marseille

    """
    parser = argparse.ArgumentParser(description = program_description, formatter_class = argparse.RawTextHelpFormatter)
    required = parser.add_argument_group('Required arguments')
    optional = parser.add_argument_group('optional arguments')
    # Input argument
    required.add_argument('-i', '--infile',
                        type=argparse.FileType("r"),
                        nargs=1,
                        required=True,
                        help="Path of the fasta file")
    # Output argument
    required.add_argument('-o', '--output',
                        type=str,
                        nargs=1,
                        required=True,
                        help="Path of the fasta file")
    # Width argument
    optional.add_argument('-w', '--width',
                        type=int,
                        nargs="?",
                        required=False,
                        help="Width of the fasta sequences lines")
    # Formatheader argument
    optional.add_argument('-f', '--formatheader',
                        type=str,
                        nargs='*',
                        required=False,
                        help="""You can choose what informations DON'T appear in the uniprot header of sequences : \n
                                OS : OrganismName\n
                                GN : GeneName\n
                                PE : ProteinExistence\n
                                SV : SequenceVersion """)
    # info.txt  argument
    optional.add_argument('-inf', '--info',
                        type=str,
                        nargs= 1,
                        required=False,
                        help="Path of info.txt. This file only exists if there are header doublons in fasta file, and give them"
                        )
    args = parser.parse_args()

    # Variables
    fasta_file = args.infile[0]                      # Fasta file
    liste_args = args.formatheader                   # List of arguments to remove of header
    width = args.width                               # Width of the lines
    path_output = args.output[0]
    if args.info != None and args.info != ['None'] : # If info parameter contains something, and for Galaxy something different of ['None']
        path_output_info = args.info[0]
    else :
        path_output_info = "formatted_" + (os.path.basename(fasta_file.name))   # Path of the info.txt by default


    # Parser
    liste_seq = parser_multi_fasta(fasta_file)          # Retrieve the sequences in a list

    # Formatting header

    if fasta_file.name.endswith('.dat') :  # If the script is running on galaxy
        if liste_args != None :
            liste_args = liste_args[0].split(",")           # As galaxy give a liste of one element with the selection input type, we need to separate all the elements
            liste_seq = format_header(liste_seq,liste_args) # Format header
        else :
            liste_seq = format_header(liste_seq)            # Format header
    else :
        if liste_args != None :
            liste_seq = format_header(liste_seq,liste_args) # Format header
        else :
            liste_seq = format_header(liste_seq)            # Format header

    # Check duplicates
    liste_seq, dico_duplicate = is_duplicate(liste_seq)

    # Write Output
    if width != None :
        write_output(fasta_file.name, liste_seq, width)
    else :
        write_output(fasta_file.name, liste_seq)

    # Write doublons
    if len(dico_duplicate) != 0 :
        with open(path_output_info,"w") as f:
            f.write("Some headers had to be changed because they are identicals :\n" )
            for header, new_headers in dico_duplicate.items() :
                f.write(header + " :\n " + str(new_headers) + '\n')
            f.write("Maybe their sequences are also the same, pay attention ")

