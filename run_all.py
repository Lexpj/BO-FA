from os import listdir, system
from time import perf_counter
s1 = perf_counter()
exp_dir = [f for f in listdir("./") if f[0]+f[1]+f[2]+f[3] == "run_" and f[-1] == "s"][0]
all_exp = listdir(f"{exp_dir}/configs/")
for i, exp in enumerate(all_exp):
    print(f"({s1})[{perf_counter()-s1}] {i+1}/{len(all_exp)}")
    system(f"python run_experiment.py ./{exp_dir}/configs/{exp}")
    