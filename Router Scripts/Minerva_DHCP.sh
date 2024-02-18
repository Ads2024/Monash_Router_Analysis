# Place DHCP Server configuration here

log-facility local6;

default-lease-time 36000;
max-lease-time 72000;

ddns-update-style none;

subnet 77.41.217.0 netmask 255.255.255.0 {
  pool {
    range 77.41.217.20 77.41.217.21;
    default-lease-time 36000;
    option routers 77.41.217.1;
    option domain-name-servers 77.41.129.11;
    option domain-name "Delos.edu";
  }
}