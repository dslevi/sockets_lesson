import socket, sys, select
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(("10.1.10.100",5555))

running = True
while running:
    inputready, outputready, exceptready = select.select([my_socket, sys.stdin], [], [])

    for s in inputready:
        if s == my_socket:
            msg = s.recv(1024)
            if msg:
                print msg
            else:
                print "Disconnect from server!"
                running = False
        if s == sys.stdin:
            user_input = sys.stdin.readline()
            if user_input == "/quit":
                sys.exit(0)
            my_socket.sendall(user_input)

my_socket.close()