import numpy as np
import pandas as pd
import time

def high_limit_audit(limit=100000):
    print(f"--- [RIEMANN TOPOLOGICAL AUDIT] Target: n={limit} ---")
    
    # Load ground truth primes
    primes_path = r'c:\Users\User\Documents\riemann\riemann_dataset\prime_number.csv'
    primes_df = pd.read_csv(primes_path)
    true_primes = set(primes_df['prime'].values[primes_df['prime'].values <= limit])
    print(f"[DATA] Loaded {len(true_primes)} primes for validation.")

    phi = (np.sqrt(5) - 1) / 2
    kepler_density = np.pi / (3 * np.sqrt(2)) # ~0.74048
    
    results = []
    
    start_time = time.time()
    
    for n in range(2, limit + 1):
        # 1. FRACTIONAL PHASING METHOD (Notebook Style)
        phasing_void = (n * phi) % 1.0
        conic_vol = 1 / np.log(n)
        error_phasing = np.abs(phasing_void - conic_vol)
        
        # 2. KEPLER VOLUME METHOD (CISM Engine Style)
        void_vol_k = (1 - kepler_density) * (n**2)
        r_inward = n / np.log(n)
        h = n * phi
        cone_vol_k = (1/3) * np.pi * (r_inward**2) * h
        error_kepler = np.abs(void_vol_k * n - cone_vol_k) / (n**3)
        
        # 3. RESONANCE FILTER METHOD (Signal Processing Style)
        resonance_score = np.abs(np.sin(np.pi * (phasing_void - conic_vol)))
        
        is_prime = n in true_primes
        results.append({
            'n': n,
            'error_phasing': error_phasing,
            'error_kepler': error_kepler,
            'resonance_score': resonance_score,
            'is_prime': is_prime
        })
        
        if n % 10000 == 0:
            print(f"[PROGRESS] n={n} processed.")

    df = pd.DataFrame(results)
    
    # Analyze Accuracy at Primes
    prime_stats = df[df['is_prime'] == True]
    non_prime_stats = df[df['is_prime'] == False]
    
    print("\n--- [AUDIT RESULTS] ---")
    print(f"PHASING METHOD - Avg Error (Primes): {prime_stats['error_phasing'].mean():.6f}")
    print(f"PHASING METHOD - Avg Error (Non-Primes): {non_prime_stats['error_phasing'].mean():.6f}")
    
    print(f"\nKEPLER METHOD - Avg Error (Primes): {prime_stats['error_kepler'].mean():.6f}")
    print(f"KEPLER METHOD - Avg Error (Non-Primes): {non_prime_stats['error_kepler'].mean():.6f}")
    
    print(f"\nRESONANCE FILTER - Avg Score (Primes): {prime_stats['resonance_score'].mean():.6f}")
    print(f"RESONANCE FILTER - Avg Score (Non-Primes): {non_prime_stats['resonance_score'].mean():.6f}")
    
    # Calculate Separation Score (Difference in means)
    print(f"\n[METRIC] Phasing Separation: {non_prime_stats['error_phasing'].mean() - prime_stats['error_phasing'].mean():.6f}")
    print(f"[METRIC] Kepler Separation: {non_prime_stats['error_kepler'].mean() - prime_stats['error_kepler'].mean():.6f}")
    print(f"[METRIC] Resonance Separation: {non_prime_stats['resonance_score'].mean() - prime_stats['resonance_score'].mean():.6f}")
    
    duration = time.time() - start_time
    print(f"\n[SUCCESS] Audit completed in {duration:.2f}s")
    
    return df

if __name__ == "__main__":
    df_results = high_limit_audit(100000)
    df_results.to_csv(r'c:\Users\User\Documents\riemann\scratch\audit_results_100k.csv', index=False)
