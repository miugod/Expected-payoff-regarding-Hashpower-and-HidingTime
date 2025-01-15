# Background
## Linear structure of a PoW blockchain
In a PoW blockchain system, every block N should only be mined after block N-1 is mined, because N needs to include the time stamp of N-1, which is not revealed until N is published.
## Misbehaviour of Miners
If I have mined N, and want to get higher probability for the next block N+1 mined by also myself, do I want to risk by postponing the publishing time of N?

# Analysis
## In comparison to other miners
There will be a closed interval of "hiding time", in which attacker with >50% hashrate will gain no less ratio of overall blocks expected than his hashrate. 

There is also a best "hiding time", where the attacker gets the most ratio of overall blocks expected, for a fixed hashrate, regardless of how much time is used for block N.
## Difficulty Adjustment
Before a difficulty adjustment given by the system, it's hard for the attacker to gain much profit.

Reason: more time is wasted by hiding.
