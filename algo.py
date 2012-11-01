from algo_electrum import AlgoElectrum
from algo_bip32 import AlgoBIP32
from bitkey_proto import bitkey_pb2 as proto

def AlgoFactory(p):
    if p == proto.ELECTRUM:
        return AlgoElectrum
    elif p == proto.BIP32:
        return AlgoBIP32
    
    raise NotImplemented