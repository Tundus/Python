This is a small explanation to my 2 scripts for the first assignment.

1) redeemComp541.py script will return an address. 
It expects 2 inputs:
a) a key that can be anything, public, private, compressed, uncomressed and 
b) a relative time lock as an integer, which can be block height or time. 
for the address it doesn't matter which one it is but the same have to be
provided for the spend script.

2) spendComp541.py will create a bitcoin transaction and return it's id.
It expects 4 inputs:
a) a private key
b) a relative time lock value
c) a from address and
d) a to address

It will also prompt the user for a decision whether the provided value is a block height (h)
or a lock time (t).

My second script will limp on 3 points.

1) I should have implemented a bit toggling for flagging which type of relative time lock it is (b/h)
In case I had more time I could have implemented it as an amend to Peter Todd's library.
2) I couldn't sign the transaction with the created signature as txin didn't let me ammend 
the scriptSig as I described it in my code. This might have happend as I created as a list and
not as a tuple. As a matter of fact this hindered me to realize the 3 point
3) I could calculate the transaction fee however for the reason in point 2) I couldn't amend
my txout. It returned an error. I am sure that this all goes back to my incomplete coding knowledge,
which is no excuse I appriciate that.

All in all, I would like to thank you for the assignement. I have already acquired an immense amount
of knowledge on coding but most importantly on Bitcoin.

Talk to you soon!

Andras
