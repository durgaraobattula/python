def revenue_after_three_years(revenue):
 
 increase_per_year = revenue * 8.9 / 100

 total_revenue_after_three_years = revenue + 3 * increase_per_year

 return total_revenue_after_three_years

initial_revenue = 100

revenue_after_three_years = revenue_after_three_years(initial_revenue)

print(f"Revenue after 3 years: {revenue_after_three_years:.2f} crores")