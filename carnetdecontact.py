carnet={"Alice":{"numéro":"01-01-03-04-05"},"Bob":{"06-07-08-09-10"},"Cédric":{"01-11-12-13-14"}}
print(carnet["Alice"])
carnet["Georges"]=67485587
print(carnet)
carnet.pop("Cédric")
print(carnet)
