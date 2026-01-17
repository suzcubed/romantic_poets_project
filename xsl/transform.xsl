<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet 
    version="1.0" 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:tei="http://www.tei-c.org/ns/1.0">

  <xsl:output method="html" encoding="UTF-8"/>

  <xsl:template match="/">
    <html>
      <head>
        <title>
            <xsl:value-of select="tei:TEI/tei:teiHeader/tei:fileDesc/tei:titleStmt/tei:title"/>
        </title>
      </head>
      <body>
        <h1>
            <xsl:value-of select="tei:TEI/tei:teiHeader/tei:fileDesc/tei:titleStmt/tei:title"/>
        </h1>
        <p>
            <a href="{tei:TEI/tei:teiHeader/tei:fileDesc/tei:titleStmt/tei:author/@ref}">
            <xsl:value-of select="tei:TEI/tei:teiHeader/tei:fileDesc/tei:titleStmt/tei:author"/>
            </a>
        </p>

         <div>
          <xsl:for-each select="tei:TEI/tei:text/tei:body/tei:lg/tei:l">
            <xsl:value-of select="."/>
            <br/>
          </xsl:for-each>
        </div>

      </body>
    </html>
  </xsl:template>

</xsl:stylesheet>
