from email.headerregistry import Address
from operator import le
from polygonscan import PolygonScan

with PolygonScan("WDDZGYYWAGAC446V2JHQT93NW4F1TX6P9Q",False) as matic:
    save = (matic.get_acc_balance_by_token_and_contract_address("0x2977F845d2793461f58C0dc54eBD753076C5AD06","0x2471a2eb689cb37b24bba6d1d11d8b1ed5b4bdc6"))
print(save)





