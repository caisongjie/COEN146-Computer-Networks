
#### Lab 3: Port Assignment
Please use your assigned ports for testing purposes.
Your assigned port is listed in "port.pdf" under the reference directory.

#### Lab 3: Template File
Included at the bottle of the page are two template files (`client.py` and
`server.py`). These files have all the IO and terminal interface set up already.
As such, all you need to do, if using these template files, is to implement the
`client` and `server` functions.

Of course, you are free to implement everything from scratch, as long as your
program meets all the requirements in the requirements section below.

#### Lab 3: Requirements
Lab 3 requirements are as follows:

* Submit `client.py`, `server.py`, and `answer.txt` as
  a first level `tar` or `tar.gz`.
    * The file names must be exactly as shown above.
    * The `tar` or `tar.gz` name can be anything you want.
    * First level means the files in the archeive are not within a directory.
    * No other files nor directories should be in the archeive.
* Answer the following questions in `answer.txt`:
    1. What does `socket.connect()` do in context of UDP?
    2. Explain `socket.send()` vs `socket.sendto()` in context of UDP.
* `client.py`:
    * Usage behavior: `python3 client.py $host:$port $dst_file <$input_file`
    * Functional behavior:
        * Connect to `$host` on `$port` via UDP.
        * Send `$dst_file` name to server.
        * Send everything in `sys.stdin` (i.e. `$input_file`) to server.
        * Properly indicate termination of session to server when done reading.
        * Cleanly exits if `$host` does not exist.
    * Other Requirements:
        * Chunking is performed on `$input_file`.
        * Sufficient comments on top of most lines in `client` function.
* `server.py`:
    * Usage behavior: `python3 server.py $port`
    * Functional behavior:
        * Listens for incoming UDP connection on `$port`.
        * Receives `$dst_file` name.
        * Writes all data sent by client to `$dst_file`.
        * Properly terminates when client indicates termination.
    * Other Requirements:
        * Sufficient comments on top of most lines in `server` function.


#### Lab 3: Useful Functions and Constants
You will only need to know the following to do this lab:

* `byte.decode()`
* `socket.AF_INET`
* `random.random()` (optional, depends on how you implement session termination)
* `socket.bind()`
* `socket.connect()`
* `socket.gaierror`
* `socket.recv()`
* `socket.send()`
* `socket.socket()`
* `socket.SOCK_DGRAM`
* `str.encode()`




