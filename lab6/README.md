

#### Lab 6: Description
In this lab, we will implement two programs. One program will generate random
data, and another program will calculate the entropy of that random data.

You can think of entropy as a measure of the amount of information. However,
perhaps a better intuition is to think of entropy as the difficulty of guessing
the information in something. So the higher the entropy, the higher the
difficulty.

For example, suppose I have data that contains 1 billion "a" characters. How
difficult is it to guess the 1 billion and 1th character? Perhaps very easy, as
it is most likely going to be "a". On the other hand, if the data has an equal
probability of any characters in the unicode standard, then the difficulty to
guess the next character is going to be pretty high. This is because we do not
have a high confidence in our guess.

Herein lies the idea of entropy: probability. How likely is it for us to guess a
good answer? If it is very likely, then we have low entropy. If it is not
likely, then we have high entropy. By definition, entropy is:

    % LaTeX Notation
    $H(X) = -\sum_{\forall i} (P(x_i)* lg(P(x_i))) $

Click on [render][1] to see rendered version.

[1]: https://www.codecogs.com/eqnedit.php?latex=$H(X)&space;=&space;-\sum_{\forall&space;i}&space;(P(x_i)*&space;lg(P(x_i)))&space;$

Here, `X` is a random variable with `n` events. The `P` is the probablity of an
event, the `lg` is the logarithm base 2. So what we are doing is adding the
probability of an event multipled by the base 2 log of that probability
for all events `x_i` in the random variable `X`.

Going back to our intution model, we are taking a weighted average of the
probabilities of each instance of possible values in the data. This then allows
us to measure the entropy. Using the logarithm base 2 is just by Shannon's
definition. Using this logarithm *does* give us some benefit for computing,
which is a question you will answer for this lab.


#### Lab 6: Requirements
The requirements for this lab are as follows:

* `generate.py`
    * Usage behavior: `python3 generate.py (random <size> | perfect)`
        * Data written out to `stdout`.
        * `random_data` generates `<size>` bytes of random ascii\* text.
        * EC: `perfect_eight` generate ascii\* text such that
            entropy is always 8 (ignores `<size>`).
    * Run `/usr/bin/time -f "%U" python3 generate.py random 4194304 >/dev/null`
        * Minor points deducted it takes more than 3 seconds on ECC.
        * Minor points awarded if it takes less than around 2 seconds on ECC.
    * All code you write is commented.
* `entropy.py`
    * Usage behavior: `python3 entropy.py`
        * Data read in from `stdin`.
        * Entropy written out to `stdout`.
    * All code you write is commented.
* `answer.txt`
    1. What is the maximum possible entropy for data of `base64` encoding?
    1. Derive a general formula for getting maximum entropy (start with
       definition of entropy). You can write by hand and scan, or use LaTeX or
       similar tool.  Hint: Recall that if encoding is `k` bits, then maximum
       entropy is `k`.


#### Lab 6: Hints
Useful functions:

* `ord`: convert character to integer representation
* `chr`: convert integer to unicode character (`str`)\*

Provided is a template file to help you get started with the random data
generator. You are required implement `random_data`, and can implement
`perfect_eight` for extra credit.

No template is provided for `entropy.py`. Use what you have learned (or already
know) to implement reading in the data and calculate the entropy. Below is one
math function to help you do the calculation:

* `math.log2`: important, we want base 2

Recall that we need the probability. If you don't know how to get started with
this, think back to your statistic course either in high school or college.
Suppose there are only three colors in this world\*\*: red, green, blue.

If you have a bag of red, green, and blue blocks, what is the probability of
getting a red block? Now suppose you have a bag of red, red, and blue
blocks. What is the probability of getting a red block now? How about the
probability of getting a green block?

We have the same thing here. The random data is a bag of a bunch of random
characters that are taken from all possible characters in the world. Some
characters may be missing, while other characters may be in abundance. We can
calculate the probability of each character the same way. After you have the
probability, the rest of the calculation is pretty simple.

\* we will use unicode representation, even though we only are interested in
ascii. The important part is that there are 256 possible choices (for 8 bits).
So it is okay if we use unicode representation, as long as there are only 256
possible characters regardless.

\*\* technically, this is true in the digital world.





