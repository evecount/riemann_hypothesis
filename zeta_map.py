import numpy as np
import matplotlib.pyplot as plt
from scipy.special import zeta

def plot_critical_line(start_t=0, end_t=50, points=1000):
    """
    Visualizes the Zeta function along the Critical Line Re(s) = 1/2.
    The zeros of this function are the foundation of the Riemann Hypothesis.
    """
    t = np.linspace(start_t, end_t, points)
    s = 0.5 + 1j * t
    z = [zeta(complex_s) for complex_s in s]
    
    abs_z = [abs(val) for val in z]
    
    plt.figure(figsize=(12, 6))
    plt.plot(t, abs_z, color='#00ffa3', label='|ζ(1/2 + it)|')
    plt.axhline(0, color='red', linestyle='--', alpha=0.5)
    plt.title('Zeta Function Magnitude on the Critical Line')
    plt.xlabel('t (Imaginary Part)')
    plt.ylabel('|ζ(s)|')
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    # Save the plot as a manifestation artifact
    plt.savefig('ZETA_MAGNITUDE_CRITICAL_LINE.png')
    print("Manifestation complete: ZETA_MAGNITUDE_CRITICAL_LINE.png")

if __name__ == "__main__":
    try:
        plot_critical_line()
    except Exception as e:
        print(f"Entropy Encountered: {e}")
