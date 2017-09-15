<?xml version="1.0" encoding="ISO-8859-1" ?>
<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/phyloxml">
  <html>
  <body>
  	<h2>Phylogenetics</h2>
  	<table border="1">
  	<tr bgcolor="#9acd32">
          <th>Branch_length</th>
          <th>Confidence</th>
	  <th>scientific_name</th>
  	</tr>
	<xsl:for-each select="phylogeny/clade/clade/clade/clade/clade">
	<xsl:sort select="confidence" data-type="number" order="descending"/> 
	<xsl:if test="confidence &gt; 80">  
  	<tr align="center">
          <td><xsl:value-of select="branch_length"/></td>
	  <td><xsl:value-of select="confidence"/></td>
	  <td><xsl:value-of select="scientific_name"/></td>
  	</tr>
	</xsl:if>
	</xsl:for-each>
  	</table>
  </body>
  </html>
</xsl:template>
</xsl:stylesheet>
