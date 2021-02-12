def labelCard(categoriaColor="transparent"):
   return """ # lbCategoria {
    color: """ + categoriaColor + """;
    background-color: transparent;
    border: 0px;
    font-size: 16pt;
    font-family: Ubuntu;
    font-weight: bold;
}"""

def frameCategoriaCard(categoriaColor="transparent"):
    return """#frCategoria {
	background-color: """ + categoriaColor + """;
	
	border-bottom-left-radius: 12px;
	border-bottom-right-radius: 12px;
	border-top-left-radius: 0px;
	border-top-right-radius: 0px;	
}"""