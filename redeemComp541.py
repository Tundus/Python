
#This module returns a bitcoin address based on 2 inputs, A) a public or a private key and B) a relative time lock value.
#Relative time lock value can be block height or time (units of 512 sec) as described in BIP112 however
#this info will only play a part when somebody will try to spend the funds sent to the created  address

import sys
#In Python 2.x bytes get messy hence the check, or at least this is what I read
if sys.version_info.major < 3:
    sys.stderr.write('Sorry, Python 3.x is required by this program.\n')
    sys.exit(1)

#These are mainly imports from python-bitcoinlib library  created by Peter Todd
import hashlib
from bitcoin import SelectParams
from bitcoin.base58 import encode, decode
from bitcoin.core import b2x, lx, x, COIN, COutPoint, CMutableTxOut, CMutableTxIn, CMutableTransaction, Hash160
from bitcoin.wallet import CBitcoinAddress, CBitcoinSecret,CKey
from bitcoin.core.script import CScript, OP_CHECKSEQUENCEVERIFY, OP_NOP3,  OP_DUP, OP_HASH160, OP_DROP, OP_EQUALVERIFY, OP_CHECKSIG, SignatureHash, SIGHASH_ALL
from bitcoin.core.key import *
from Crypto.PublicKey import RSA

#We will work on the testnet
SelectParams ('testnet')

#First argument is the secret key (private or public, compressed or uncompressed).
#Second argument is the delay (can be block height or time) expressed as int
seckey = str(sys.argv[1])
delay_value = int(sys.argv[2])

#Based on its length we should know if the received key is a priv or pub key. 
#Priv key is either 51 or 52 hex long. Compressed pubkey is 66 hex long, uncompressed:130 
if len(seckey)<53:
	#here comes a code that creates a public key based on the received private key
	#we 
	decode_hex_priv = b2x(decode(seckey)) #Remove Base58 encoding and turn byte sting into hex
	raw_priv = decode_hex_priv[2:66] # remove network byte and compression+checksum flags
	print ("Ez a decode_hex_priv hossza: %r" % len(decode_hex_priv))
	if len(decode_hex_priv)==76: #this is a compressed key (network_id+key+comp_flag+checksum
		seckey_pub = CKey(x(raw_priv)).pub
		key_received = "compressed private key"
	else:
		seckey_pub = CKey(x(raw_priv),compressed=False).pub #when uncompressed pub key is uncompressed too
		key_received = "uncompressed private key"
else:
	if len(seckey)<130: key_received = "compressed public key"
	else: 	key_received = "uncompressed public key"
	seckey_pub = x(seckey) #public key will be used 'as is' except turned into byte series


#Since CScript only takes byte arguments I have to convert
#time delay value into bytes
hex_delay = hex(delay_value)
byte_delay = bytes(hex_delay,'utf-8')

#Create redeem script. Since Peter Todd's library doesn't cater for OP_CHECKSEQUENCEVERIFY (Relative time lock)
#We will use OP_NOP3 instead which the new OP has substituted. By doing so users will be able to
#use the original bitcoinlib. Might worth a pull request in the future!
txin_redeemScript = CScript([byte_delay, OP_NOP3, OP_DROP, OP_DUP, OP_HASH160, Hash160(seckey_pub), OP_EQUALVERIFY, OP_CHECKSIG])


#Create P2SH pubkey format from redeem scrip
txin_scriptPubKey = txin_redeemScript.to_p2sh_scriptPubKey()

txin_p2sh_address = CBitcoinAddress.from_scriptPubKey(txin_scriptPubKey)

print ("I have received a(n) %s for the redeem script!" % key_received)
print ("This is your public key for the redeem script: %r" % b2x(seckey_pub))
print('Pay to: ', str(txin_p2sh_address)) 
