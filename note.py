Router 1
int f0/1
ip address 10.0.0.1 255.0.0.0
no shut
exit
int serial1/1
ip address 50.0.0.1 255.0.0.0
no shut

Router 2
int f0/1
ip address 150.0.0.1 255.255.0.0
no shut
exit
int serial1/0
ip address 50.0.0.2 255.0.0.0
no shut
exit
int serial1/1
ip address 100.0.0.1 255.255.0.0
no shut

Router 3
int f0/1
ip address 200.0.0.1 255.255.255.0
no shut
exit
int serial1/0
ip address 50.0.0.2 255.255.0.0
no shut

/-----------------------------------------------------------------/

pc1
int f0/0
ip address 10.0.0.2 255.0.0.0
no shut
no ip routing

pc2
int f0/0
ip address 150.0.0.2 255.255.0.0
no shut
no ip routing

pc3
int f0/0
ip address 200.0.0.2 255.255.255.0
no shut
no ip routing

/-----------------------------------------------------------------/

On Router 1:
ip route 200.0.0.0 255.255.255.0 50.0.0.2
exit
wr

On Router 2:
ip route 10.0.0.0 255.0.0.0 50.0.0.1
ip route 200.0.0.0 255.255.255.0 100.0.0.2
exit
wr

On Router 3:
ip route 10.0.0.0 255.0.0.0 50.0.0.1
exit
wr

/-----------------------------------------------------------------/

PC1:
ping 200.0.0.2
