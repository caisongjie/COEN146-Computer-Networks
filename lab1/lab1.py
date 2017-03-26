def multiplex(messages):
    txt = "mux_stream"
    file = open(txt,'w')
    count = 0
    for x in messages:
        count = count + len(x)
    #get number of elements in the list; decrease the count while poping
    while count > 0:
        machine = 60400
        for a in messages:
            for b in range(5):
                if len(a) != 0:
                    temp = a.pop(0)
                    print('{}: {}'.format(machine, temp))
                    file.write('%s: %s\n'%(machine, temp))
                    count -= 1
                else:
                    print('%s: No messages'%machine)
                    file.write('%s: No messages\n'%machine)
            machine += 1
    file.close()

def demultiplex(input_file='mux_stream'):
    # you should write this function and get rid of the statement on the next line
    # initialize the tuple consisting of 5 lists; append the messages to the corresponding list
    t1 = ([],[],[],[],[])
    with open(input_file,'r') as f:
        for txt in f:
            if txt[7:-1] != 'No messages':
                index = int(txt[0:5]) - 60400
                if index > 4:
                    t1[4].append(txt[7:-1])
                else:
                    t1[index].append(txt[7:-1])
    print(t1)
    return t1
## YOU DON'T NEED TO EDIT ANYTHING BELOW HERE

def test_case_1():
    """Testing Multiplexing with tons of messages."""
    # we have to keep the type immutable and then create a copy or else pass by argument will
    # mutate the variable
    messages = (
        ('1', '2', '3', '4', '5', '6', '7', '8', '9'),
        ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17'),
        ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'),
        ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16'),
        ('1', '2', '3', '4'),
        ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20')
    )
    # this will get consumed if we pass as list of lists so make a copy
    messages_copy = [list(msgs) for msgs in messages]
    multiplex(messages_copy)
    messages_received = demultiplex('mux_stream')
    assert len(messages_received[0]) == 9
    assert len(messages_received[1]) == 17
    assert len(messages_received[2]) == 20
    assert len(messages_received[3]) == 16
    assert len(messages_received[4]) == 24

def test_case_2():
    """Testing multiplexing with tons of lost messages."""
    # we have to keep the type immutable and then create a copy or else pass by argument will
    # mutate the variable
    messages = (
        ("This ain't", "no intro,", " this the entree"),
        (),
        (),
        (),
        ("Hit that", "intro with Kanye ", "and sound like Andre"),
        ("Tryna", "turn", "my", "baby", "mama", "to", "my", "fiancee"),
        ("She like"," music, she from", "Houston",  "like Auntie Yonce"),
        ("Man my daughter couldn't", "have a better mother"),
        ("If she ever", "find another, he", "better", "love", "her")
    )
    # this will get consumed if we pass as list of lists so make a copy
    messages_copy = [list(msgs) for msgs in messages]
    multiplex(messages_copy)
    messages_received = demultiplex('mux_stream')
    assert len(messages_received[0]) == 3
    assert len(messages_received[1]) == 0
    assert len(messages_received[2]) == 0
    assert len(messages_received[3]) == 0
    assert len(messages_received[4]) == 22

if __name__ == '__main__':
    test_case_1()
    test_case_2()
