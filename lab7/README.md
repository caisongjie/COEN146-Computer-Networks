

#### Lab 7: Description
We will implement a program that calculates a Diffie-Hellman shared key in this
lab. There will be no network communication, only the calculation will be done.

Simply put, Diffie-Hellman Key Exchange involves two\* parties: Alice and Bob.
There exists two publicly known values: a prime number and the primitive root of
that prime number (also known as the base). Each party will obtain\*\* a private
key. Using the private key and the publicly known values, each party will then
compute a public key.

\* There are extensions to the Diffie-Hellman Key Exchange protocol that allows
   for multi-party use cases.

\*\* This is usually done by randomly generating the value. For this lab, we
     will not randomly generate it. Instead, we will specify the value using
     commandline arguments.

The public key is then send insecurely over the network to each other. Each
party then combines the received public key with their private key (so Alice
"adds" her private key to Bob's public key, and Bob "adds" his private key to
Alice's public key). At this point, both Alice and Bob will have the same shared
key, which can then be used to encrypt messages for secure communication.

See the below image for an illustration.

![example](https://upload.wikimedia.org/wikipedia/commons/4/46/Diffie-Hellman_Key_Exchange.svg)

Here, the common paint is the prime and base. The secret colors are the private
keys of each party. The public transport is the public key created using the
private key and the publicly known prime and base. After the exchange of the
public keys, each party they adds their private key to the public key of the
other party, and we end up with a shared secret key.

The theory is that it is extremely difficult to get the private key using only
the publicly known values and the public keys. In the example above, the theory
is that it is extremely difficult to get the secret colors using only the common
paint and public transport colors.

To actually do this in practice, we use numbers instead of colors. The whole of
Diffie-Hellman can be described as:

    % Latex Notation
    $SharedKey \equiv A^b \equiv (g^a)^b \equiv (g^b)^a \equiv B^a \pmod{p}$

Where `A` and `B` are Alice and Bob's public keys, `a` and `b` are Alice and
Bob's private keys, `g` is the primitive root (base), and `p` is the prime.
Click on [render][1] to see rendered version.

[1]: https://www.codecogs.com/eqnedit.php?latex=$SharedKey&space;\equiv&space;A^b&space;\equiv&space;(g^a)^b&space;\equiv&space;(g^b)^a&space;\equiv&space;B^a&space;\pmod{p}$

For your implementation, you can either use that equation and write a short
program to arrive at the answer immediately, or you can perform the whole key
exchnage operation. If you do the second approach, your program will look more
realistic. Namely, you will first compute the public keys, then you will
"transfer" them (which in this lab will be a simple assignment), and then
finally compute the shared secret. For an example, see
[Wikipedia](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange#Cryptographic_explanation).


#### Lab 7: Requirements
The requirements for this lab are as follows:

* `diffiehellman.py`
    * Usage behavior: `python3 diffiehellman.py <a_pk> <b_pk> [ <prime> <base> ]`
        * Template file available for parsing the input.
    * Compute shared key and print to `stdout` the following:
        * `Shared Key: <the shared key>`
        * This is the string "Shared Key" followed by ":" followed by a space
          followed by the shared key value.
    * All code you write is commented.
* `talk.py` and `listen.py`
    * Lab 4 solution available on this page.
    * Add pseudocode for implementing secure communication with
      Diffie-Hellman Key Exchange.
        * Pseudocode should look like actual code and be enough to use as
          implementation guide.
        * Write Psueudocode as comments in `secure_send` and `secure_recv`.
        * Styling is important. Don't write one long line. Use `#` comments.
        * Hint: The key exchange protocol should be done each time the function
          is called (think why).
    * Extra credit given if your psuedocode supports multiple `talk` users.
        * Hint: Use generators (no need for threading or multiprocessing).
    * Pretend you are given `encrypt()` and `decrypt()` functions.


#### Lab 7: Grade Distribution

* `diffiehellman.py` is 50%
* `talk.py` and `listen.py` is 50%






