# General Questions

1. Although ICMP runs on top of IP,
   it is not considered part of the transport layer.
   Why not?

2. Why is it helpful that ICMP does not run on top of TCP or UDP?

3. In a post-apocalyptic wasteland with no Google maps but plenty of gasoline,
   you are trying to create a map of the route from your town to a distant
   city.
   You send out a driver with an eigth of a tank of gas,
   and when they have burned through half of it they come back and tell you
   the furthest point they reached.
   Then you send out a driver with a quarter of a tank of gas,
   and they follow the same procedure.
   You keep doing this until you send out a driver who reports back that they
   successfully reached the city.
   What networking tool have you recreated?
   Are there any significant differences from the actual tool?

4. What is the general purpose of ICMP
   (i.e., why does it exist)?

5. What is the difference between SNMP in request/response mode vs trap mode?
   (The purpose, not the header information.)

6. Give an analogy to explain the difference between the link and network
   layers.
   One that is at least slightly different from the analogy in the lecture
   video would be preferable.

7. What is the "payload" of a link-layer frame
   (i.e., what "data" does it contain)?

8. Which of the following need to run link layer protocols?
    * Gateway router
    * Backbone router
    * Host running a Web client
    * Host running a Web server

9. Error detection and correction have somewhat obvious upsides.
   What are some downsides to error detection and/or correction?

10. You and your friend are trying to play a game of chess over the phone
    because you wanted to make a convenient metaphor for your networking
    professor.
    You tell them your moves (e.g., "knight to A-3") and they arrange the
    pieces on the board.
    You used to play over a land-line,
    and you never bothered to repeat yourself.
    One day you decide to move to walkie-talkies to save on your phone bill,
    and your friend starts reading back every move to you to make sure they
    heard you correctly.
    What does this have to do with link-layer protocols?

11. Pizza Shack wants to be environmentally friendly,
    so they don't have delivery drivers.
    Instead, they post a delivery runner at every intersection,
    and each runner will pass the pizza along to the next runner so that nobody
    needs to run too far.

    Unfortunately, all of the jostling of the pizzas is leading to a lot of
    complaints from customers who open their boxes to find smashed food.
    To solve this,
    Pizza Shack trains all of their runners in pizza surgery.
    When a pizza arrives at a runner,
    they will check it for smashedness and repair the pizza if necessary.

    What are some upsides and downsides to this system?

12. In networking terms,
    how would different layers have come into play in the previous example?

13. Consider the high-level description of error detection below.
    What is wrong with this description?

    The sender appends extra bits to the message according to some agreed-upon
    rule.
    The receiver receives the original message plus the extra bits.
    It then runs an algorithm to determine whether the received versions of the
    message and extra bits match.
    If the receiver confirms the received frame is identical to the original,
    it passes the payload up to the next layer.
    Otherwise, it discards the frame.

14. Consider parity-checking system where parity bit ensures sum is odd.
    A sender sends the following (`message | parity bit`).

    ```
    11001100 | 1
    ```

    If the receiver receives the following, what happens?

    ```
    11000000 | 1
    ````

15. Assume we are using a two-dimensional parity where the parity bit ensures
    the sum is odd.
    (Note that this is different from the two-dimensional parity scheme
    described in the slides.)
    The received message below contains a single bit error.
    Correct the error.

    ```
    1 1 0 0 | 1
    0 0 1 0 | 0
    1 1 1 0 | 1
    1 1 1 1 | 1
    -----------
    0 1 0 0 | 0
    ```

16. Using a cyclic redundancy check with the generator `1101`,
    append the three-bit value `R` to the message `1011010`.
    You can check your answer by performing the CRC as the receiver using your
    determined value of R.

    <!--
    Compute R:
    ```
              1100 100
    1101 | 1011010 000
           1101
            1100
            1101
             0011
             0000
              0110
              0000
               110 0
               110 1
                00 10
                00 00
                 0 100
                 0 000
                   100  <-- answer
    ```

    Check:
    ```
              1100 100
    1101 | 1011010 100
           1101
            1100
            1101
             0011
             0000
              0110
              0000
               110 1
               110 1
                00 00
                00 00
                 0 000
                 0 000
                   000  <-- verified
    ```
    -->

17. As people, we share the medium of sound when communicating.
    Give examples of human protocols for sharing this medium,
    both in one-on-one situations and scenarios involving multiple people.

18. You book lists "fully decentralized" as a desirable characteristic of
    a multiple-access protocol.
    Why do you think this is a desirable characteristic?

19. For each of the four desirable characteristics of a medium-access protocol
    listed below
    (taken from your textbook),
    give an example of a protocol that has that characteristic but that is
    a bad or imperfect protocol for some other reason.
    (These do not necessarily all need to be practical protocols.)
    * when one node wants to transmit,
      it can send at rate R (the full rate of the channel)
    * when M nodes want to transmit,
      each can send at average rate R/M
    * fully decentralized
    * simple

20. For each of the following scenarios,
    decide what the shared medium is and determine whether the protocol is more
    similar to TDMA or FDMA:
    * Your car radio has several stations it can tune into.
    * Airplanes follow a schedule so that two planes are never on the runway
      together.
    * A radio station plays songs individually throughout the day,
      rather than all together.
    * Satellites orbit at various altitudes above the earth so that they do not
      crash into one another.
