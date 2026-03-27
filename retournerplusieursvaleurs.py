def stats(notes):
 moyenne = sum(notes) / len(notes)
 minimale = min(notes)
 maximale = max(notes)
 return moyenne, minimale, maximale
ma_moyenne, mon_min, mon_max = stats([12, 8, 15, 10, 18])
print(f"Moyenne : {ma_moyenne}")
print(f"Min : {mon_min}   Max : {mon_max}")