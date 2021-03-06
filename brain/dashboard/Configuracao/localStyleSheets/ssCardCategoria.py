colors = {
    0: "#1abc9c",
    1: "#2ecc71",
    2: "#3498db",
    3: "#9b59b6",
    4: "#34495e",
    5: "#f1c40f",
    6: "#e67e22",
    7: "#e74c3c",
    8: "#bdc3c7",
    9: "#95a5a6"
}


def botoesStyleSheet(cor='#fff'):
    return """
    QRadioButton {
    background-color: transparent;
    }
    
    QRadioButton::indicator::unchecked {
	background-color:""" + cor + """;
	border-radius: 6px;
}

QRadioButton::indicator::checked {
	background-color:""" + cor + """;
	border-radius: 6px;
	border: 3px solid white;
}"""


def cardCategoriaBg(modo=None):
    if modo == 'inserir':
        backgroundColor = "rgba(237, 201, 81, 255)"
    elif modo == 'excluir':
        backgroundColor = "rgb(235, 114, 75)"
    else:
        backgroundColor = "rgba(136, 138, 133, 170)"

    return """#frTopBg {
	background-color: """ + backgroundColor + """;	
	border-top-left-radius: 12px;
	border-bottom-right-radius: 12px;
	border-top-right-radius: 12px;
	border-bottom-left-radius: 2px;
}"""


def framePlanoBg(modoEdicao: bool):
    if modoEdicao:
        backgroundColor = 'rgba(255, 255, 100, 80);'
    else:
        backgroundColor = 'rgba(238, 238, 236, 150);'

    return """ #frCriaPlanos {
    background-color: """ + backgroundColor + """
	border-radius: 12px;
}"""
