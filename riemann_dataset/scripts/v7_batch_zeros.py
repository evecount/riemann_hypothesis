#!/usr/bin/env python3
"""
Batch 1/4: Compute 10,000 zeros in chunks of 1000, save after each chunk.
Uses unbuffered output (flush=True) for real-time progress.
"""
import sys
import numpy as np
from mpmath import mp, re, im, fabs, zeta, zetazero, diff, mpc, power
import csv, time, os, json

mp.dps = 18
OUT_DIR = "/data/.openclaw/workspace/research/riemann-hypothesis/v7_data"
os.makedirs(OUT_DIR, exist_ok=True)

N_ZEROS = 10000
CHUNK = 1000

# Arrays
zeros_beta = []
zeros_gamma = []
zp_re_arr = []
zp_im_arr = []
zp_abs_arr = []

print(f"Computing {N_ZEROS} Riemann zeros in chunks of {CHUNK}...", flush=True)
total_t0 = time.time()

for chunk_start in range(0, N_ZEROS, CHUNK):
    chunk_end = min(chunk_start + CHUNK, N_ZEROS)
    chunk_num = chunk_start // CHUNK + 1
    t0 = time.time()
    print(f"\n--- Chunk {chunk_num}/10: zeros {chunk_start+1}-{chunk_end} ---", flush=True)
    
    for n in range(chunk_start + 1, chunk_end + 1):
        rho = zetazero(n)
        zp = diff(zeta, rho)
        zeros_beta.append(float(re(rho)))
        zeros_gamma.append(float(im(rho)))
        zp_re_arr.append(float(re(zp)))
        zp_im_arr.append(float(im(zp)))
        zp_abs_arr.append(float(fabs(zp)))
        
        if n % 200 == 0:
            elapsed = time.time() - t0
            print(f"  {n}/{chunk_end} ({elapsed:.0f}s) γ_{n} = {zeros_gamma[-1]:.2f}", flush=True)
    
    chunk_time = time.time() - t0
    print(f"  Chunk {chunk_num} done in {chunk_time:.1f}s. Total zeros: {len(zeros_gamma)}", flush=True)
    
    # Save checkpoint after each chunk
    checkpoint_file = f"{OUT_DIR}/zeros_checkpoint_{chunk_end}.csv"
    with open(checkpoint_file, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["n", "beta", "gamma", "Re_zeta_prime", "Im_zeta_prime", "abs_zeta_prime"])
        for i in range(len(zeros_gamma)):
            w.writerow([i+1, zeros_beta[i], zeros_gamma[i], zp_re_arr[i], zp_im_arr[i], zp_abs_arr[i]])
    print(f"  Checkpoint saved: {checkpoint_file}", flush=True)

total_time = time.time() - total_t0
print(f"\n=== ALL {N_ZEROS} ZEROS COMPUTED in {total_time:.0f}s ({total_time/60:.1f} min) ===", flush=True)

# Save final complete file
final_file = f"{OUT_DIR}/zeros_10000.csv"
with open(final_file, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["n", "beta", "gamma", "Re_zeta_prime", "Im_zeta_prime", "abs_zeta_prime"])
    for i in range(N_ZEROS):
        w.writerow([i+1, zeros_beta[i], zeros_gamma[i], zp_re_arr[i], zp_im_arr[i], zp_abs_arr[i]])

# Save as numpy for fast loading by analysis scripts
np.savez_compressed(f"{OUT_DIR}/zeros_10000.npz",
    beta=np.array(zeros_beta),
    gamma=np.array(zeros_gamma),
    zp_re=np.array(zp_re_arr),
    zp_im=np.array(zp_im_arr),
    zp_abs=np.array(zp_abs_arr))

print(f"Final data saved: {final_file}", flush=True)
print(f"γ range: [{zeros_gamma[0]:.4f}, {zeros_gamma[-1]:.4f}]", flush=True)
