#!/usr/bin/env python3



ip_a = input("Enter IP address #1: ")
ip_al = ip_a.split(".")
ip_al_int = [ int(x) for x in ip_al]
ip_ad1 = ip_al_int[0]*(2**24)
ip_ad2 = ip_al_int[1]*(2**16)
ip_ad3 = ip_al_int[2]*(2**8)
ip_ad4 = ip_al_int[3]
ip_an = ip_ad1 + ip_ad2 + ip_ad3 + ip_ad4

ip_b = input("Enter IP address #2: ")
ip_bl = ip_b.split(".")
ip_bl_int = [ int(x) for x in ip_bl]
ip_bd1 = ip_bl_int[0]*(2**24)
ip_bd2 = ip_bl_int[1]*(2**16)
ip_bd3 = ip_bl_int[2]*(2**8)
ip_bd4 = ip_bl_int[3]
ip_bn = ip_bd1 + ip_bd2 + ip_bd3 + ip_bd4

ip_m = input("Enter the subnet mask: ")
ip_ml = ip_m.split(".")
ip_ml_int = [ int(x) for x in ip_ml]
ip_md1 = ip_ml_int[0]*(2**24)
ip_md2 = ip_ml_int[1]*(2**16)
ip_md3 = ip_ml_int[2]*(2**8)
ip_md4 = ip_ml_int[3]
ip_mn = ip_md1 + ip_md2 + ip_md3 + ip_md4

bin(ip_an)
bin(ip_bn)

net_a = bin (ip_an & ip_mn)
net_b = bin (ip_bn & ip_mn)

if (net_a == net_b):
    print (ip_a, "and", ip_b, "are on the same subnet")

if (net_a != net_b):
    print (ip_a, "and", ip_b, "are not on the same subnet")


