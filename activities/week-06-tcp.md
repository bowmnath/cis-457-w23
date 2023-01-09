# General Questions

1. Explain why flow control is used in TCP and how it differs from congestion
control.

2. A professor is giving a student papers to read as part of a project.
The student has a mental limit to how many papers they can have at once that
they have not read;
if this limit is exceeded, they get really freaked out.
The student and professor implement the following system for staying not
freaked out:
* The professor sends the student papers via intra-office mail.
* The student reads the papers in the order they were sent.
* Whenever the student finishes a paper,
  they send an email saying which paper they just read and how many more unread
  papers they can have right now while maintaining their sanity.

Using this system
the professor sends five papers.
They then get an email from the student saying the first paper is read and that
the student can handle four more unread than they have.
The professor then sends the student three more papers via the intra-office
mail.

Is there any way in which the student could be overworked in this scenario?
If so, how?
If not, explain how the protocol has prevented it.

3. Consider a TCP sender that has received a receive window value from a TCP
receiver.
For each of the scenarios below,
consider whether the scenario is possible.
If so, give an example of how it could occur.
If not, explain why it is not possible.
* The TCP receiver has more free buffer space than the receive window
  indicates.
* The TCP receiver has exactly the amount of free buffer space that the receive
  window indicates.
* The TCP receiver has less free buffer space than the receive window
  indicates.

4. Is it necessary for the receiver to indicate its free buffer space in
every segment?
Or, could the designers of TCP have made the receiver simply send its free
buffer space as part of the handshake and allowed the sender to keep track of
what it had sent and the corresponding amount of free space at the receiver?
Why or why not?

5. The formula for determining whether a host can send data into the TCP
connection based on flow control is
```
LastByteSent - LastByteAcked <= rwnd
```
Explain in your own words
* what the left-hand side of the formula means,
* what the right-hand side of the formula means, and
* how this formula works to institute flow control.

6. Does the above formula apply to flow control in UDP?
Why or why not?

7. Consider a TCP sender that is trying very hard to be polite.
If the receive window in an ACK is 0,
the TCP sender will not send any segments of any kind until it gets a
notification that the receive window is no longer 0.
This is a deviation from the actual TCP protocol as discussed in lecture.
How is it different?
What issue could this cause?

8. TCP connections begin with a three-way handshake.
If it takes 5 seconds for a message to get between two hosts,
what is the overhead in terms of time of the TCP handshake?
You may ignore transmission delay and consider only propagation delay.

9. When closing a TCP connection,
the host that sends the final segment
(an ACK to the final FIN)
waits for a period of time before actually closing the connection.
Why is this done (i.e., what problem could arise if it were not done)?
If this step were skipped,
would there be any way for the other side to close the connection?

10. Imagine you live next door to someone who runs a business out of their
place,
and that people frequently get the wrong address and knock on your door.
You have two options when this happens.
You can
* ignore the person entirely and hope they go away, or
* tell them that they are in the wrong spot.

If you tell them they are in the wrong spot,
what would be the equivalent kind of TCP message?
What might be the benefits and drawbacks of doing so?

11. Describe the similarities and differences in the mechanism for
rate-limiting in flow control vs congestion control.

12. Why is a triple duplicate ACK treated differently than a timeout for
purposes of congestion control?

13. If they decide to deviate from TCP's congestion control policies,
which of the following parties can "break" TCP's congestion control
(cause an unreasonable amount of data to be sent into the network)
on a network shared by several hosts:
* A single sender acting on its own
* A single receiver acting on its own
* A single sender-receiver pair acting together

For each of the above,
explain how or explain why it is not possible.

14. Even if congestion is not bad enough that packets are dropped,
a TCP sender will grow its window faster in an uncongested network than a
congested one.
Why?
(Hint: why is TCP called "self-clocking"?)

15. Consider an office with an overworked secretary who sometimes takes a while
to send memos along to clients and sometimes forgets to send them at all.
You know from experience that if they are bombarded with memos,
they will get flustered and it will just take them longer to send the memos
along.
* Scenario A: You give the secretary three memos to send to a single client.
  The next day, you have not heard anything back from the client.
* Scenario B: You give the secretary three memos for a client.
  The next day,
  you have a letter from the client complaining that the two memos you sent
  don't make any sense and that there is clearly missing information.

If you have several more memos you need sent,
are you better off in Scenario A or Scenario B?
Why?

How does this relate to congestion control?

16. A TCP sender with no current outstanding packets sends out 4 packets,
waits one RTT,
then sends out 8 packets.
If you assume they are not in the Fast Recovery state,
which of the following is true:
* they are most likely in the Slow Start state;
* they are most likely in the Congestion Avoidance state;
* they are equally likely to be in the Slow Start or Congestion Avoidance
  states?

17. If a TCP sender receives an ACK and increases its congestion window by
the size of one packet,
which of the three states might it be in?

You may want to look at the FSM diagram for the next few questions if you have
not already been referencing it.

18. TCP Senders A and B have the same current congestion window.
Sender A suffers a timeout,
and Sender B has a triple-duplicate ACK.
Which one, if either, has the higher value of `ssthresh`?

19. The current congestion window for a sender is 15 packets.
If the sender is in Congestion Avoidance,
how many ACKs must they receive before their window is 17 packets?

20. Even though the first phase of congestion avoidance is called
"Slow Start",
a sender generally will not spend much time there.
Why not?

21. Imagine you want five pieces of furniture from a store that is one hour
away.
Your car is large enough to fit just one piece of furniture at a time.
Consider the following two scenarios for obtaining the furniture.
* Scenario A: You drive out to the furniture store and take the pieces away
  one at a time,
  resulting in several trips to the far-away store.
* Scenario B: A local branch of the store offers to get the items for you.
  This branch is just five minutes away from you
  (and 55 minutes from the other store).
  They do not drive any faster than you,
  but they can fit all five pieces into their truck.
  However, they will only bring them to their store --
  they do not deliver to your house.

How long does it take to get all of the furniture home in Scenario A?
In Scenario B?

22. The scenario above is not a perfect metaphor for TCP because the furniture
store did not require a "handshake".
What would a TCP-style handshake look like in the fictional scenario above,
and how would it effect the times of the two scenarios?

23. What TCP topic do the previous questions remind you of?

24. The topic above is somewhat different from caching.
How is this scenario different?
What would caching look like in our made-up furniture example?
