from os import listdir, system
from os.path import isfile, join
exp_dir = [f for f in listdir("./") if f[0]+f[1]+f[2]+f[3] == "run_" and f[-1] == "s"][0]
for exp in listdir(f"{exp_dir}/configs/"):
    system(f"python run_experiment.py ./{exp_dir}/configs/{exp}")