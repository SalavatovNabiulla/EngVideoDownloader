import subprocess

print("Start")
path_to_exe = "C:\\Program Files (x86)\\Download Master\\dmaster.exe"
path_to_txt = "C:\\Users\\snmsu\\Desktop\\Untitled.txt"
code = subprocess.Popen([path_to_exe, path_to_txt])
print("Finish")