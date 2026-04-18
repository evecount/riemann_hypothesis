import React, { useMemo } from 'react';
import { motion } from 'framer-motion';

/**
 * RIEMANN SOVEREIGN ENGINE
 * A symbolic visualization of the Critical Line and the first 10 Zeta Zeros.
 * Used as a Logic Beacon for the Sovereign Neural Interface.
 */
export const RiemannSovereignEngine = () => {
    // Symbolic representation of the First 10 Zeta Zeros
    const zeros = [14.134, 21.022, 25.010, 30.424, 32.935, 37.586, 40.918, 43.327, 48.005, 49.773];
    
    return (
        <div style={{ padding: '40px', background: '#0a0a0a', height: '100%', color: '#f0f0f0', borderRadius: '12px', overflow: 'hidden' }}>
            <h1 style={{ fontSize: '2.5rem', marginBottom: '24px', letterSpacing: '-0.05em' }}>
                THE CRITICAL LINE <span style={{ color: '#ff2d55' }}>[Re(s) = 1/2]</span>
            </h1>
            <div style={{ position: 'relative', height: '400px', borderLeft: '2px solid #333', marginLeft: '100px' }}>
                <div style={{ position: 'absolute', left: '-60px', top: '50%', transform: 'translateY(-50%)', fontWeight: 800 }}>
                    1/2
                </div>
                {/* Visualizing the Zeros as Sovereign Beacons */}
                {zeros.map((z, i) => (
                    <motion.div 
                        key={i}
                        initial={{ opacity: 0, scale: 0 }}
                        animate={{ opacity: 1, scale: 1 }}
                        transition={{ delay: i * 0.1 }}
                        style={{ 
                            position: 'absolute', 
                            left: '0', 
                            top: `${(z / 60) * 100}%`,
                            width: '12px',
                            height: '12px',
                            background: '#00ffa3',
                            borderRadius: '50%',
                            boxShadow: '0 0 15px #00ffa3',
                            transform: 'translateX(-50%)'
                        }}
                    />
                ))}
            </div>
            <p style={{ marginTop: '40px', color: '#888', maxWidth: '600px' }}>
                Architecture: All non-trivial zeros are aligned. The Flightpath is valid. 
                Sovereignty is the ability to maintain balance on the 1/2 axis.
            </p>
        </div>
    );
};
