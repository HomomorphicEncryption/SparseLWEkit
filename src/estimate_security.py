from multiprocessing import cpu_count
import pandas as pd
import time
import platform
import subprocess

from lattice_estimator.estimator import *
from sage.all import oo, log


def estimate_security(toolname, logn, sigma, logq, h, num_cores=1):
    if toolname == 'lattice_estimator':
        return estimate_security_lattice_estimator(logn, sigma, logq, h, num_cores=num_cores)
    else:
        raise ValueError(f"Unknown tool: {toolname}. Supported estimation tools: {toolnames}")
    
def estimate_security_lattice_estimator(logn, sigma, logq, h, m=oo, num_cores=1):  
    params = LWE.Parameters(n=2**logn, q=2**logq, Xe=ND.DiscreteGaussian(sigma), Xs=ND.SparseTernary(p=h // 2, m= h // 2, n=2 ** logn), m=m)
    print(f"estimating security for logn={logn}, sigma={sigma}, logq={logq}, h={h}...")
    start = time.perf_counter()
    full_estimates = LWE.estimate(params, deny_list=["arora-gb", "bkw"], quiet=True, jobs=num_cores)
    
    # only keep the exponent part of rop, to 1dp
    estimates = {k: round(float(log(v["rop"], 2)), 1) for k, v in full_estimates.items()}

    end = time.perf_counter()
    elapsed_time = end - start
    seconds = int(elapsed_time)
    hours, rem = divmod(seconds, 3600)
    minutes, seconds = divmod(rem, 60)

    estimates_and_time = estimates | {"estimation_time": f"{hours}h {minutes}m {seconds}s"}
    return estimates_and_time


if __name__ == "__main__":
    toolnames = ['lattice_estimator']
    parameters_db = pd.read_csv('src/data/parameter_db.csv')

    # default to using half of the available cores
    num_cores = cpu_count() // 2
    # a string which specifies the machine used to generate estimates
    machine_info = f"{platform.system()} {platform.release()},{platform.machine()},{num_cores} cores"

    for toolname in toolnames:
        tool_estimates = parameters_db.apply(lambda row: pd.Series(estimate_security(toolname, row[r"$\log_2(n)$"], row['σ'], row[r"$\log_2(q)$"], row[r"$h$"], num_cores=num_cores)), axis=1)

        tool_estimates = parameters_db.join(tool_estimates).drop(columns=['Origin'])

        # pull the commit of the tool
        tool_commit = subprocess.check_output(["git", "-C", f"src/{toolname}", "rev-parse", "--short", "HEAD"]).decode("utf-8").strip()

        # add machine info and tool commit to the estimates
        tool_estimates["machine_info"] = machine_info
        tool_estimates["tool_commit"] = tool_commit

        tool_estimates.to_csv(f"src/data/{toolname}_estimates.csv", index=False)
        # print(tool_estimates.to_markdown(index=False))


    




