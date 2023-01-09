# General Questions

1. What mechanism is used to detect corrupt packets in TCP?

2. What mechanism is used to detect lost packets in TCP?

3. Can you think of any other way to detect lost packets than the mechanism
described in (2)?
If so, explain.
If not, why not?

4. Describe what is meant by a "stop-and-wait" protocol.

5. Assume there is a communication channel that does *not* corrupt packets,
but that may lose packets.
If a stop-and-wait protocol is employed,
are sequence numbers necessary?
If so, come up with a scenario where the protocol would fail without sequence
numbers.
If not, explain why not.

For the next few questions,
imagine you have a one-sided pen pal,
someone with whom you exchange written letters on a regular basis.
You tend to send them long letters,
and they usually just reply letting you know that they got your letter.
However, you and your pen pal are concerned about the quality of the postal
service in your country.
The sometimes lose letters,
and they sometimes drop them in water so parts of the letters are unreadable.

6. Assume you never send more than one consecutive letter without hearing a
reply from your friend.
Describe how you and your friend could be sure that all of your letters
are eventually arriving at their house safely and correctly.
Consider using a finite-state machine to describe your process.

7. If it generally takes three days for your letters to reach your friend,
how frequently can you send letters using the protocol you described above?

8. What if you did not limit yourself to one outstanding letter at a time?
Consider the situation in which you would like to send them daily news.
If you were instead willing to have three unanswered letters out at once,
would this be enough to allow you to send daily news?
Why or why not?

9. What complications might arise if you had three unanswered letters out at
once?
Consider your protocol from (6).
Would it be able to handle all possible failure cases
(lost and corrupted letters, etc.)?
If so,
explain how.
If it needs to be modified,
suggest modifications.

10. Assume you have started numbering your letters to your pen pal.
If the pen pal receives letters 1, 2, and 4 in that order,
they immediately burn letter 4 and discard the ashes without reading it.
Which type of pipelined protocol is your pen pal using?

For the next two questions, assume the following scenario:
Using GBN with a window size of 5, a sender sends packets 1 - 5.
The sender recieves just one ACK, and the ACK is for packet 3.

11. Which packet(s) will be re-sent?

12. What is the current window for the sender?

13. In lecture, our assumption was that packets would not "switch order" in
the network.
That is, if packet A is sent before packet B,
packet A will arrive before packet B unless packet A is lost.
If we get rid of this assumption,
do we need to make any changes to rdt3.0 to account for it?
If so, describe the changes.
If not, explain why.

14. Assume a sender has recently received ACKs for packets with sequence
numbers 1, 3, and 5.
A timeout then occurs,
and the sender resends a packet with sequence number 2.
You may assume the sender has a few hundred sequence numbers available to it.
Is this enough information to determine whether the protocol in use is SR or
GBN?
If so, which protocol is in use?
If not, what other information would you need?

15. Which will benefit more from pipelined data transfer:
* connection with low latency and high transmission rate, or
* connection with high latency and high transmission rate?

Why?

16. Assume a receiver has a very small receive buffer.
Which protocol would likely be a better fit: GBN or SR?
Why?

17. Assume we have a channel that we know will frequently reorder packets,
but that dropping packets is very rare.
Which type of pipelined protocol that we have discussed would be a better fit
for this channel?
Why?

18. Assume an SR sender has a window size of 5 and sequence numbers [0 - 7].
Explain why this combination of sequence numbers and window size would not work
using an example.
I.e., come up with a scenario in which the receiver does not know whether it is
receiving new or old data.

19. Assume the same scenario as the previous problem,
but using GBN instead of SR.
Could the same problem arise?
Why or why not?

20. We learned in leture that if we have a window of size N in SR,
then we need at least 2N sequence numbers to be safe.
Draw a diagram (or a few diagrams) showing possible sender and receiver windows
that explains why this is the case.

# TCP Questions

21. Assume a TCP sender sends packets 1 - 5 and receives ACKs for 1, 4, and 5.
What packet(s) will be re-sent after the next timeout?

22. Assume a TCP sender sends packets 1 - 5 and receives ACKs for 1 and 2.
What packet(s) will be re-sent after the next timeout?

23. Why is a server generally able to handle more UDP clients at once than TCP
clients?

24. Consider the pen pal story above,
but you and your pen pal started numbering your letters to one another.
Each envelope has a number that represents the entire letter,
starting at 1, then 2, and so on.
How is this somewhat different from sequence numbers in TCP?
(There are a few differences.)

25. Consider the pen pal scenario again,
but your pal has decided to start writing more detailed messages of their own.
While finishing up writing you a letter,
they receive a letter from you.
In keeping with how you did things previously,
they send you a brief response acknowledging your letter.
Then, they mail a letter containing their own news.
How does this differ from the way things are done in TCP?

26. What, if anything, does a network do differently to support a
connection-oriented protocol like TCP vs a connection-less protocol like UDP?

27. Which of the following limit the maximum size of a TCP segment?
(There may be more than one.)
* The maximum size of an application message
* The maximum size of a network datagram
* The maximum size of a link frame

28. A TCP client sends a segment with sequence number 1000 and size 500,
and the server replies with a segment of size 800.
When the sender sends its next segment,
what will the sequence number be?

29. In the previous example,
the server would also use its reply to ACK the first segment from the sender.
What would the ACK number be?

30. Assume the expected RTT is computed using the formula from
[the slides](https://github.com/bowmnath/cis-457-w21/blob/master/slides/tr-tcp-ack.pdf)
with `a = 0.125` and that the initial estimation for RTT is 0.5 second.
The next two samples are 0.5 and 1 second, respectively.
* What is the new expected RTT?
* Would the expected RTT be different if the order of the two samples were
  switched?

31. Why do we bother computing expected RTT in the first place?
What other related value do we compute, and why?

32. Compute expected RTT using the exponentially weighted moving average
formula where
* The initial estimation is 1 second
* The next four samples are 1 second, 2 seconds, 2 seconds, and 1 second
* The parameter `a` is not given --
  simply leave it as `a` in your final answer.

Distribute terms in your answer
(i.e., change things like `x(y + z)` to `xy + xz`)
until you do not have any parentheses left.
Based on what you find,
is it clear why the average is called "exponentially weighted"?

33. In the description of the TCP receiver from the slides,
the receiver will wait up to 500 milliseconds after receiving an expected
packet before sending the ACK.
However, if it receives another expected packet in that time,
it will immediately send an ACK for the more recently received packet.
Explain why both of these behaviors are helpful for reducing the total amount
of data transmitted.
In particular,
explain why the receiver does not continue to wait after receiving the second
packet.

34. Consider a TCP sender sending three packets out at once into a lossy
channel.
Give an example timing diagram
(a rough diagram showing when packets are sent, received, or lost)
showing where a short timeout can be helpful,
and one showing where a short timeout can be harmful.
