# General Questions

1. Consider a fast-food drive through lane.
For much of the day,
the drive-through is nearly empty.
Around noon and five o'clock,
the line suddenly becomes very long,
and then eventually dies down again after an hour or so.
If this lane were a link on a network,
would the network be packet-switched or circuit-switched?
How can you tell?

2. To alleviate the crowding issue,
the restaurant emails all of its customers and assigns them a 2-minute time
slot at some point in the day.
The customer is allowed to visit the drive-through at only this point in time.
What are the upsides and downsides to this idea?
How does this relate to networking?

3. Is it easier to provide a minimum bandwidth guarantee in a packet-switched
or a circuit-switched network?
Why?

4. How do two hosts reserve bandwidth ahead of time in a packet-switched
network?

5. The city of Bigsburgh has a six-lane highway running through it.
The residents are grumpy that out-of-state drivers cause a lot of congestion,
so they pass a law stating that Bigsburghians drive only in the left three
lanes and all other drivers are in the right three lanes.
Is this example most closetly related to packet-switching,
circuit-switching with FDM,
or circuit-switching with TDM?
Explain.

6. In which type of network, packet-switched or circuit-switched,
are queueing delays usually more of an issue?
Why?

7. Describe the difference between time-division and frequency-division
multiplexing.
Try to give real-life examples of each.

8. For a given set of sending hosts,
is it ever possible for a packet-switched network to have a lower utilization
than a circuit-switched network?
If so,
give an example.
Otherwise, explain why not.

In the next two questions, assume the network under consideration is
circuit-switched and uses TDM.

9. If there are 5 hosts sharing a 1 Mbps link
and 4 of the hosts are almost always idle,
what is the effective transmission rate of the host that is sending?

10. In the above question,
what percent of the time is the link idle?

11. If there are 5 hosts sharing a 1 Mbps link on a **packet-switched** network
and 4 of the hosts are almost always idle,
what is the effective transmission rate of the host that is sending?

12. In general,
describe a worst-case sending pattern for circuit-switched networks in terms
of resource utilization.
Then, describe a best-case pattern.

13. When a packet moves from the input interface of a router to an output
interface,
this is... (forwarding or routing)?

14. List a few kinds of guarantees that could be provided by a network layer.
What guarantees are provided by the internet's network layer?

15. What are some possible benefits of the internet's no-frills network service
model?

16. Where would queueing delays most likely occur in a router under each of the
following circumstances?
(Some of these may not result in excessive queueing at all.)
* The switching fabric is significantly slower than the input ports
* The switching fabric is significantly faster than the input ports
* The routing is done by a single routing processor instead of locally on each
  port

17. You are in an airport on your way to Tokyo.
You come to an intersection with three signs:
* Left: Flights to Europe
* Straight ahead: Flights to Japan
* Right: Flights to Asia

More than one of these signs may seem relevent to you.
Which one do you follow?
What does this have to do with forwarding or routing?

18. Consider the following routing table.
```
Destination address range           | Link interface
---                                 | ---
10100010 XXXXXXXX XXXXXXXX XXXXXXXX | 0
10100011 XXXXXXXX XXXXXXXX XXXXXXXX | 1
10100011 111XXXXX XXXXXXXX XXXXXXXX | 2
otherwise                           | 3
```
Give the link interface for each of the following addresses:
* 162.224.0.1
* 162.3.2.1
* 161.3.2.1
* 161.253.2.1
* 163.253.2.1

Note: `10100010b = 162`, `10100011b = 163`, and `11100000b = 224`.

19. Given a destination IP `dest` and a list `forwards` containing
`(IP prefix, link interface)` pairs,
write pseudocode for how you would determine the link interface to send `dest`
out.
(This can be fairly rough pseudocode because we have a limited amount of time.)
How long does your code take to run?
Based on this,
how much benefit do you think there is to a router to have something like TCAM
(special hardware designed to find a longest-prefix match)?

20. In lecture, you learned about destination-based vs generalized forwarding.
What are some concerns other than its destination that might affect how a
packet is forwarded?

21. Imagine you are stuck at a stop sign.
You want to turn right, and you are behind someone turning left.
The road is very busy with right-to-left traffic,
and the left-to-right direction is completely clear.
Something very similar to this frustrating scenario can happen inside routers.
Explain when this can happen and what term we use for it.

For the next few questions,
consider the following scenario.
A major city has decided to save money by replacing its postal service with
a distributed service that calls on many citizens to play their part.
The city is laid out on a perfect grid,
and at each intersection is a citizen-postmaster.
The system works as follows:
* each morning, the chief postmaster creates a set of personalized instructions
  for every citizen-postmaster
* when they have a letter to pass on,
  a citizen-postmaster will consult their instructions to decide which of the
  four neighboring intersections to run it to
* because postmasters are often away from their intersections,
  each has a designated table at their intersection for incoming mail to be
  placed on

22. Which of these can afford to take longer:
* a chief postmaster deciding on a citizen-postmaster's instructions, or
* a citizen-postmaster deciding which intersection to run to next?

What does this say about the relative speed requirements of the data and
control planes on the internet?

23. A citizen-postmaster is clearly meant to be a router.
What aspects does a citizen-postmaster share with a router?
(I.e., map the parts of their job to the parts of a router).
Some features found in routers do not exist in the above scenario.

24. There is a critical inefficiency in the above scenario compared to how
forwarding would be done in an actual router
(and I don't just mean the fact that it involves humans).
What makes the forwarding process as described above so inefficient?
(Your answer to the previous question may be helpful here.)
If you had the budget for more employees,
how could you modify the scenario to make it more resemble an actual router
that performs efficient forwarding?

25. Assume a router has 5 input ports and 5 output ports.
What is the maximum number of packets that can be moved across the switching
fabric at once using
* a bus?
* a crossbar?

26. Router A is connected to several extremely busy links.
Router B, which has the same hardware as Router A,
is connected to links that are not very busy.
* For which router, if either, is the queuing policy more important?
* If we remove the assumption that the routers have the same hardware,
  how might that change the answer, if at all?

For the next few questions, assume five packets arrive in the queue of an
output port of a router at roughly the same time.
We refer to the packets simply as 1, 2, 3, 4, 5, based on the order of their
arrival.

27. How will the packets be scheduled using priority scheduling if odd-numbered
packets are high-priority and even-numbered packets are low-priority?

28. How will the packets be scheduled using round robin scheduling if
packets 1 and 4 are one class and packets 2, 3, and 5 are another class?

29. How will the packets be scheduled using weighted fair queuing if
* odd packets are one class and even packets are another, and
* the odd packets get 2/3 of the time (i.e., a 2:1 ratio)?

30. The professor generally walks around the classroom group-by-group and asks
members of the particular group whether they have any questions.
If this were the only way for questions to be asked of the professor,
what type of scheduling would this most remind you of?

31. If, completely hypothetically, one group rarely asked questions,
the professor might spend more time moving between the other groups and only
occaisionally stop by that group.
What queuing setup would this remind you of?
