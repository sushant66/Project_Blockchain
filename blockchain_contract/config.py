"""
    Configuration files. Please double check all the informations for the
    project to run correctly.

    The included CA certificate is for `Amazon Root CA 1`, and it's being used
    for *.infura.io RPC node. Omit it if your node is not using https, or
    change it with the one of your CA.
"""

# Network configuration

WIFI_SSID = 'omkar'
WIFI_PASSWORD = 'Sainath@123'


# Ethereum configuration

RPC_URL = 'ropsten.infura.io/v3/203de21bf7754576bf877024b3f908d5'

ADDRESS = '0x33BAaF08A7A6a1CE6d06c12D1F5B33B621bABFAC'
PRIVATE_KEY = '0xf2bd611d24aec089a5fc98fd2da8351dea4ae65bd8e921e25c46a3f373f59cb7' # Note the '0x' prefix - it must be used

BET_AMOUNT = 50 # The Wei amount to be used as a bet

# Do not edit below if not sure
CONTRACT_ADDRESS = '0xfA6FB40eFE9e66eb82bCB44392f722EDF4C9B70C'#0x546bc268a99a6d4f65256e295a138b7f1e3634d8 working  #0xc3907D59091400bB6D9A8BA6296C1838De4227Dc vikas_1     #0xd18fcacba5ae4c395ecd0319d92cfdb8f6328d18 simple 0x2aF103a4C268Bd8D91d528f36CAE4de94Fb06c4B 2 out

# Methods interface
# Name, arguments types, and  gas limit must be specified.
CONTRACT_METHODS = {
    "get": {
        "args": (),
        "gas_limit": "0x6691b7",
    },
    "get2": {
        "args": (),
        "gas_limit": "0x6691b7",
    }
}

GAS_PRICE = "0x174876e800"

CA_CERT = """-----BEGIN CERTIFICATE-----
MIIDQTCCAimgAwIBAgITBmyfz5m/jAo54vB4ikPmljZbyjANBgkqhkiG9w0BAQsF
ADA5MQswCQYDVQQGEwJVUzEPMA0GA1UEChMGQW1hem9uMRkwFwYDVQQDExBBbWF6
b24gUm9vdCBDQSAxMB4XDTE1MDUyNjAwMDAwMFoXDTM4MDExNzAwMDAwMFowOTEL
MAkGA1UEBhMCVVMxDzANBgNVBAoTBkFtYXpvbjEZMBcGA1UEAxMQQW1hem9uIFJv
b3QgQ0EgMTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBALJ4gHHKeNXj
ca9HgFB0fW7Y14h29Jlo91ghYPl0hAEvrAIthtOgQ3pOsqTQNroBvo3bSMgHFzZM
9O6II8c+6zf1tRn4SWiw3te5djgdYZ6k/oI2peVKVuRF4fn9tBb6dNqcmzU5L/qw
IFAGbHrQgLKm+a/sRxmPUDgH3KKHOVj4utWp+UhnMJbulHheb4mjUcAwhmahRWa6
VOujw5H5SNz/0egwLX0tdHA114gk957EWW67c4cX8jJGKLhD+rcdqsq08p8kDi1L
93FcXmn/6pUCyziKrlA4b9v7LWIbxcceVOF34GfID5yHI9Y/QCB/IIDEgEw+OyQm
jgSubJrIqg0CAwEAAaNCMEAwDwYDVR0TAQH/BAUwAwEB/zAOBgNVHQ8BAf8EBAMC
AYYwHQYDVR0OBBYEFIQYzIU07LwMlJQuCFmcx7IQTgoIMA0GCSqGSIb3DQEBCwUA
A4IBAQCY8jdaQZChGsV2USggNiMOruYou6r4lK5IpDB/G/wkjUu0yKGX9rbxenDI
U5PMCCjjmCXPI6T53iHTfIUJrU6adTrCC2qJeHZERxhlbI1Bjjt/msv0tadQ1wUs
N+gDS63pYaACbvXy8MWy7Vu33PqUXHeeE6V/Uq2V8viTO96LXFvKWlJbYK8U90vv
o/ufQJVtMVT8QtPHRh8jrdkPSHCa2XV4cdFyQzR1bldZwgJcJmApzyMZFo6IQ6XU
5MsI+yMRQ+hDKXJioaldXgjUkK642M4UwtBV8ob2xJNDd2ZhwLnoQdeXeGADbkpy
rqXRfboQnoZsG4q5WTP468SQvvG5
-----END CERTIFICATE-----
\x00"""
