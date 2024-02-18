import pandas as pd
import openpyxl
# Calculate EIGRP metric
def calculate_eigrp_metric(bandwidth_kbps, delay_us):
    return 256 * ((10**7 // bandwidth_kbps) + (delay_us // 10))

# Direct and indirect routes definition (to be filled with actual data)
direct_routes = {
    'R2-R1': {'bandwidth': 1000, 'delay': 110},
    'R3-R1': {'bandwidth': 100, 'delay': 100},
    'R4-R1': {'bandwidth': 100, 'delay': 100},
    'R4-R2': {'bandwidth': 1000, 'delay': 110},
    'R3-R2': {'bandwidth': 1000, 'delay': 110}   # Format: 'Source-Destination': {'bandwidth': <in Mbps>, 'delay': <in us>}
}

indirect_routes = {
    'R4-R1_via_R2':[('R4-R2','R2-R1')],
    'R4-R2_via_R1':[('R4-R1','R2-R1')],
    'R4-R1_via_R2&R3':[('R4-R2','R3-R2','R3-R1')],
    'R4-R2_via_R1&R3':[('R4-R1','R3-R1','R3-R2')],
    'R4-R3_via_R2':[('R4-R2','R3-R2')],
    'R4-R3_via_R1':[('R4-R1','R3-R1')],
    'R4-R3_via_R2&R1':[('R4-R2','R2-R1','R3-R1')],
    'R4-R3_via_R1&R2':[('R4-R1','R2-R1','R3-R2')]# Format: 'Source-Destination_via_<via>': [('Source-Intermediate', 'Intermediate-Destination')]
}

# Calculate metrics for direct routes
eigrp_metrics_direct = {
    route: calculate_eigrp_metric(details['bandwidth'] * 1000, details['delay'])
    for route, details in direct_routes.items()
}

# Calculate metrics for indirect routes
eigrp_metrics_indirect = {}
for route, paths in indirect_routes.items():
    for path in paths:
        # Calculate minimum bandwidth and total delay for each segment in the indirect path
        min_bandwidth = min(direct_routes[segment]['bandwidth'] for segment in path) * 1000  # Corrected to use all segments in the path
        total_delay = sum(direct_routes[segment]['delay'] for segment in path)  # Corrected to use all segments in the path
        eigrp_metrics_indirect[route] = calculate_eigrp_metric(min_bandwidth, total_delay)


# Combine direct and indirect metrics
all_routes = {**eigrp_metrics_direct, **eigrp_metrics_indirect}

# Determine optimal paths
optimal_paths = {}
for route in direct_routes.keys():
    possible_routes = [r for r in all_routes.keys() if route in r]
    optimal_route = min(possible_routes, key=lambda x: all_routes[x])
    optimal_paths[route] = optimal_route

# Prepare data for table display
table_data = []
for route, metric in all_routes.items():
    source, destination = route.split('-')[:2]
    if route in direct_routes:  # Handle direct routes
        bandwidth = direct_routes[route]['bandwidth'] * 1000  # Convert Mbps to Kbps
        delay = direct_routes[route]['delay']
    else:  # Handle indirect routes
        path = indirect_routes[route][0]  # Assuming there's only one path per indirect route for simplicity
        min_bandwidth = min(direct_routes[segment]['bandwidth'] for segment in path) * 1000
        total_delay = sum(direct_routes[segment]['delay'] for segment in path)
        bandwidth = min_bandwidth
        delay = total_delay
    optimal = (route == optimal_paths.get(f'{source}-{destination}'))
    table_data.append([source, destination, bandwidth, delay, metric, optimal])


# Create DataFrame for table display
df = pd.DataFrame(table_data, columns=["Source Router", "Destination Router", "Bandwidth (Kbps)", "Delay (us)", "EIGRP Metric", "Optimal Path"])
df['Optimal Path'] = df['Optimal Path'].map({True: 'Yes', False: 'No'})

# Display the table
# Specify the filename of your existing Excel file
filename = r'C:\Users\User\Documents\Optimal Paths.xlsx'

# Load the Excel file
with pd.ExcelWriter(filename, mode='a', engine='openpyxl') as writer:  
    # Write your DataFrame to a new sheet in the Excel file
    df.to_excel(writer, sheet_name='R4')
