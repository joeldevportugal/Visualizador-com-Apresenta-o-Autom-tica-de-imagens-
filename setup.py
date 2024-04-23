from cx_Freeze import setup, Executable

# Dependências do aplicativo
build_exe_options = {
    "packages": ["tkinter", "customtkinter","PIL","os"],  # Inclui os pacotes usados no script
}

# Configuração do executável
setup(
    name="Visualizador de Imagens",
    version="0.0.0.0",
    description="Um aplicativo para visualizar imagens feito com Python customtkinter.",
    options={"build_exe": build_exe_options},
    executables=[Executable("visualizador.py", base="Win32GUI")]  
)
