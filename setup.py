import cx_Freeze

executables = [cx_Freeze.Executable("making_executable.ipynb")]

cx_Freeze.setup(
    name="Mission_Sanitizer",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["coronavirus.png",'profile (1).png','coronavirus.png',
                                            'anonymous_hacker_computer-wallpaper-800x600.jpg',
                                            'water-droplet.png','background.wav','masked_man_background.jpg',
                                            'explosion.wav','laser.wav']}},
    executables = executables

    )