<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="2.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:outline="http://wkhtmltopdf.org/outline"
                xmlns="http://www.w3.org/1999/xhtml">
    <xsl:output doctype-public="-//W3C//DTD XHTML 1.0 Strict//EN"
                doctype-system="http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitiona
l.dtd"
                indent="yes" />
    <xsl:template match="outline:outline">
        <html>
            <head>
                <title>Table of Contents</title>
                <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
                <style>
					body {
					  font-family: Source Sans Pro,Helvetica Neue,Arial,sans-serif;
					  color: #333;
					}
                    h1 {
                    text-align: center;
                    font-size: 20px;
                    }
                    div {
						background: url('https://i.imgur.com/7flVb8Q.png');
						background-repeat: repeat-x;
						background-size: 6px 1px;
						background-position: bottom;
						padding-bottom: 4px;						
					}
                    span {float: right; }
                    li {list-style: none;}
					ul {
                    font-size: 20px;

					}
                    ul ul {font-size: 90%; }
                    ul {padding-left: 0em; }
                    ul ul {padding-left: 1.5em;}
                    a {text-decoration:none; color: black;}
					.level-2, .level-3 {margin-top: 5px}
					.level-1{ margin-top: 15px;}
					.level-1 > .level-1, .level-1 > .level-1 > .level-1 {margin-top: 5px}
					.level-4, .level-5, .level-6{display: none;}
                </style>
            </head>
            <body>
                <h1>Table of Contents</h1>
                <ul><xsl:apply-templates select="outline:item/outline:item"/></ul>
            </body>
        </html>
    </xsl:template>
    <xsl:template match="outline:item">
        <li class="level-{count(ancestor::*) - 1}">
            <xsl:if test="@title!=''">
                <div>
                    <a>
                        <xsl:if test="@link">
                            <xsl:attribute name="href"><xsl:value-of select="@link"/></xsl:attribute>
                        </xsl:if>
                        <xsl:if test="@backLink">
                            <xsl:attribute name="name"><xsl:value-of select="@backLink"/></xsl:attribute>
                        </xsl:if>
                        <xsl:value-of select="@title" />
                    </a>
                    <span> <xsl:value-of select="@page" /> </span>
                </div>
            </xsl:if>
            <ul class="level-{count(ancestor::*) - 1}">
                <xsl:comment>added to prevent self-closing tags in QtXmlPatterns</xsl:comment>
                <xsl:apply-templates select="outline:item"/>
            </ul>
        </li>
    </xsl:template>
</xsl:stylesheet>