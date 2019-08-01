# Challenge 1

## Overview

The organization allows applications with high severity vulnerabilities to be released, but nothing more severe than high. These three vulnerabilities are considered critical.
Resolve the vulnerabilities through implementing changes to the file and once the image is clean, the challenge is complete.

Note: Removal of these dependencies is not considered a solution, while it would work it is not the objective of this challenge.

[CVE-2018-18074](https://nvd.nist.gov/vuln/detail/CVE-2018-18074)

### Overview

- The Requests package before 2.20.0 for Python sends an HTTP Authorization header to an http URI upon receiving a same-hostname https-to-http redirect, which makes it easier for remote attackers to discover credentials by sniffing the network.

- Impact: Base Score - CVSS v3.0 Score - 9.8 - CRITICAL
- Affected up to 2.20 (excluding)

[CVE-2019-8457](https://nvd.nist.gov/vuln/detail/CVE-2019-8457)

### Overview

- SQLite3 from 3.6.0 to and including 3.27.2 is vulnerable to heap out-of-bound read in the rtreenode() function when handling invalid rtree tables.

### Version and Impact

- Impact: Base Score - CVSS v3.0 Score -9.8 - **CRITICAL**
- Affected up to 3.27.2 (including)

[CVE-2018-12699](https://nvd.nist.gov/vuln/detail/CVE-2018-12699)

### Overview

- finish_stab in stabs.c in GNU Binutils 2.30 allows attackers to cause a denial of service (heap-based buffer overflow) or possibly have unspecified other impact, as demonstrated by an out-of-bounds write of 8 bytes. This can occur during execution of objdump.

### Version and Impact

- Impact: Base Score - CVSS v3.0 Score - 9.8 - **CRITICAL**
- Affected version 2.30

## Bryce's Solution

### Mitigation(s) for CVE-18074

Upgraded version to 2.22.0 (latest)

### Mitigation(s) for CVE-2019-8457

Verified bin-utils is vulnerable in image via build output:

```
Installing sqlite-libs (3.25.3-r1)
```

- Mitigated by upgrading alpine image to 3.10.1 (latest)

Output after upgrade:

```
Installing sqlite-libs (3.28.0-r0)
```

### Mitigation(s) for CVE-2018-12699

Verified bin-utils is vulnerable in image via build output:

```
Installing binutils-libs (2.30-r1)
```

- Mitigated by upgrading alpine image to 3.10.1 (latest)

Output after upgrade:

```
(8/35) Installing binutils (2.32-r0)
```

## Additional Notes

1. Docker Alpine version 3.7 CVE-2019-5021 which affects 3.7 - https://alpinelinux.org/posts/Docker-image-vulnerability-CVE-2019-5021.html. Side note - if version cant be updated, possible mitigation for disabling root login:

```
RUN sed -i -e 's/^root::/root:!:/' /etc/shadow
```

2. Changed directory application ran from.
3. Could also look at potential running as non-ROOT user and deleting all unncessary files from container.

---
