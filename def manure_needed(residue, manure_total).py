def manure_needed(residue, manure_total):
 manure_from_residue = residue * 0.3  
 extra_manure_needed = manure_total - manure_from_residue
 return round(extra_manure_needed, 2)
residue = 500
manure_total = 1500
extra_manure = manure_needed(residue, manure_total)
print(f"Extra manure needed: {extra_manure} kg")