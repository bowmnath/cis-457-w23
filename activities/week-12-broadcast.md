# General Questions

<!--
1. Give an example of a human protocol for sharing a broadcast medium
   (e.g., the air when we speak).

2. Would your example be most similar to a channel partitioning, random access,
   or turn-taking protocol?
-->

1. Rank the following from worst to best scenarios for using a channel
   partitioning scheme.
   (You can rank some as a tie if they are roughly equivalent.)
   * Many senders, almost all sending
   * Few senders, almost all sending
   * Many senders, only one sending
   * Few senders, only one sending

2. What is the major downside to random access protocols?

3. We often use human analogies for medium access protocols.
   In regular conversation,
   do people use "carrier sense" as part of their protocols?
   If so, what would it look like if they did not use carrier sense?
   If not, how would things change if they did use carrier sense?

4. Finish the sentence:
   A random access protocol will be the most effective type of protocol when...

5. In slotted ALOHA with `p = 0.5`,
   assume two senders send in the same slot,
   leading to a collision.
   What is the probability that there will be a collision between those senders
   in the next slot?
   What is the probability that the next slot will be wasted
   (either neither sends or both send)?

6. What is the purpose of the slots in slotted ALOHA
   (i.e., why are they beneficial)?
   What is a possible downside to using slots?

7. Another 457 student tells you the following:

   When many hosts are connected to a link that is shared with the slotted
   ALOHA protocol,
   the effective rate of the link is much lower than the maximum rate.

   This is almost true,
   but it is imprecise (or makes a hidden assumption).
   What would you need to change about the statement to make it true?

8. A friend and I are at a party discussing our favorite networking protocols.
   While she explains TCP,
   I listen politely.
   Once she is finished,
   I expound on the beauty of IP,
   and she waits for me to say my piece.
   Then, since neither of us is talking,
   we both start speaking at the same time about other protocols.
   Once we have started,
   neither of us stops talking until we have finished our explanation.
   Sadly, nobody can really understand what either of us is saying,
   and they all use it as an excuse to leave and find more interesting
   conversations.

   What useful feature of a medium-access protocol were my friend and I
   missing?

9. Why can collisions still occur when nodes are listening before they send?
   Is this more likely to occur with nodes that are near one another or far
   from one another?

10. What is wrong with the following description?

    Adding collision detection to CSMA increases efficiency by reducing the
    number of collisions between transmitting nodes.

11. Why is the backoff interval after a collision usually chosen randomly?

12. What is exponential backoff?
    Why can it be better than using a fixed set of choices for backoff
    intervals?

13. Assume two CSMA/CD senders have had three collisions in a row with one
    another (and neither has experienced a previous collision).
    What is the probability that they collide with each other a fourth time in
    a row?

14. There is a major downside to channel-partitioning schemes
    (what is it?).
    If you were trying to make a simple improvement to them to get around this,
    what would it look like?
    Does your solution resemble any schemes we have discussed in class?

15. How are turn-taking protocols (e.g., polling) similar to TDMA?
    How are they different?

16. Imagine a classroom in which the professor is concerned about shy students.
    Every few minutes,
    she calls on each student in turn whether or not they have a question.
    If the student has a question,
    they ask it.
    Otherwise, they just say "pass."
    What are some upsides and downsides to this scheme?
    What networking idea does this remind you of? 

17. You and your friends argue a lot,
    so you have decided to make your conversations more civil by ensuring
    nobody talks over anyone else.
    To do so,
    you design a glamorous Speaker Sash,
    and promise that you will never speak in one another's presence unless
    you are wearing the sash.
    At the next party,
    your friend Eleanor really likes the sash,
    so she puts it on and leaves the party.
    What is the problem here?
    How can something similar arise in a medium-access control protocol?

18. You decide that polling is a bad idea because the controller will poll
    other hosts even when those hosts have nothing to say.
    You decide instead to have hosts announce when they would like control
    of the medium.
    Why might this idea lead to more complications than polling?

19. Your friend believes that turn-taking protocols are almost meant to be
    hybrids of the other two kinds.
    He claims that turn-taking protocols work better in many cases,
    but that they don't do as well as the other protocols in extreme cases,
    such as having just one sender.
    Do you agree or disagree?

20. Assume my name is Inigo.
    Whether I am visiting the store,
    reading at the library,
    or watching TV at home,
    my name is still Inigo.
    Even if I move homes to a different address,
    my name is still Inigo.
    What is the corresponding idea in networking?
    This is example is very different from that idea in at least one key way --
    what is it?

21. Compared to an IP address, a MAC address gives {more, less} information
    about a node's location.

22. To avoid bias in exam grading,
    a professor asks all students to write down their student ID numbers rather
    than their names at the top of the exam.
    Then, when returning exams, the professor simply calls out to the whole
    class, for example,
    "Who is 457158357?"
    and the corresponding student will reply with their name so the professor
    can hand them the exam.

    What networking protocol is the professor making use of here?
    If the professor has a very good memory,
    why might this system not be effective in the long term for avoiding bias?

23. In the example above,
    is there a TTL to the information you are gathering?

24. Assume host `A` is on one network and host `B` is on a different network
    that is several hops away.
    Which of the following change during a packet's journey from `A` to `B`?
    (There is more than one possible answer depending on what assumptions you
    make.)
    * Source IP address
    * Destination IP address
    * Source MAC address
    * Destination MAC address
