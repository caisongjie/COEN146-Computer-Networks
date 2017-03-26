
#### Lab 5: Port Assignment
Please use your assigned ports for testing purposes.
Your assigned port is listed in "port.pdf" under the reference directory.


#### Lab 5: Description
In this lab, you are going to build upon lab 3. Recall that in lab 3, we wrote
"client", which transfers a file to the "server", which we also wrote. The
"client" and "server" did not perform the transmission of data reliably. This is
because we used UDP, which means the data may be lost or corrupted. In this lab,
we will improve the reliability of our programs by implementing a modified
version of Stop-And-Wait called the Stop-And-Go protocol.

On the "server", instead of only receiving and accepting the data, we now need
to verify that the data was not corrupted. To do this, the "client" will need to
attach a checksum with the data. The "client" will also need to attach a
sequence number with the packet. This tells the "server" what sequence we are
on. The "server" will then compute the checksum using the received data, and
compare it to the checksum the "client" attached.  If the values are the same,
then the data is most likely not corrupted. At this point, the "server" should
send an acknowledgement to the "client". The acknowledgement should include the
next sequence number the "server" expects (i.e. 1 + the current sequence
number). However, if the message was corrupted, the "server" should send an
acknowledgement with the same current sequence in order to request a
retransmission of the current sequence.

On the "client", instead of only sending and forgetting the data, we now need to
wait for an acknowledgement from the "server". To do this, we simply wait for
the server to respond with an acknowledgement after each message we send. If we
never receive an acknowlegement, we will wait forever\*. If we get an
acknowledgement, but the sequence number has not changed, we will retransmit the
message. If we do get an acknowledgement, and the sequence number has changed,
we will proceed to that next sequence number.

Typically in Stop-And-Wait, we should send multiple messages at once, keeping
track of the sequences that has been sent, and resend when necessary. However,
for our modified version, we will only send and wait for one message at a time.
Further, we will not resend messages if we never get an acknowledgement. Indeed,
our modified version, the Stop-And-Go, will only handle message corruption, and
not lost messages nor missing acknowlegements.

\* This is one of the key difference between Stop-And-Wait and Stop-And-Go.


#### Lab 5: Requirements
The requirements for this lab are very similar to Lab 3:

* Submit `client.py` and `server.py` and `answers.txt` as an archieve.
* `client.py`:
    * Usage behavior: `python3 client.py $host:$port $dst_file <$input_file`
    * Functional behavior:
        * Structures data to include checksum and sequence.
        * Properly serializes data.
        * Waits for acknowledgement.
        * Retransmits when message is corrupted.
        * All `client.py` requirements from Lab 3.
    * Other Requirements:
        * Sufficient comments on top of most lines you write.
        * Does not print out anything unnecessary.
* `server.py`:
    * Usage behavior: `python3 server.py $port`
    * Functional behavior:
        * Checks checksum to verify data.
        * Properly deserializes data.
        * Sends acknowledgement.
        * Indicates message corruptions.
        * All `server.py` requirements from Lab 3.
    * Other Requirements:
        * Sufficient comments on top of most lines you write.
        * Does not print out anything unnecessary.
* `answers.txt`:
    1. Why is `chunk_size` and `packet_size` different?
    1. Explain the idea of a checksum in the context of this lab.
    1. What is serialization and deserialization (Hint: See Hints)?
    1. Provide some ideas to modify the code so that we will be able to handle
       lost messages and missing acknowledgements (i.e. ideas on how we might go
       about implementing the full Stop-And-Wait protocol).


#### Lab 5: Template Files
Provided on this site are template files for this lab. The template files have
most of the interface and lab 3 work done for you. You will only be responsible
for implementing `reliable_send` and `reliable_recv` if using these template
files.

Be sure not to copy and paste the code. Rather, you should right click the file
and download it.


#### Lab 5: Hints
For this lab, the "client" needs to attach a checksum and sequence number. The
simplest, but perhaps the worst, way to do this is to simply append the checksum
and sequence to the beginning of the message. A more complicated, but better,
way is to provide some sort of structure. You should use a `dict` to store your
packet information. Perhaps use a key `"data"` to map to the actual data, a key
`"sequence"` to map to the sequence number, and a key `"checksum"` to map to the
checksum. For example:

    packet = { "data": data,    
               "sequence": sequence,
               "checksum": compute_checksum(data) }  

Or equivalently:

    packet = dict()  
    packet["data"] = data  
    packet["sequence"] = sequence
    packet["checksum"] = compute_checksum(data)  

Ideally, you now want to send the `packet` to the server by encoding on the
client side and decoding on the server side. The problem is, you can't really
encode a `dict`. Instead, you must first serialize the packet dictionary before
sending it, and then deserialize after receiving it. Namely:

    # on the client
    udp_socket.send(json.dumps(packet).encode())

And:

    # on the server
    packet = json.loads(udp_socket.recv(packet_size).decode())

What is happening on the side of the client is that the dictionary is being
converted to a string representation (a process called serialization). Then, it
is being encoded so that we can transmit it over the network. On the server
side, the data received is decoded into a string representation, and converted
back to a Python object (a process called deserialization).

The hints provided here should give you all the tools needed to implement our
Stop-And-Go protocol. Another hint is that whenever a client connects to a
server, the client automatically opens up a port to listen for server responses.
As such, you will be able to send acknowledgement from the server directly to
the client without requiring the client to use `bind`.


