0x0B. SSH
Introduction
SSH (Secure Shell) is a protocol used to securely connect to remote systems over a network. It provides a secure channel over an unsecured network by using a pair of cryptographic keys (public and private) for authentication and encryption.

Resources
What is a (physical) server?
Text
Video
SSH Essentials
SSH Config File
Public Key Authentication for SSH
How Secure Shell Works
SSH Crash Course (Highly informative video, may be helpful to watch at x1.25 speed or above)
For Reference
Understanding the SSH Encryption and Connection Process
Secure Shell Wiki
IETF RFC 4251 (Description of the SSH Protocol)
Internet Engineering Task Force
Request for Comments (RFCs)
Tasks
0. Use a Private Key
Learn to use SSH with a private key for secure authentication.
1. Create an SSH Key Pair
Generate a pair of SSH keys (public and private) for secure authentication.
2. Client Configuration File
Configure SSH clients using a configuration file for streamlined connections.
3. Let Me In!
Use the generated keys and configuration to securely access remote servers.
4. Client Configuration File (w/ Puppet)
Automate the setup and management of SSH client configurations using Puppet.
Explanation for README
SSH, or Secure Shell, is a protocol designed to provide a secure method for remote login from one computer to another. It ensures that all data transmitted over the network is encrypted, protecting against eavesdropping, connection hijacking, and other attacks. SSH uses a pair of cryptographic keys (public and private) to authenticate the user and establish a secure channel for communication.

To effectively use SSH, one must understand how to generate and use SSH keys, configure the SSH client, and automate the setup process for multiple clients using tools like Puppet. The resources provided in this project cover the essentials of SSH, including its configuration, public key authentication, and the underlying encryption and connection process.

This project also includes practical tasks to help you implement SSH in a real-world scenario, ensuring you can securely access and manage remote systems.

For more detailed information, please refer to the provided resources and RFC documents.
