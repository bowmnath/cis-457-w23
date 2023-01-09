Note: some questions may be taken entirely or in part from your textbook.

# General Questions

1. Explain the purpose of a "welcome" socket vs a "connection" socket in TCP.

2. Consider two scenarios:
* A receptionist at a busy office handles clients' phone calls directly and
  addresses their concerns themself.
* The receptionist instead greets the customer and then connects the customer
  with a different representative who handles the customer's question.
One of these scenarios is more like TCP, and the other more like UDP.
Explain.

3. Consider a standard answering machine and a person who calls two separate
times back-to-back and leaves a voicemail each time.
When you are listening to your voicemails,
you hear two separate messages.

Alternatively, consider a machine that instead appends the second voicemail the
first as one large piece of data.
When you listen to your voicemails on this machine,
you grab the message in sound-bites from that one large piece of data,
where the sound-bites do not necessarily line up with the original messages.

Which of these scenarios is more similar to TCP,
and which is more similar to UDP?

4. If my client encodes strings using UTF-16 and my server decodes them using
ASCII,
will this be a problem?
Why or why not?
(This is not a question about those two particular encodings.)

5. Consider the following simple protocol.
* A client greets a server with the message `hello`
* The server resonds with a greeting
* The client then sends two integers separated by a space; e.g., `5 4`
* The server responds with a message indicating whether the first number is
  less than the second
* If the client does first not properly greet the server,
  the server will not answer the client's question about the numbers.
* A new greeting must be sent before each pair of numbers.
* The protocol runs over UDP

During the discussion section,
there will be an implementation of the server side of this protocol running on
DataComm.
* Write client code that allows you to interact with this server and displays
  the server responses.
  This code can actually interact with my server if you run it on the DataComm
  computers via `cislab.hpc.gvsu.edu`.
* Try out a few interactions with the server,
  including ones that do not follow the typical protocol
* Your client code can be *very* similar to the example code in the course
  repository under `misc/socket-examples/udp`.

If you want to try this on your own time,
the server code is included in the `code/` subdirectory of the activities.
However, you should be able to write your client without needing to look at the
server code.

6. You probably wrote the client code in Python,
which is the same language the server was written in.
Is it possible for a client written in another language,
such as Java,
to interact with my Python server?
If so,
what special changes would you need to make to account for the differences
in languages, if any?
If not, why not?

7. If you are running on DataComm,
you can see your IP address using the command `ip addr`.
Look for an output named `enp0...` and a section `inet:` underneath it.
The number after that label is your IP address (ignore the `/24`).
Is this the same IP address that the server is running on?
Does it need to be?

8. The protocol uses UDP for simplicity,
but there are significant downsides to this given the way the protocol works.
(You may have run into issues because of this when testing out the protocol
during the class period.)
Why would TCP be a better choice of transport-layer protocol for supporting
this application-layer protocol?

9. If you were able to write the client,
you probably found that it didn't really do much.
Next, upgrade it so that the client program takes care of the greeting part for
you.
That is,
you simply enter a pair of numbers and the client handles the "handshake" with
the server without you needing to do anything as the user.

10. We almost certainly will not have time for this in class,
but if you are looking for a few extra ways to test yourself:
* Write the server side of the program.
  You should be able to test it using your own client.
  Let me know if you have trouble getting it set up and listening on a
  DataComm computer.
* Write a client and server for a similar protocol that runs over TCP.
* Create your own simple protocol with a friend and have one of you write the
  client and the other write the server.
  Try running them on different hosts on DataComm and see if you were
  successful in implementing your protocol.

11. HTTP and SMTP both run over TCP.
However, those two protocols have substantial differences in the messages they
send.
How do these differences affect the transport-layer headers?

12. If UDP were to change the way it computed a checksum,
would routers on the internet need to be updated accordingly?
If so, how?
If not, why not?

13. When a simple application message,
such as an HTTP GET request,
is sent from a client to a server,
is the message largest when it is
* an application-layer message,
* a transport-layer segment, or
* a network-layer datagram?
Why?

14. We will study encryption later,
but a simple understanding is that it allows messages to be passed privately
between processes even in the presence of eavesdroppers.
Why might it be helpful to provide encryption at the transport layer rather
than the application layer?
What downsides might there be?

15. Assume an internet-connected host runs just one networked application.
For example, this host is only a web server.
Since there is no problem distinguishing which application messages are being
sent to,
can this server get by without implementing transport-layer protocols?
Why or why not?

16. What is the purpose of port numbers?
How do they differ from IP addresses?

17. Servers generally listen on well-known port numbers,
such as port 80 for an HTTP server.
Why do clients not need to send from well-known numbers?

18. If I know a TCP segment was sent to (192.168.3.1, 80),
is that enough information to specify which socket it goes to?
Why or why not?

19. In UDP, only the destination IP and port are necessary to specify a socket.
If two clients send UDP segments to the same (IP, port) pair,
why are they not interfering with one another's connections?

20. Why might using UDP as the transport protocol for a video streaming service
be frowned upon by others on the network?

21. Consider a socket that is set up to listen for incoming messages.
In UDP, if another host contacts that socket with an application-layer message,
that socket can reply directly.
In TCP, this is not possible.
What is the extra step that is required?

22. My office is in Mackinac Hall in room D-2-212.
If I were a networked process,
what would you way were my "port number" and "IP address"?

23. Ethernet is a link-layer protocol that provides error detection at the link
level.
If my computer is connected to my router via Ethernet,
why might a UDP checksum still prove helpful?

24. At the receiving host,
the sum of 16-bit words in a message is
```
0110011001100000
```
and the UDP checksum is
```
0001100110011111
```
Did an error occur in the transmission?

What if the UDP checksum were
```
1001100110011111
```

25. The UDP header reserves 16 bits each for storing the source port,
destination port, length, and checksum.
Given this, what is the maximum number of ports available when communicating
over UDP?
How can you tell?

26. Consider drawing a FSM for an HTTP server.
What aspect of the HTTP protocol will make this a rather plain FSM?
Try actually drawing the simple FSM assuming the server only ever responds
with `200 OK`, `304 Not modified`, or `404 Not found`.

27. Consider the client and server from the simple protocol we programmed in a
previous example.
Draw FSMs describing the behavior of both.

28. You are giving directions to a friend over the phone,
such as "turn left, then right, then drive two blocks..."
After every step they say "yeah", or "uh-huh", or similar.
If they instead say "wait, what was that?",
then you repeat the last step.
What networking tool are you and your friend using to ensure you have reliable
communication?

29. Imagine you are in the scenario above,
but your friend does not respond after you say "turn right".
Assuming they did not hear you,
you repeat that step.
What problem might your friend run into?
How does this relate to computer networks,
and what tool do networks use to solve this particular problem?
How could you and your friend do something similar over the phone?

