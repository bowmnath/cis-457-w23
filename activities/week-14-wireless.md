# General Questions

1. What is an ad-hoc network?
   How does it differ from most of the wireless networks we discuss?

2. If a network has a low signal-to-noise ratio (SNR),
   should it use a high-bitrate or low-bitrate modulation scheme?

3. Consider a host using CDMA with the following chipping sequence:
   ```
   A: 1  1  -1 -1
   ```

   If the host wants to send the bit `1`,
   what does the receiver receive for that time slot?
   I am asking specifically for a sequence of four values,
   not for the eventual `1` that the receiver should be able to figure out.
   For example,
   ```
   2 2 2 2
   ```

4. Consider a host using CDMA with the following chipping sequence:
   ```
   A: -1  1  -1 -1
   ```

   If the receiver recieves the following values,
   what bit does the receiver believe was sent?
   ```
   1  -1  1  1
   ```

5. Consider hosts A and B using CDMA with the following chipping sequences:
   ```
   A: 1  1  1 -1  1 -1 -1  1
   B: 1 -1  1  1  1 -1  1 -1
   ```

   A receiver receives the following signal in one time slot:
   ```
   2 0 2 0 2 -2 0 0
   ```
   What was the bit sent by A?
   What was the bit sent by B?

6. Consider hosts A and B using CDMA with the following chipping sequences:
   ```
   A: 1 -1  1  1  1 -1 -1  1
   B: 1 -1  1  1  1 -1  1 -1
   ```

   A receiver receives the following signal in one time slot:
   ```
   0  0  0  0  0  0 -2  2
   ```
   Try recovering the bit sent by A.
   You should get a strange result.
   What do you think happened?

7. Assume you are renting a house with an upstairs neighbor.
   The two of you are using separate 802.11 wireless networks,
   and they keep interfering with one another so that neither of you gets
   a strong internet connection.
   You both believe that the only way to settle this is with bloodshed.
   As you are girding yourselves for the battle to decide which of you gets to
   keep their wireless network,
   a wise 457 student stops you and claims that there is a way you can *both*
   have strong wireless connections that do not interfere with one another.
   What do you think the student has in mind?

8. For a host trying to connect to an 802.11 network,
   active scanning requires sending more frames (why?) but will generally
   result in a shorter total time before joining the network.
   Why?

9. Is it possible for two hosts that are connected to different access points
   to be on the same subnet?
   Why or why not?

10. Consider visiting a corn maze with a friend.
    The two of you get separated at some point and cannot see one another.
    It is getting dark,
    and there are some ominous-looking children wandering around,
    so you decide it is time to leave,
    and you shout to your friend at the top of your voice to get their
    attention.
    Unfortunately, at the exact same time,
    your friend decides to shout to you.
    You are very far away in the maze,
    so not only do you not hear what one another said,
    you do not even realize that the other shouted because their voice is so
    faint compared to your own.
    At this point,
    you believe your friend cannot hear you or chose not to respond.

    As you are driving home in a rush without your friend,
    you ponder how the problem you encountered relates to computer networking.
    In particular, how does it relate to medium-access protocols?

11. If a wireless sender could send and receive at the same time,
    would this allow collision detection to be effective in a wireless setting?
    Why or why not?

12. What is a beacon frame in an 802.11 network and what purpose does it serve?

13. Why do you think a CSMA/CA sender initiates a random backoff when it senses
    the channel it wants to send on is busy?
    Why not simply wait for a DIFS after the channel becomes not busy and then
    send?

14. A SIFS (the time interval before a host is allowed to send an ACK)
    is shorter than a DIFS
    (the time interval before a host is allowed to send a new frame).
    This essentially gives ACKs priority over other traffic.
    Why was the protocol designed this way?

15. Consider both CSMA/CD and CSMA/CA.
    For each of these protocols,
    state whether each of the following conditions would cause an exponential
    backoff.
    Some of these do not make sense for one of the protocols --
    if that is the case, explain why.
    * Sender has data to send, but senses channel is busy
    * Sender detects collision while sending frame
    * ACK is not received after sending frame

16. Your friend is adding request-to-send and clear-to-send to their wireless
    networking protocol because they want to decrease the number of collisions
    on the network.
    Is your friend's idea going to work?
    Why or why not?

17. To get all the way from a wireless host to a router,
    a packet will go through both an 802.11 frame and an 802.3 frame.
    Why?

18. Why do 802.11 frames include sequence numbers when 802.3 (Ethernet) frames
    do not?

19. You are walking down the hallway and see your professor,
    and you are hoping to ask a question about your project.
    At the same time,
    you see another student from your class approaching the professor.
    Rather than dive right in to the question,
    you say "Excuse me, professor?",
    to make sure that you get to ask first.
    Only once she responds to you do you ask your actual question,
    and the other person waits to ask theirs.
    What optional feature of wireless networking are you taking advantage of
    in this case?
    Although it is polite in human interaction,
    why is it not particularly helpful from a technical perspective in this
    scenario?

20. Assume a wireless host has MAC address 11:22:33:44:55:66.
    The addresses in an 802.11 frame are, in the following order,
    * AA:BB:CC:DD:EE:FF
    * 11:22:33:44:55:66
    * 12:34:56:78:9A:BC

    What is the MAC address of the router?
    Is this frame going from router to host or host to router?

21. If a network is not particularly busy,
    what is a downside to a request-to-send and clear-to-send setup?

22. Consider a host that changes access points but remains on the same subnet.
    Which of the following change?
    * IP address of host
    * MAC address of host
    * MAC address of associated access point
    * MAC address of router

23. Does a router send frames that have an access point's MAC address as their
    destination?
    Why or why not?

24. Explain how a wireless host that is not very active
    (i.e., does not send or receive very many packets)
    can save battery life.
