Note: some questions may be taken entirely or in part from your textbook.

# General Questions

1. What is the difference between an NS record and an A record in DNS?
If I have an NS record for a nameserver,
do I also need an A record for that same server?

2. If I want to email `student1@mail.gvsu.edu`, `student2@mail.gvsu.edu`,
and `prof@gvsu.edu`,
how many MX records do I need?
How many A records?

3. Which of these will cause a larger increase in records that must be stored
at the root DNS servers?
    * 500 new websites of the form `*.com`
    * Creating a new `.supergood` TLD that currently holds 50 websites

4. You become the proud owner of `457isthebest.com`.
What do you need to do to register `i.think.457isthebest.com`?

5. Consider running
```
dig gvsu.edu A
```
If the result of this query is `148.61.6.9`,
what happens if you then run
```
dig cis.gvsu.edu @148.61.6.9
```
Explain.

6. Consider running
```
dig gvsu.edu NS
```
and getting the result `corey.ns.cloudflare.com`.
Without making further DNS queries,
do you have enough information to send a message to GVSU's mail server?
What if you also had the IP address of `corey.ns.cloudflare.com`?

7. In the above example,
would the NS record containing the name `corey.ns.cloudflare.com` and the
A record containing the IP address of `corey.ns.cloudflare.com` be stored on
the same DNS server or different levels of DNS servers?
Explain.

8. Imagine there is a rapper named Diddy whose street address you would like
to know.
You ask a friend for the address and determine that his real name is P. Diddy,
but your friend does not know his address.
After asking another friend about P. Diddy,
you determine that his full name is Puff Daddy,
but this friend also does not have the address.
Finally, you ask another friend about Puff Daddy,
and this friend helpfully informs you that the rapper's name is Sean Combs and
that he lives at 123 Hip-Hop Boulevard.
What does any of this have to do with DNS?

9. Consider a library so large that each section
(e.g., 1800s history, 1900s history, nuclear physics, ichthyology, etc.)
has its own librarian.
The organizational system of this library is very strange,
so you need to ask a librarian to figure out where anything is.
Even finding a librarian for a given section can be tricky,
so there is a head librarian who knows the locations of all of the others.
In this scenario,
what person, place, or other entity corresponds to an authoritative nameserver?

10. Consider the above situation,
but there is also a front-desk librarian.
If you ask this librarian where to find a book,
they will figure out the answer and tell you exactly where it is.
What would be a few advantages to this scenario?
What does this front-desk librarian correspond to in terms of DNS?

11. Assume your local DNS server has the `gvsu.edu` NS record cached.
If you visit `cis.gvsu.edu/~bowmnath/index.html`,
how many DNS requests will your server need to make
(ones that it cannot satisfy from its cache)?

12. What is the difference between an MX record for `gvsu.edu` and an A record
for `gvsu.edu`?
If I have an MX record,
do I have all the information I need to contact the `gvsu.edu` mail server?

13. A recursive DNS request results in the client sending fewer DNS messages
for a particular query.
Why would a client ever *not* request a recursive query?

14. There are four sections in a DNS message that can contain questions or
resource records: "questions", "answers", "authority", "additional".
Consider a new student who asks you for the name of the building that houses
most CIS classes at GVSU.
You tell them that the building is called Mackinac Hall and the address is
10880 North Campus Drive.
If you were a DNS server,
which section would the part about 10880 North Campus Drive go into?

15. What is the purpose of the TTL field in DNS RRs?

16. In a previous lab,
we acted as an HTTP client and wrote messages directly to an actual server
using `netcat`.
We will not be repeating that experiment with DNS.
What in general about DNS as a protocol would make that activity more difficult
compared to HTTP?

17. If I were mad at Ferris State,
how many DNS servers would I need to bring down to make all websites in their
domain unavailable to the public?
(This is a thought experiment.
I do not condone internet vandalism no matter how many times a school beats us
in football.)

Switching gears to email...

18. Does a user agent need to understand SMTP?
Why or why not?

19. What is the advantage to using a dedicated mail server rather than sending
email directly from a user agent?

20. What is the difference between an SMTP handshake and a TCP handshake?
(We have not learned the details of a TCP handshake yet;
I'm looking for a fairly general answer here.)

21. Can you think of any reason an SMTP handshake is helpful?
Once the TCP connection is established,
why not just send the first email?

22. Based on what you saw in lecture,
how does SMTP prevent email spoofing
(sending email from someone else's address)?

23. SMTP connections are persistent.
What are possible benefits or drawbacks to this?

23. Describe what it means that SMTP is a push protocol whereas HTTP is a pull
protocol.

24. If you were to download a web page with some text and three images,
how many `HTTP GET` requests would you need?
How many application-layer messages are required to send an email with some
text and three images?

25. Is an access protocol,
such as POP3, IMAP, or HTTP,
necessary for reading email stored on a mail server?
If so, why?
If not, why not?
