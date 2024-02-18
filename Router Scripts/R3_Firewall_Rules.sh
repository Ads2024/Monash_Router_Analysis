#This is a shell script and hash character makes the rest of the lin 
# as comment
 
# Incoming DNS requests to the DNS server
#internal
iptables -A FORWARD -i eth2 -o eth0 -d 107.200.253.10 -p udp --dport 53 -m state --state NEW,RELATED,ESTABLISHED -j ACCEPT
iptables -A FORWARD -i eth2 -o eth0 -d 107.200.253.10 -p tcp --dport 53 -m state --state NEW,RELATED,ESTABLISHED -j ACCEPT

#External
iptables -A FORWARD -i eth3 -o eth0 -d 107.200.253.10 -p udp --dport 53 -m state --state NEW,RELATED,ESTABLISHED -j ACCEPT
iptables -A FORWARD -i eth3 -o eth0 -d 107.200.253.10 -p tcp --dport 53 -m state --state NEW,RELATED,ESTABLISHED -j ACCEPT

# Outgoing DNS server to response
#internal
iptables -A FORWARD -i eth0 -o eth2 -s 107.200.253.10 -p udp --sport 53 -m state --state RELATED,ESTABLISHED -j ACCEPT
iptables -A FORWARD -i eth0 -o eth2 -s 107.200.253.10 -p tcp --sport 53 -m state --state RELATED,ESTABLISHED -j ACCEPT

#External
iptables -A FORWARD -i eth0 -o eth3 -s 107.200.253.10 -p udp --sport 53 -m state --state RELATED,ESTABLISHED -j ACCEPT
iptables -A FORWARD -i eth0 -o eth3 -s 107.200.253.10 -p tcp --sport 53 -m state --state RELATED,ESTABLISHED -j ACCEPT

# Incoming HTTP requests to the web server
#Internal
iptables -A FORWARD -i eth2 -o eth0 -d 107.200.253.11 -p tcp --dport 80 -m state --state NEW,RELATED,ESTABLISHED -j ACCEPT

#External
iptables -A FORWARD -i eth3 -o eth0 -d 107.200.253.11 -p tcp --dport 80 -m state --state NEW,RELATED,ESTABLISHED -j ACCEPT

# Outgoing web server to response
#Internal
iptables -A FORWARD -i eth0 -o eth2 -s 107.200.253.11 -p tcp --sport 80 -m state --state RELATED,ESTABLISHED -j ACCEPT

#External
iptables -A FORWARD -i eth0 -o eth3 -s 107.200.253.11 -p tcp --sport 80 -m state --state RELATED,ESTABLISHED -j ACCEPT

# Incoming SMTP requests to the mail server
#Internal
iptables -A FORWARD -i eth2 -o eth0 -d 107.200.253.12 -p tcp --dport 25 -m state --state NEW,RELATED,ESTABLISHED -j ACCEPT

#External
iptables -A FORWARD -i eth3 -o eth0 -d 107.200.253.12 -p tcp --dport 25 -m state --state NEW,RELATED,ESTABLISHED -j ACCEPT

# Outgoing mail server to response to SMTP requests
#Internal
iptables -A FORWARD -i eth0 -o eth2 -s 107.200.253.12 -p tcp --sport 25 -m state --state RELATED,ESTABLISHED -j ACCEPT

#External
iptables -A FORWARD -i eth0 -o eth3 -s 107.200.253.12 -p tcp --sport 25 -m state --state RELATED,ESTABLISHED -j ACCEPT

#Allow DNS Server to Initiate Queries

iptables -A FORWARD -i eth0 -o eth3 -s 107.200.253.10 -p udp --dport 53 -m state --state NEW,RELATED,ESTABLISHED -j ACCEPT
iptables -A FORWARD -i eth0 -o eth3 -s 107.200.253.10 -p tcp --dport 53 -m state --state NEW,RELATED,ESTABLISHED -j ACCEPT

#Allow Web Server to Initiate Outbound HTTP/HTTPS

iptables -A FORWARD -i eth0 -o eth3 -s 107.200.253.11 -p tcp --dport 80 -m state --state NEW,RELATED,ESTABLISHED -j ACCEPT
iptables -A FORWARD -i eth0 -o eth3 -s 107.200.253.11 -p tcp --dport 443 -m state --state NEW,RELATED,ESTABLISHED -j ACCEPT


#Allow Mail Server to Send Emails.
iptables -A FORWARD -i eth0 -o eth3 -s 107.200.253.12 -p tcp --dport 25 -m state --state NEW,RELATED,ESTABLISHED -j ACCEPT

# If using secure SMTP or submission ports
iptables -A FORWARD -i eth0 -o eth3 -s 107.200.253.12 -p tcp --dport 465 -m state --state NEW,RELATED,ESTABLISHED -j ACCEPT
iptables -A FORWARD -i eth0 -o eth3 -s 107.200.253.12 -p tcp --dport 587 -m state --state NEW,RELATED,ESTABLISHED -j ACCEPT

# Accept all traffic from internal subnets to DMZ
iptables -A FORWARD -i eth1 -o eth0 -m state --state NEW,ESTABLISHED,RELATED -j ACCEPT
iptables -A FORWARD -i eth2 -o eth0 -m state --state NEW,ESTABLISHED,RELATED -j ACCEPT

# Accept return traffic from DMZ to internal subnets
iptables -A FORWARD -i eth0 -o eth1 -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables -A FORWARD -i eth0 -o eth2 -m state --state ESTABLISHED,RELATED -j ACCEPT

# Accept SSH from internal subnets to DMZ servers
iptables -A FORWARD -i eth2 -o eth0 -s 107.200.96.0/24 -d 107.200.253.0/24 -p tcp --dport 22 -m state --state NEW,RELATED,ESTABLISHED -j ACCEPT
iptables -A FORWARD -i eth2 -o eth0 -s 107.200.32.0/24 -d 107.200.253.0/24 -p tcp --dport 22 -m state --state NEW,RELATED,ESTABLISHED -j ACCEPT
iptables -A FORWARD -i eth2 -o eth0 -s 107.200.57.0/24 -d 107.200.253.0/24 -p tcp --dport 22 -m state --state NEW,RELATED,ESTABLISHED -j ACCEPT

# Accept established and related connections back from DMZ to internal networks
iptables -A FORWARD -i eth0 -o eth2 -m state --state RELATED,ESTABLISHED -j ACCEPT


# Allow all internal traffic routed through eth2
iptables -A FORWARD -i eth2 -o eth2 -m state --state NEW,RELATED,ESTABLISHED -j ACCEPT


#Internal stateful inspection
iptables -A FORWARD -i eth1 -o eth2 -m state --state RELATED,ESTABLISHED -j ACCEPT
iptables -A FORWARD -i eth2 -o eth1 -m state --state RELATED,ESTABLISHED -j ACCEPT

# Accept all outbound traffic from internal subnets to the external network
iptables -A FORWARD -i eth1 -o eth3 -m state --state NEW,ESTABLISHED,RELATED -j ACCEPT
iptables -A FORWARD -i eth2 -o eth3 -m state --state NEW,ESTABLISHED,RELATED -j ACCEPT

# Accept inbound traffic from the external network only if it is related to an established connection
iptables -A FORWARD -i eth3 -o eth1 -m state --state RELATED,ESTABLISHED -j ACCEPT
iptables -A FORWARD -i eth3 -o eth2 -m state --state RELATED,ESTABLISHED -j ACCEPT

# Allow SSH traffic from the client's subnet to R3 via eth2
iptables -A INPUT -i eth2 -p tcp --dport 22 -m state --state NEW,RELATED,ESTABLISHED -j ACCEPT

# Allow SSH responses from R3 to the client's subnet via eth2
iptables -A OUTPUT -o eth2 -m state --state RELATED,ESTABLISHED -j ACCEPT

# Allow ICMP echo requests from R3 to DMZ
iptables -A OUTPUT -o eth0 -p icmp --icmp-type echo-request -j ACCEPT

# Allow ICMP echo replies from DMZ to R3
iptables -A INPUT -i eth0 -p icmp --icmp-type echo-reply -j ACCEPT

# Allow ICMP echo requests from R3 to internal networks
iptables -A OUTPUT -o eth2 -p icmp --icmp-type echo-request -j ACCEPT

# Allow ICMP echo replies from internal networks to R3
iptables -A INPUT -i eth2 -p icmp --icmp-type echo-reply -j ACCEPT

# Allow ICMP echo requests from DMZ to R3
iptables -A INPUT -i eth0 -p icmp --icmp-type echo-request -j ACCEPT

# Allow ICMP echo replies from R3 to DMZ
iptables -A OUTPUT -o eth0 -p icmp --icmp-type echo-reply -j ACCEPT

# Allow ICMP echo requests from internal networks to R3
iptables -A INPUT -i eth2 -p icmp --icmp-type echo-request -j ACCEPT

# Allow ICMP echo replies from R3 to internal networks
iptables -A OUTPUT -o eth2 -p icmp --icmp-type echo-reply -j ACCEPT

# Drop all other traffic
iptables -P INPUT DROP
iptables -P OUTPUT DROP
iptables -P FORWARD DROP 