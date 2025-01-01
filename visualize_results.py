import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd

ALGS = ["RDUCB","RDPI","RDEI"]
REP = [0,1,2,3,4] # implicit
FUNC = [1,8,12,15,21]
IDS = [0,1,2]
DIMS = [2,10,40,100]

for curfunc in FUNC:

    fig, axes = plt.subplots(nrows=3, ncols=4, figsize=(15, 10))

    path = './results/'
    all_runs = os.listdir(path)


    def readFile(_path):
        df = pd.read_csv(f"./{_path}",skiprows=1,sep=" ")
        
        with open(f"./{_path}") as f:
            line = f.readline().split('" "')
            a,b = line[-1].split('" ')
            line[0] = line[0].split('"')[-1]
            line[-1] = a
            line.extend(b.split())
            df.columns = line
        
        return df['function evaluation'], df['best-so-far f(x)']


    for i, ids in enumerate(IDS):  # Rows: dimensions
        for j, dim in enumerate(DIMS):  # Columns: instances
            ax = axes[i, j]
            ax.set_title(f"{dim}D, iid: {ids}", fontsize=10)
            ax.grid(True)
            
            
            for k, alg in enumerate(ALGS): # 3rd: algorithms

                runs = [f for f in all_runs if all([att in f for att in [f"_Dim-{dim}_", f"_Id-{ids}_", f"Opt-{alg}_",f"_F-{curfunc}_"]])]
                
                X,y = [], []
                for run in runs:
                    
                    dirls = "/"+[f for f in os.listdir(path+run) if "." not in f][0]
                    datls = "/"+os.listdir(path+run+dirls)[0]
                    
                    _X, _y = readFile(path+run+dirls+datls)
                    X.append(_X)
                    y.append(_y)
                    
                X = np.array(X).mean(axis=0)
                y = np.array(y)
                y_mu = np.mean(y,axis=0)
                y_std = np.std(y,axis=0)
                
                try: # Could fail for some reason?
                    ax.plot(X, y_mu, label=f"{alg}")
                    print(alg,X,y_mu)
                    ax.fill_between(X, y_mu-y_std, y_mu+y_std,alpha=0.2)
                except:
                    pass
            
            ax.legend(fontsize=8)
            ax.set_xlabel("Number of iterations")
            ax.set_ylabel("Best found $f(x)$")
    fig.suptitle(f"Assessment on function F-{curfunc} in various dimensionalities and instances", fontsize=12)
    
    plt.tight_layout()
    plt.savefig(f"./results/{curfunc}.png")