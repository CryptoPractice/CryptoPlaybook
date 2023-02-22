Pad the Flag
Introduction
The padding oracle vulnerability has been made known for some times but can unfortunately still be found in many modern applications. It is easily overlooked when developers implement the padding algorithm or utilize the cryptographic functions. This challenge demonstrated even a secure cryptosystem can be broken easily due to insecure implementation on PKCS#1 v1.5 padding.

Info for participants
Challenge Description
Jaga arrived at a new town known as paddington and is tasked with identifying the vulnerabilities within it's local registrar server. Jaga must privilege escalate to admin and retrieve the flag to prove that Jaga was able to fully compromise the server.

Additional Instructions
-

Info for HTB
Access
-

Key Processes
-

Automation / Crons
-

Firewall Rules
-

Docker
Docker is used to build, setup and copied the related files to a python docker container which running a tcp port 9000.

sudo docker build -t padtheflag .
sudo docker run -d --rm --name padtheflag -p 9000:9000 padtheflag:latest 
Other
-