[![status](https://circleci.com/gh/Branbados/irc-application.svg?style=shield)](https://app.circleci.com/pipelines/github/Branbados/irc-application)
# Table of Contents
* [Introduction](#Introduction)
* [Technologies](#Technologies)
* [Installation](#Installation)
* [Client Commands](#ClientCommands)
* [License](#License)

# Introduction
This project implements a client and server for an Internet Relay Chat (IRC) application. The server is able to relay text between clients using websockets. Clients are able to make chatrooms and send messages to rooms for other clients to see.

# Technologies
This was written in Python using the socket, sys, and select packages. Testing is done using Pytest and unittest, and continuous integration is implemented using CircleCI.

# Installation
Make sure that you have Python 3 installed. The following commands will install the project and run the server.

```
git clone https://github.com/Branbados/irc-application.git
cd irc-application
python3 Server.py
```

You will need additional windows to run client applications.

```
python3 Client.py
```

# Client Commands
```/list```: Lists all rooms in the server.  
```/join```: Adds client to an existing room, or creates and joins a room if the room does not exist.  
```
/join #coding
```
```/leave```: Removes a client from a room. Removes the room from the server when the last client leaves.  
```
/leave #coding
```
```/send```: Sends a message to a room the client has joined. Can send to multiple rooms.  
```
/send #coding Boy I sure love Python!
/send #coding #python Look at this IRC app I made!
```
```/members```: Lists all clients in a room.  
```/quit```: Disconnects the client from the server.  

# License
This work is released under the MIT License. Please see the file LICENSE.md in this distribution for license terms.
