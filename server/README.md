# Socket server



## temp sensor ds18b20

https://www.circuitbasics.com/raspberry-pi-ds18b20-temperature-sensor-tutorial/

python3 skf/read_DS180.py


Måtte : 

sudo raspi-config -> interfaces -> enable som skrives i tutorial , men fikk det ikke til før jeg brukte sudo 
gjorde restarter og modprop commando, men usikker på hva som var sammenhengen for å få det til å virke. 
Feilkobling gjorde at ikke interface ble synlig.  

kan cat verdier direkte i /sys/bus/w1 ---/28-XXXX/ w1_slave filen som viser verdier.