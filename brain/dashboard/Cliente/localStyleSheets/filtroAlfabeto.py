def estiloBotoesFiltro():
    return """
        QPushButton {
            background-color: transparent;
            border: 0px;
            font-size: 12px;
            font-family: Ubuntu;
        }
        QPushButton::hover{
            border: 0px solid;
            border-radius: 10px;
            background-color: #838689;
            color: #fff;
            font-size: 16px;
            font-family: Ubuntu;  
        }"""

def estiloLabelFiltro():
    return """
        QLabel {
            background-color: transparent;
            border: 0px;
        }
        """