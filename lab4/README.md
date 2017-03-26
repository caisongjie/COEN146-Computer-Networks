
#### Lab 4: Port Assignment
Please use your assigned ports for testing purposes.
Your assigned port is listed in "port.pdf" under the reference directory.


#### Lab 4: Description
In this lab, you are going to build upon lab 3. Recall that in lab 3, we wrote
"client", which transfers a file to the "server", which we also wrote. This
time, we will run "talk" and "listen" programs, which is similar to the
"client" and "server" programs.

The  "talk" program will transmit any text string the user types to the "listen"
program. The "listen" program will then display the received text string to
`stdout` as IP address of the sender ("talk") followed by a colon followed by a
space followed by the string that was sent.  For example, if the user at IP
address "192.168.0.1" sends "Hello There", the "listen" program should output:

    192.168.0.1: Hello There

The transmission should happen each time the "talk" user presses ENTER. Note
that newlines should *not* be sent. You are free to strip away all trailing and
leading whitespaces if you wish.

The user on the "talk" side can enter into a session by running the program, and
exit a session by pressing CTRL+D. Whenever the user exits via CTRL+D, the
"listen" program should **not** exit. However, if the user types "quit" (exactly
as shown, without quotes), both the "talk" and the "listen" side should
terminate.


#### Lab 4: Requirements
The requirements for this lab are as follows:

* Submit `talk.py` and `listen.py` as a `tar` or `tar.gz` archieve.
* `talk.py`:
    * Usage behavior: `python3 talk.py $host:$port`
    * Functional behavior:
        * Accepts input from `stdin`.
        * Sends input, each time ENTER is pressed, to `$host`.
        * Exits (and tells `$host` to exit) when "quit" is written.
    * Other Requirements:
        * Cleanly exits if `$host` does not exist.
        * Does not send newlines to the `$host`.
        * Sufficient comments on top of most lines you write.
* `listen.py`:
    * Usage behavior: `python3 listen.py $port`
    * Functional behavior:
        * Accepts messages from a "talk" user on port `$port`.
        * Prints all received messages to `stdout` in format:
            * `<ip>: <msg>`
        * Property terminates session when "talk" sends "quit".
    * Other Requirements:
        * Allows for multiple connections.
        * Sufficient comments on top of most lines you write.


#### Lab 4: Useful Functions and Constants
See the list from lab 3. Note that instead of `socket.recv()`, you should use
`socket.recvfrom()`. This is because you are interested in the address of the
sender this time, whereas you weren't for lab 3. Note also that you no longer
need `random.random()`, as you are now using "quit" as termination string.





