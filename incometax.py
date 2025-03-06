# Input total yearly income
total_income_input = input("Enter total yearly income: ")
total_income = float(total_income_input.replace(',', ''))

# Calculate the minimum taxable deduction based on new rule
tax_free_option1 = total_income / 3
tax_free_option2 = 450000
tax_free_allowance = min(tax_free_option1, tax_free_option2)

# Calculate the new taxable income
taxable_income = max(total_income - tax_free_allowance, 0)

# Define tax slabs and rates
slabs = [
    (350000, 0.00),    # 0% for first 350,000
    (100000, 0.05),    # 5% for next 100,000
    (400000, 0.10),    # 10% for next 400,000
    (500000, 0.15),    # 15% for next 500,000
    (None, 0.20)       # 20% for remaining amount
]

remaining_income = taxable_income
total_tax = 0.0

# Calculate tax for each slab
for slab_amount, slab_rate in slabs:
    if remaining_income <= 0:
        break
    if slab_amount is not None:
        income_in_slab = min(remaining_income, slab_amount)
    else:
        income_in_slab = remaining_income  # remaining balance
    total_tax += income_in_slab * slab_rate
    remaining_income -= income_in_slab

# Print formatted result
print(f"\nTotal Yearly Income: {total_income:,.2f}")
print(f"Tax-Free Allowance: {tax_free_allowance:,.2f}")
print(f"Taxable Income: {taxable_income:,.2f}")
print(f"Total Tax Payable: {total_tax:,.2f}")