import numpy as np
import matplotlib.pyplot as plt
from scipy.special import zeta
import os

def plot_critical_line(start_t=0, end_t=50, points=1000):
    """
    Utility to visualize the magnitude of the Riemann Zeta function along the 
    Critical Line (Re(s) = 0.5). This serves as a secondary verification for the 
    Zero-Axial resonance nodes used in the CISM Inward Sighting Method.
    
    Args:
        start_t (int): Starting imaginary height.
        end_t (int): Ending imaginary height.
        points (int): Number of resolution points for the plot.
    """
    t = np.linspace(start_t, end_t, points)
    s = 0.5 + 1j * t
    z = [zeta(complex_s) for complex_s in s]
    
    abs_z = [abs(val) for val in z]
    
    plt.figure(figsize=(12, 6), facecolor='#0a0a0a')
    ax = plt.gca()
    ax.set_facecolor('#0a0a0a')
    
    plt.plot(t, abs_z, color='#00ffa3', linewidth=1.5, label='|ζ(1/2 + it)|')
    plt.axhline(0, color='#ff2d55', linestyle='--', alpha=0.5, label='Zero Horizon')
    
    # Standard Academic Styling
    plt.title('Zeta Magnitude: Resonance on the Critical Line', color='#f0f0f0', fontsize=14)
    plt.xlabel('Imaginary Height (t)', color='#f0f0f0')
    plt.ylabel('Magnitude |ζ(s)|', color='#f0f0f0')
    ax.tick_params(colors='#f0f0f0')
    plt.grid(True, alpha=0.1)
    plt.legend()
    
    # Save to Assets for README inclusion
    output_path = os.path.join('assets', 'zeta_magnitude_line.png')
    plt.savefig(output_path, dpi=300)
    print(f"[SUCCESS] Zeta visualization generated at: {output_path}")

if __name__ == "__main__":
    try:
        # Create assets dir if it doesn't exist
        if not os.path.exists('assets'):
            os.makedirs('assets')
            
        plot_critical_line()
    except Exception as e:
        print(f"[ERROR] Visualization pipeline failed: {e}")
