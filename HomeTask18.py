from multiprocessing import Process, Pipe
from time import sleep
from os import getpid

def ponger(receiver, sender, response):
    sender.send(response)
    while True:
        # receive a message
        receiver.recv()
        # print it as f"Process{getpid()} got message: {msg}"
        print(f' Process {getpid()} got message: {response}')
        # sleep before responding
        sleep(2)
        # send response message back
        sender.send(response)


if __name__ == "__main__":
    # create 2 pipes
    sender_1, receiver_2 = Pipe()
    sender_2, receiver_1 = Pipe()
    # create 2 processes that will use ponger, give them different sides of pipes
    # they also need a specific message (either ping or pong)
    # start both processes
    # initiate ping-pong by sending first message to one of the pipes
    process_1 = Process(target=ponger, args=(receiver_1, sender_1, "ping")).start()
    process_2 = Process(target=ponger, args=(receiver_2, sender_2, "pong")).start()
