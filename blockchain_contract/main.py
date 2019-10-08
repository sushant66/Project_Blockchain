import streams

# Ethereum modules
from blockchain.ethereum import rpc

from blockchain.ethereum import ethereum
# WiFi drivers
from espressif.esp32net import esp32wifi as net_driver # for ESP-32
# from broadcom.bcm43362 import bcm43362 as net_driver # for Particle Photon
from wireless import wifi

# SSL module for https
import ssl

# Configuration file
import config


# The SSL context is needed to validate https certificates
SSL_CTX = ssl.create_ssl_context(
    cacert=config.CA_CERT,
    options=ssl.CERT_REQUIRED|ssl.SERVER_AUTH
)

# Use serial monitor
streams.serial()
pinMode(D18, INPUT_PULLUP)
pinMode(D19, INPUT_PULLUP)

def init_wifi():
    # Connect to WiFi network
    net_driver.auto_init()
    print("Connecting to wifi")
    wifi.link(config.WIFI_SSID, wifi.WIFI_WPA2, config.WIFI_PASSWORD)
    print("Connected!")


def send_bet():
    nt = eth.getTransactionCount(config.ADDRESS)
    tx = ethereum.Transaction()
    #tx.set_value(0, ethereum.WEI)
    tx.set_gas_price(config.GAS_PRICE)
    tx.set_gas_limit("0x33450")
    tx.set_nonce(nt)
    #tx.set_receiver(config.CONTRACT_ADDRESS)
    tx.set_chain(ethereum.ROPSTEN)
    tx.sign(config.PRIVATE_KEY)
    tx_hash = eth.sendTransaction(tx.to_rlp(True))
    return tx_hash


def print_balance():
    # Get our current balance from the net
    balance = eth.getBalance(config.ADDRESS)
    print("Current balance: ", int(balance,0))
    if not balance:
        print(eth.last_error)
        raise Exception


# Main
#try:
    
    # Run the game
    #print('Data a: %d' %x)
    #print('Data b: %d' %y)
    #print('Betting %s Wei...' % config.BET_AMOUNT)
    """
    nonce = eth.getTransactionCount(config.ADDRESS)
    print(nonce)
    tx_hash = game.tx('set', nonce, value=(0,ethereum.WEI), args=((1),(1)))
    print(tx_hash)
    #print('Your bet has been placed, and the transaction is now being mined.')
    print('Monitor your balance at https://ropsten.etherscan.io/address/%s#internaltx to see if you won!' % config.ADDRESS)
    #print('Reset your device to play again.')
    """
#except Exception as e:
#    print(e)
init_wifi()
# Init the RPC node
eth = rpc.RPC(config.RPC_URL, ssl_ctx=SSL_CTX)

# Init smart contract object
game = ethereum.Contract(
    eth,
    config.CONTRACT_ADDRESS,
    config.PRIVATE_KEY,
    config.ADDRESS,
    chain=ethereum.ROPSTEN
)
for name in config.CONTRACT_METHODS:
    method = config.CONTRACT_METHODS[name]
    game.register_function(
        name,
        config.GAS_PRICE,
        method["gas_limit"],
        args_type=method["args"]
    )
print_balance()

"""

jackpot = game.call('get', rv=(256, str))
x  = int(jackpot, 0)
print('Current jackpot: %d' % x)
#print('Betting %s Wei...' % config.BET_AMOUNT)
nonce = eth.getTransactionCount(config.ADDRESS)
tx_hash = game.tx('set', nonce) #value=(0, ethereum.WEI))
print(tx_hash)
print('Your bet has been placed, and the transaction is now being mined.')
print('Monitor your balance at https://ropsten.etherscan.io/address/%s#internaltx to see if you won!' % config.ADDRESS)
print('Reset your device to play again.')

"""
while True:
    read1 = digitalRead(D18)
    if (read1 == 1):
        nonce = eth.getTransactionCount(config.ADDRESS)
        tx_hash = game.tx('get', nonce) #value=(0, ethereum.WEI))
        print("Candidate 1: ",tx_hash)
        sleep(3000)
    read2 = digitalRead(D19)
    if (read2 == 1):
        nonce = eth.getTransactionCount(config.ADDRESS)
        tx_hash2 = game.tx('get2', nonce) #value=(0, ethereum.WEI))
        print("Candidate 2: ",tx_hash2)
        sleep(3000)
    # loop forever, printing the value of D5
