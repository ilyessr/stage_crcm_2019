========================================================
diag_ions_test
=======================================================
**Description**


This tool is based on R package MSnbase (Gatto L, Lilley K) and allows
to find some pics (M/Z) in spectrums of MGF file.

-----

**Input**

- MGF file
- Tolerance (ppm)
- M/Z ratio :
    => whether a file containing M/Z ratio in one column (without a header)
    => whether you can copy/paste some M/Z, each separated by a semicolon

-----

**Output**


A HTML report with a table containing :
- Resume about the spectrums in MGF file
- Table and plots of spectrums containing M/Z wanted
- Table  indicating shared diagnostic ions between spectrums
- Heatmap


-----


**Authors**

Author: Laurent Gatto, Johannes Rainer and Sebastian Gibb with contributions from Guangchuang Yu, Samuel Wieczorek, Vasile-Cosmin Lazar, Vladislav Petyuk, Thomas Naake, Richie Cotton, Arne Smits, Martina Fisher, Ludger Goeminne, Adriaan Sticker and Lieven Clement.

Citation (from within R, enter citation("MSnbase")):

Gatto L, Lilley K (2012). “MSnbase - an R/Bioconductor package for isobaric tagged mass spectrometry data visualization, processing and quantitation.” Bioinformatics, 28, 288-289.


-----


.. class:: infomark


**Galaxy integration**

    Ilyess RACHEDI, Samuel GRANJEAUD's student intern at
    Centre de Recherche en Cancérologie de Marseille (CRCM), France
    27 Boulevard Lei Roure, 13009 Marseille



