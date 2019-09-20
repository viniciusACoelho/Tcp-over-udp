import socket
import threading
import sys
import time
import pickle

   
def get_Host_Name_Ip():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return host_ip
    except:
        print("Unable to get Hostname and IP")

Host = '127.0.0.1'
Port = 10000
code = 1


connection_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
MyIp = (Host, Port)
connection_socket.bind(MyIp)

def  recv_con():
    while True:
        data, client = connection_socket.recvfrom(2048)
        tcpHeader = pickle.loads(data)
        if tcpHeader.syn == True:
            check_recv_connection(tcpHeader, client)

def  check_recv_connection(header, client):
    if header.syn == True:
        if True:
            print('Conexão recebida, enviando confirmação...')
            time.sleep(1)
        global code   
        connection_object = tcp_header(True, True, code)
        code = code + 1
        data_byte = pickle.dumps(connection_object)
        connection_socket.sendto(data_byte, client)
        thread_new_connection = threading.Thread(target=recv_message)
        create_thread()

#função que vai rodar na thread pra receber mensagem de uma conexão nova
def recv_message():
    while True:
        print('')

def create_thread():
    global thread_list
    newThread = threading.Thread(target=recv_message, args=len(thread_list))
    thread_list.append(newThread)



thread_list = []
thread = threading.Thread(target=recv_con, args='Thread principal')
thread_list.append(thread)
thread.start()

def create_socket():
    return 0
class tcp_header:
    code = None
    source_port_number = None
    destination_port_number = None
    sequence_number = None
    acknowledgement_number = None
    window_size = None
    syn = False
    ack = False
    fin = False
    rst = False
    msg = None

    def __init__(self, syn, ack, code):
        self.syn = syn
        self.ack = ack
        self.code = code

    def read_msg():
        print(msg)
    def write_msg(msgr):
        self.msg = msgr

#x = cabecalho_tcp
#print(sys.getsizeof(x))
