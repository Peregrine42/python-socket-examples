###Installing OS on Raspberry Pi
 - format the SD card to FAT32
 - download a raspbian disk image (http://downloads.raspberrypi.org/raspbian_latest)
 - dd the image onto the SD card (e.g sudo dd if=/path/to/image of=/dev/rdisk1)
 - put the SD card into the Pi and boot up
 - find a computer/monitor with an HDMI cable
 - complete the raspberry pi setup - make sure to enable ssh

###Set up a Windows machine to find a raspberry pi
 - Control Panel > Network And Sharing Center > Change adapter settings
 - right click ethernet > Properties
 - select Internet Protocol Version 4
 - select Properties...
 - select Use the following IP address
   - IP Address = 192.168.1.1
   - Subnet mask = 255.255.255.0
   - Default gateway = 192.168.1.3 (not sure this is essential but this is what worked)
 - click OK

###Modify Pi SD card To Connect to Webtop
 - connect SD card to Ubuntu - it should mount automatically
 - go to /etc/network/interfaces
 - change to this:
    auto lo eth0
    iface lo inet loopback
    iface eth0 inet static
        address 192.168.1.2
        netmask 255.255.255.0
        gateway 192.168.1.1

###SSH to Raspberry Pi
 - username: raspberry
 - password: pi
 - ssh pi@192.168.2.1
