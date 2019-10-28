All my work was done in a Docker image. Here you can find the six tools that I created :
- GO GSEA
- KEGG GSEA
- GO over-representation test
- KEGG over-representation test
- Diagnostic ions test (mass spectrometry)
- Formatting fasta files

These tools are intended to be integrated on Galaxy. So you can install them without needing Docker but you need Galaxy. 
To integrate these tools, simply move the six folders in the tools folder of your personal Galaxy and add these lines in the tool_conf.xml.sample:

  <section id="fasta_format_section" name="Fasta Format">
    <tool file="fasta_format/fasta_format.xml" />
  </section>
  <section id="term_enrich_section" name="Cluster Profiler">
    <tool file="go_term_enrich/go_term_enrich.xml" />
    <tool file="kegg_enrich/kegg_enrich.xml" />
    <tool file="kegg_gsea/kegg_gsea.xml" />
    <tool file="go_gsea/go_gsea.xml" />
  </section>
  <section id="diag_ions_test_section" name="Diagnostic Ions Test">
    <tool file="diag_ions_test/diag_ions_test.xml" />
  </section>


Necessary packages R (3.5>) :

- MSnbase
- clusterProfiler
- DT
- enrichplot
- tools 
- readxl
- the latest version of pandoc.

You will find in each folder a READ.ME concerning the tool in question.



