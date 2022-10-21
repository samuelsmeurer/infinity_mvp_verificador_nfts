from email.headerregistry import Address
from operator import le
from polygonscan import PolygonScan
'''
with PolygonScan("WDDZGYYWAGAC446V2JHQT93NW4F1TX6P9Q",False) as matic:
    print(matic.get_matic_balance(address="0xc340f3e886052D5091bdA667562AeAA1e1199766"))'''
'''
with PolygonScan("WDDZGYYWAGAC446V2JHQT93NW4F1TX6P9Q",False) as matic:
    print(matic.get_contract_abi("0x9928A8ea82d86290DfD1920E126B3872890525b3"))'''
vetor_to = list
with PolygonScan("WDDZGYYWAGAC446V2JHQT93NW4F1TX6P9Q",False) as matic:
    save = (matic.get_erc721_token_transfer_events_by_contract_address_paginated("0x9928A8ea82d86290DfD1920E126B3872890525b3",1,10000,"asc"))
    i =0
    vetor_to = []
    for  i in range(len(save)):
        a = dict(save[i])
        b = a.get("to")
        vetor_to.append(b)
        print(vetor_to)


'''
    a = dict(save[2])
    b = a.get("to")
    samuel =[]
    samuel.append(b)
    print(samuel)'''