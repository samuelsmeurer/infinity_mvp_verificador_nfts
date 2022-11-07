from polygonscan import PolygonScan

with PolygonScan("WDDZGYYWAGAC446V2JHQT93NW4F1TX6P9Q",False) as matic:
    save = (matic.get_contract_abi("0xa661E867871E4D6479504c6ED296bEEbe6CAfF6d"))
print(save)