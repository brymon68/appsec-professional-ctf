# Challenge 4

Build a tool that can be used to automate identification of expired and soon-to-be expired HTTPS certificates associated with Overstock.com.

This challenge has a few components.

1. Identify which public subnets belong to Overstock.com.

2. Build a tool that can scan those subnets to identify hosts listening on port 443

3. Once those servers are identified, extract the HTTPS certificate and parse the validity information to see when it will expire.

4. Generate output that can be used to determine which certificates are (1) already expired or (2) will expire within the next year. This can be an email or a report, but it should be understandable and efficiently denote which certificates should be prioritized for update.

## Overview

I will build a tool that generates a report enumerating expired or soon-to-be expired HTTPS certifcates for subdomains within Overstock. The enumerated host list will be generated via 3rd party too named Dr_robot - https://github.com/sandialabs/dr_robot. Dr. Robot aggregates host information from numerous sources such as ARIN, Shodan, Sublist3r, etc. Sources like Sublist3r are able to enumerate domains from data provided from major search engines (Google, Bing, etc. ). It also enumerates subdomains from other sources such as Virustotal, ThreatCrowd, DNSdumpster, and ReverseDNS.

Once I've genearated a list of subdomains, I will validate TLS certificate expiration, version and type via OpenSSL for each domain's certificate (if presented) and create an easily readible output to be consumed by other clients.

Alternatively, instead of using a tool for generation of a domain and subdomain list, one could grab the publically available IPv4 range for a domain found at: https://whois.arin.net, and use nmap to programatically request :443 information from each IP within a range.

For instance, a quick search of \*overstock.com returns the following IP ranges from ARIN:

- 173.241.144.0 - 173.241.159.255 - /20 ~4094 hosts
- 63.239.22.56 - 63.239.22.63 - /29 - ~7 hosts
- 65.116.112.0 - 65.116.119.255 - /21 ~2046 hosts
- 67.110.104.0 - 67.110.111.255 - /21 ~2046

nmaping ~10k hosts on port 443 only, running in concurrence, I would expect could be done within a couple hours (max). The only thing I am concerned with is overstock.com could choose to not publish certain IP ranges to ARIN. (This is what makes Dr Robot so powerful). Furthermore,

Once I have the NMAP results, I would use the same code as below to grab certificate information and parse it into a consumable format (format_host_data). Perhaps the only tricky part about this would be for subdomains located on the same IP. But I believe this could be mitigated with resources like Shodan and ARIN.

I can go into detail with this more on the call.

## Automating identificaiton of expired and soon-to-be-expired HTTPS certificates

1. Downloaded dr_robot and configured tool to my enviornment.
2. Dr Robot both a list of ips, but also a list of domains.
3. With the list of domains in hand, my **format_host_data.py** script can request TLS certficiate expiration information via openssl. To speed the process up a bit more, I implemented threading.
4. Once TLS information is returned, I create an object until the program returns and I am left with an array of objects which I can export as JSON for consumption (final.json)

## Example outputs

Example output of Dr.Robot IP list:

```
air.travel.overstock.com
traveltrack.overstock.com
trk.overstock.com
tt11.overstock.com
um.overstock.com
univision.overstock.com
usedcars.overstock.com
vacations.overstock.com
vcsgw.overstock.com
```

Example output after parsing certificate informaiton:

```
[
  {
    "host": "www.overstock.com",
    "version": 2,
    "sig_algorithm": "sha256WithRSAEncryption",
    "expiration": 1620842400.0
  },
  {
    "host": "3dview.overstock.com",
    "version": 2,
    "sig_algorithm": "sha256WithRSAEncryption",
    "expiration": 1591552800.0
  }
```

## Bonus

If I have spare time:

1. I will create a webapp for viewing all 4 challenge results in MD format - **DONE**
2. Dockerize dr_robot and report generation for easy deployment anywhere / testability by Overstock.com management and technical teams - **Updated** INCOMPLETE - Ran out of time. See Dockerfile-unfinished for progress. I probably need about another two hours but seems like pipenv was not playign nicely with my Docker-In-Docker container.

At the very least, I if I am not able to finish bonus items, I will at least provide the below detailed report for how I generated the data and output of data.

## To Demo
