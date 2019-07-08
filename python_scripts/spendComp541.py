#python spendComp541.py 7BCPbaEZGy5Mq56C9fLqthKYcr54BYN37wYj7ho1Lh887Y61oj 10 mnRXHdiFBGCSmYrVr7v58jmnjtdnMPMBFd mqUKY25Py8JMPgMjffSKW1eoikJDtziDQQ python spendComp541.py 7BCPbaEZGy5Mq56C9fLqthKYcr54BYN37wYj7ho1Lh887Y61oj 10 mnRXHdiFBGCSmYrVr7v58jmnjtdnMPMBFd mqUKY25Py8JMPgMjffSKW1eoikJDtziDQQ #This module returns a txid based on 2 inputs, a public or private key and a relative time lock value.
#Relative time lock can be either block height or time (units of 512 sec) as described in BIP112 expressed
#as int. Script call is as follows: python spendComp541.py PRIVKEY RELTIMELOCKVALUE FROMADDRESS TOADDRESS


#These are imports mainly from python-bitcoinlib library created by Peter Todd
import sys
import hashlib
from bitcoin import SelectParams
from bitcoin.base58 import encode, decode
import bitcoin.rpc
from bitcoin.core import b2x, lx, x, COIN, COutPoint, CMutableTxOut, CMutableTxIn, CMutableTransaction, Hash160
from bitcoin.wallet import CBitcoinAddress, CBitcoinSecret, P2PKHBitcoinAddress, CKey
from bitcoin.core.script import CScript, OP_CHECKSEQUENCEVERIFY, OP_NOP3,  OP_DUP, OP_HASH160, OP_DROP, OP_EQUALVERIFY, OP_CHECKSIG, SignatureHash, SIGHASH_ALL
from bitcoin.core.key import *
from decimal import *

#In Python 2.x bytes get messy hence the check!
if sys.version_info.major < 3:
    sys.stderr.write('Sorry, Python 3.x is required by this program.\n')
    sys.exit(1)

#This function will might help  us in toggling a certain bit
def toggleBit(int_type, offset):
	mask = 1 << offset	
	return(int_type ^ mask)

BlkHightOrTime = input ("Was it a relative lock (t)ime or lock (h)eight? (t/h):")

#We will work on testnet
SelectParams ('testnet')

#First argument is the secret key (private or public) second argument is the delay (can be block height or time)
seckey = str(sys.argv[1]) #this is the public or private key arg to recreate redeem script.
delay_value = int(sys.argv[2]) #This is the delay to be used for the redeem script and to be actually used for our output
P2SH_from_address = sys.argv[3] #This is the address where we should get the funds from
P2PKH_to_address = sys.argv[4] #This is the address where we will send the funds to

#We will work on testnet
SelectParams ('testnet')

#Based on its length we should know if the received key is a priv or pub key. 
#Priv key is either 51 or 52 hex long. Compressed pubkey is 66 hex long, uncompressed:130 
if len(seckey)<53:
	#here comes a code that creates a public key based on the received private key
	#we 
	decode_hex_priv = b2x(decode(seckey)) #Remove Base58 encoding and turn byte sting into hex
	raw_priv = decode_hex_priv[2:66] # remove network byte and compression+checksum flags
	if len(decode_hex_priv)==76: #this is a compressed key (network_id+key+comp_flag+checksum
		seckey_pub = CKey(x(raw_priv)).pub
		key_received = "compressed private key"
	else:
		seckey_pub = CKey(x(raw_priv),compressed=False).pub #when uncompressed pub key is uncompressed too
		key_received = "uncompressed private key"
else:
	if len(seckey)<130: key_received = "compressed public key"
	else: 	key_received = "uncompressed public key"
	seckey_pub = x(seckey) #public key will be used 'as is' if only it turned into byte series required by CScript


#Since CScript only takes byte arguments I have to convert
#time delay value into bytes
hex_delay = hex(delay_value)
byte_delay = bytes(hex_delay,'utf-8')

#Here we have to fetch the inputs or out points (txid and vout) for  
#our spend transaction, which #will be kindly provided by  the listunspent rpc call.
#Unspent transaction id's with vouts will be wrapped as COutPoints into an array
#Also, we will summarize the total amount of all spendable money on the
#input address for our send amount
proxy = bitcoin.rpc.Proxy()

r = proxy._call('listunspent', 0, 99999, [P2SH_from_address]) #for testing purposes we will fetch zero confirmed tx's as well


#create the txin structure and calculate the total spendable amount
txin = []
total_amount = 0

for unspent in r:

	#This is one of the key moments! I will set  nSequence for funding transactions FROM  0xfffffff TO 0xefffffff,
	#which tells the node that we are dealing with a time locked transaction.
 	#Depending on user input this should be a block height or relative time lock type
	#probably the best solution would be ammending Peter's library: script.CTxIn.stream_selialize
	#f.write(struct.pack_into(b"<I", 22,value) and add it to the CMutableTxIn. I didn't have the time
	#to experience with it.

	unspent['outpoint'] = CMutableTxIn(COutPoint(lx(unspent['txid']), unspent['vout']), nSequence = 0xefffffff)
	del unspent['txid']
	del unspent['vout']
	total_amount += unspent['amount']
	txin.append(unspent['outpoint'])

txout = []
txout.append(CMutableTxOut(total_amount, CBitcoinAddress(P2PKH_to_address).to_scriptPubKey()))

#This is a version 2 transaction and a time locked too
tx = CMutableTransaction(txin, txout, nLockTime = delay_value, nVersion = 2)

#Create the redeem script that should become part of scriptSig
txin_redeemScript = CScript([byte_delay, OP_NOP3, OP_DROP, OP_DUP, OP_HASH160, Hash160(seckey_pub), OP_EQUALVERIFY, OP_CHECKSIG])

sighash = SignatureHash(txin_redeemScript, tx, 0, SIGHASH_ALL)

sig = CKey(x(decode_hex_priv)).sign(sighash) + bytes([SIGHASH_ALL])

#I couldn't solve this issue. Something is not right here although I followed 
#the provided example. I got an error saying that I provided 3 positional argument
#whereas the script accepts 1 or 2. I can see 2 arguments down here.
#txin.scriptSig = CScript(sig, txin_redeemScript)


#calculate fees based on transaction length in bytes
#transaction byte length is:
tx_byte_length = len(tx.serialize())

#Current fee in Satoshi's per byte is 6 so let's set a correct transaction fee:
tx_fee = Decimal((tx_byte_length * 6) / COIN)

final_total = total_amount - tx_fee

#I should have been able to update the transaction fee in my txout but I got an error
#saying that a list doesn't have an nValue argument.
#txout.nValue = final_total

#If I was able to update my transaction value I would go back here and
#recreate the transaction from tx to txin.scriptSig.

print(b2x(tx.serialize()))
