MULTIPLEXING PSEUDOCODE

1. Open a file for writing
2. Iterate through the list of lists
  a. Iterate through each list of strings, 5 elements at a time
    i. If the list has a message to write, write it out in the format
           604xx: Messages
    ii. If the list has no message to write, write out the following string
           604xx: No messages
    iii. xx is the machine number, the index number of the list
3. Return the number of messages written to the file. 

DEMULTIPLEXING PSEUDOCODE

1. Create a list to hold messages from 60400
2. Create a list to hold messages from 60401
3. Create a list to hold messages from 60402
4. Create a list to hold messages from 60403
5. Create a list to hold messages all other messages
6. Open a file for reading
7. Go through the file line by line
  a. Determine which machine sent this message
  b. Place the message into the appropriate list
  c. We should only place the actual messages, not including the machine number
8. Return all lists in a tuple (so we end up with a tuple of lists)