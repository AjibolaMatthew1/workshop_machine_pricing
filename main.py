import streamlit as st

# Define the coefficients for different machines (example coefficients for lathe machine)
coefficients = {
    'Lathe Machine': {
        'Initial Cost': 0.0004056891810690172,
        'Space Occupied': 1.609495360944793,
        'Power Rating': 0.04697320976320274,
        'Time Spent': 424.90621134259817,
        'Workpieces': -29.41797076859265,
        'Operators': -55.66171992476241,
        'Ventilation Cost': 0.006782578466305367,
        'Cleaning Cost': 0.2553865093524714,
        'Waste Management Cost': -0.24896513218323035,
        'Toilet Usage Cost': 0.04003480507607149
    },
    'Milling Machine': {
        'Initial Cost': 0.000230,
        'Space Occupied': 1.300,
        'Power Rating': -0.0250,
        'Time Spent': 400.0,
        'Workpieces': 0.280,
        'Operators': -85.0,
        'Ventilation Cost': -0.160,
        'Cleaning Cost': 1.2,
        'Waste Management Cost': -1.5,
        'Toilet Usage Cost': -0.009
    },
    # Add coefficients for more machines here
}

# Function to calculate the price based on selected machine and input values
def calculate_price(machine, data):
    price = sum(coefficients[machine][key] * data[key] for key in coefficients[machine])
    return price

# Define the Streamlit interface
st.title("Workshop Machine Price Calculator")
st.write("A simple calculator to determine the price based on machine usage.")

# Dropdown for selecting the machine type
machine = st.selectbox("Select Machine Type", ['Lathe Machine', 'Milling Machine', 'Grounding Machine', 'Drilling Machine'])  # Add more machines as needed

# Display the formula for the selected machine
# st.write(f"### Formula for {machine}:")
# st.latex(rf"p_i = (\alpha \cdot \text{{Initial Cost}}) + (\beta \cdot \text{{Space Occupied}}) + "
#          r"(\gamma \cdot \text{{Power Rating}}) + (\delta \cdot \text{{Time Spent}}) + "
#          r"(\epsilon \cdot \text{{Workpieces}}) + (\phi \cdot \text{{Operators}}) + "
#          r"(\psi \cdot \text{{Ventilation Cost}}) + (\omega \cdot \text{{Cleaning Cost}}) + "
#          r"(\sigma \cdot \text{{Waste Management Cost}}) + (\lambda \cdot \text{{Toilet Usage Cost}})")

# User inputs for the variable values
initial_cost = st.number_input("Initial Cost (₦)", min_value=1000000, step=100000)
area_occupied = st.number_input("Area Occupied (m²)", min_value=50.0, max_value=500.0, step=1.0)
power_rating = st.number_input("Power Rating (Watts)", min_value=10000, max_value=30000, step=500)
time_spent = st.number_input("Time Spent (minutes)", min_value=60, max_value=720, step=10)
workpieces = st.number_input("Workpieces (units)", min_value=1, max_value=100, step=1)
operators = st.number_input("Operators (persons)", min_value=1, max_value=10, step=1)
ventilation_cost = st.number_input("Ventilation Cost (₦)", min_value=1000, max_value=20000, step=500)
cleaning_cost = st.number_input("Cleaning Cost (₦)", min_value=1000, max_value=20000, step=500)
waste_management_cost = st.number_input("Waste Management Cost (₦)", min_value=1000, max_value=20000, step=500)
toilet_usage_cost = st.number_input("Toilet Usage Cost (₦)", min_value=1000, max_value=10000, step=500)

# Input data for calculation
data = {
    'Initial Cost': initial_cost,
    'Space Occupied': area_occupied,
    'Power Rating': power_rating,
    'Time Spent': time_spent,
    'Workpieces': workpieces,
    'Operators': operators,
    'Ventilation Cost': ventilation_cost,
    'Cleaning Cost': cleaning_cost,
    'Waste Management Cost': waste_management_cost,
    'Toilet Usage Cost': toilet_usage_cost
}

# Calculate and display the price
if st.button("Calculate Price"):
    price = calculate_price(machine, data)
    st.success(f"The calculated price for {machine} is: ₦{price:,.2f}")
