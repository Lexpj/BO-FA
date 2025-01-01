from os import listdir, system
from os.path import isfile, join
exp_dir = [f for f in listdir("./") if f[0]+f[1]+f[2]+f[3] == "run_" and f[-1] == "s"][0]
all_exp = listdir(f"{exp_dir}/configs/")
for i, exp in enumerate(all_exp):
    print(f"[{'='*(int((i+1)/len(all_exp))*30)}{' '*(30-int((i+1)/len(all_exp))*30)}] {i+1}/{len(all_exp)}")
    system(f"python run_experiment.py ./{exp_dir}/configs/{exp}")
    