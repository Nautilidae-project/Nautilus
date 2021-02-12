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