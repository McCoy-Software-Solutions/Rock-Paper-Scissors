import cx_Freeze

executables = [cx_Freeze.Executable("rockpaperscissors.py")]

cx_Freeze.setup(name="Rock Paper Scissors", options={"build_exe":{"packages":["pygame"],"include_files":[]}},executables=executables)