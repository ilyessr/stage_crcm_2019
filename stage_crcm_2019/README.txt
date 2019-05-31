Tout mon travail a été fait dans une image Docker. Ici, vous pouvez retrouver les différents outils que j'ai crée.
Ces outils sont destinés à être intégrer sur Galaxy. Vous pouvez donc les installer sans avoir besoin de Docker. Par contre l'installation de Galaxy est bien evidemment nécessaire. Pour intégrer ces outils, il suffit de déplacer les six dossiers dans le dossier tools de votre Galaxy personnel et ajouter ces lignes dans le tool_conf.xml.sample : 

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



Il faudra penser à installer sur R (3.5>) les packages MSnbase, clusterProfiler, DT, enrichplot, fgsea, tools, readxl ainsi qu'avoir la dernière version de pandoc.

Vous trouverez dans chaque dossier un READ.ME concernant l'outil en question



