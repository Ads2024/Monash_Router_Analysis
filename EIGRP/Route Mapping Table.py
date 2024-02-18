import pandas as pd

# Data for the table
data = [
    {"Route": "R1 -> R2", "Intermediate Stops": "None"},
    {"Route": "R1 -> R3", "Intermediate Stops": "None"},
    {"Route": "R1 -> R4", "Intermediate Stops": "None"},
    {"Route": "R1 -> R2", "Intermediate Stops": "Via R4"},
    {"Route": "R1 -> R2", "Intermediate Stops": "Via R3"},
    {"Route": "R1 -> R3", "Intermediate Stops": "Via R2"},
    {"Route": "R1 -> R3", "Intermediate Stops": "Via R4 and R2"},
    {"Route": "R1 -> R4", "Intermediate Stops": "Via R2"},
    {"Route": "R1 -> R4", "Intermediate Stops": "Via R3 and R2"},
    {"Route": "R2 -> R1", "Intermediate Stops": "None"},
    {"Route": "R2 -> R3", "Intermediate Stops": "None"},
    {"Route": "R2 -> R4", "Intermediate Stops": "None"},
    {"Route": "R2 -> R1", "Intermediate Stops": "Via R4"},
    {"Route": "R2 -> R1", "Intermediate Stops": "Via R3"},
    {"Route": "R2 -> R3", "Intermediate Stops": "Via R4 and R1"},
    {"Route": "R2 -> R4", "Intermediate Stops": "Via R3 and R1"},
    {"Route": "R2 -> R3", "Intermediate Stops": "Via R1"},
    {"Route": "R2 -> R4", "Intermediate Stops": "Via R1"},
    {"Route": "R3 -> R1", "Intermediate Stops": "None"},
    {"Route": "R3 -> R2", "Intermediate Stops": "None"},
    {"Route": "R3 -> R1", "Intermediate Stops": "Via R2"},
    {"Route": "R3 -> R2", "Intermediate Stops": "Via R1"},
    {"Route": "R3 -> R1", "Intermediate Stops": "Via R2 & R4"},
    {"Route": "R3 -> R2", "Intermediate Stops": "Via R1 & R4"},
    {"Route": "R3 -> R4", "Intermediate Stops": "Via R2"},
    {"Route": "R3 -> R4", "Intermediate Stops": "Via R1"},
    {"Route": "R3 -> R4", "Intermediate Stops": "Via R2 & R1"},
    {"Route": "R3 -> R4", "Intermediate Stops": "Via R1 & R2"},
    {"Route": "R4 -> R1", "Intermediate Stops": "None"},
    {"Route": "R4 -> R2", "Intermediate Stops": "None"},
    {"Route": "R4 -> R1", "Intermediate Stops": "Via R2"},
    {"Route": "R4 -> R2", "Intermediate Stops": "Via R1"},
    {"Route": "R4 -> R1", "Intermediate Stops": "Via R2&R3"},
    {"Route": "R4 -> R2", "Intermediate Stops": "Via R1 & R3"},
    {"Route": "R4 -> R3", "Intermediate Stops": "Via R2"},
    {"Route": "R4 -> R3", "Intermediate Stops": "Via R1"},
    {"Route": "R4 -> R3", "Intermediate Stops": "Via R2 & R1"},
    {"Route": "R4 -> R3", "Intermediate Stops": "Via R1 & R2"}
]

# Create a DataFrame
df = pd.DataFrame(data)

# Display the table
print(df)
