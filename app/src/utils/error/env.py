class EnviomentLoadException(Exception):
    def __init__(self) -> None:
        super().__init__("Envioment Load Error")
