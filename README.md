# Introduction

The `prime-field` module is a python module for dealing with finite
fields of prime characteristic. 

Roughly speaking a "field" is a mathematical structure where consistent
addition, subtraction, multiplication, and division operations are
defined. A "finite field" is a field where the number of elements is
finite. In this case, the number of elements of the field is called 
its "characteristic." It is a fact of number theory that the characteristic
must be a positive power of a prime number. In the case that the 
characteristic is a prime number itself, then the field is called a 
"prime field."

Perhaps the most familiar prime field is the Boolean field
where the elements are 0 and 1, addition (and subtraction) correspond
to XOR, and multiplication (and division) work as normal for 0 and 1.

More generally, every prime field of characteristic `p` can be realized 
as the ring of integers modulo `p`. A ring is just a mathematical structure
where consistent addition, subtraction, and multiplication operations
are defined, but not necessarily division. The interesting fact is that because
`p` is prime, this ring enjoys a division operation as well, thereby making
it into a field. 

More complicated finite fields are useful and interesting for
cryptography and erasure correcting codes, but they are not the focus of this
module. 

# Usage

Download the file `primefield.py` and put it in a suitable location
on your local system. Then you can import the module. 

```python
>>> import primefield
```

The module supports a number of different features. To get
started, you could try something like the following.
```python
>>> import primefield
>>> k = PrimeField(7) # create the field of characteristic 7
>>> a = k[6]    # field elements can be accessed as residues of integers
>>> b = k[-2]
>>> print(b) # show the residue class of b
'[5]_7'
>>> c = a/b # perform the division of a and b within the field
>>> print(c)
'[4]_7'
>>> d = ~b # access the inverse of the nonzero element b
>>> print(d)
'[3]_7'
>>> e = a ** 99 # raise a to the power 99
>>> print(e)
'[6]_7'
>>> e == a # check whether two elements are equal
True
>>> repr(a) # access the (canonical) representation of a
'Element(value=6, characteristic=7)'
>>> str(a) # access the (canonical) string representation of a as a residue class
'[6]_7'
>>> a == eval(repr(a)) # the representation is chosen so that it is compatible with evaluation
True 
```

# Future work

It would be nice to extend these features to fields of non-prime characteristic. One 
subtlety of doing so is that, in such a case, elements are represented by polynomials,
and there is some choice as to which representation is used. 

Since vector spaces are defined over fields, it would also be nice to support
the use of vectors and matrices defined over these prime fields. It would be particularly
interesting to support the construction of the inverse of an invertible matrix over
a prime field. 
