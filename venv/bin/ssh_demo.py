import paramiko
import socket

opts = paramiko.transport.Transport(socket.socket()).get_security_options()
print(opts.ciphers)
paramiko.Transport._preferred_ciphers = ('aes256-ctr', 'aes192-ctr', 'aes128-ctr')
opts = paramiko.transport.Transport(socket.socket()).get_security_options()
print(opts.ciphers)


print(opts.kex)
print(opts.digests)
print(opts.key_types)
print(opts.compression)

print (paramiko.transport.Transport(socket.socket()).disabled_algorithms)


client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('test.rebex.net',username='demo',password='password')

while True:
        text = raw_input("prompt")  # Python 2

        (stdin, stdout, stderr) = client.exec_command(text)
        for line in stdout.readlines():
                print line

client.close()
