import cx_Freeze

executables = [cx_Freeze.Executable(script="main.py", icon="imagens/carro.ico")]

cx_Freeze.setup(
    name="Jogo Matematica do Fusca",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ["imagens", "acerto.wav", "engine-loop-1.wav", "engine-loop-1-normalized.wav", "start.mp3", "Explosion.wav", "dados.txt", "ranking.txt"]
                           }}, executables=executables)