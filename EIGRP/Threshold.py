
propagation_delay_via_R2 = 220 * 10**-6  # seconds
propagation_delay_direct = 100 * 10**-6  # seconds
bandwidth_via_R2_bps = 1_000_000 * 1_000  # bits per second
bandwidth_direct_bps = 100_000 * 1_000  # bits per second

# Equate total delays and solve for L
# D_total_via_R2 = propagation_delay_via_R2 + L / bandwidth_via_R2_bps
# D_total_direct = propagation_delay_direct + L / bandwidth_direct_bps
# Set them equal and solve for L
L_threshold = (propagation_delay_via_R2 - propagation_delay_direct) / (1/bandwidth_direct_bps - 1/bandwidth_via_R2_bps)

print(L_threshold)
