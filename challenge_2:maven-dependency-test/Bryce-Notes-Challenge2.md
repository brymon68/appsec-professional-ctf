# Challenge 2

## Overview

The goal of this challenge is to assess how you resolve vulnerable dependencies within a maven project.

The repo contains a maven manifest file and a file containing the results of a Software Composition Analysis scan.

The organization allows applications with medium severity vulnerabilities to be released however this project contains 31 vulnerabilties considered high severity so in it's current state is not accepted as a release candidate.
Resolve the vulnerabilities through implementing changes to the pom file and once the image complies to the oranization's risk apetite, the challenge is complete.

## Bryce's Solution

1. Vulnerabilities found with Spring-Bootstarter (spring-boot-starter-web) version 1.1.1.RELEASE. Modified dependency:

```
	<dependency>
	    <groupId>org.springframework.boot</groupId>
	    <artifactId>spring-boot-starter-web</artifactId>
	    <version>2.1.6.RELEASE</version>
	</dependency>
```

2. Vulnerability found with Jackson (jackson-databind) verison 2.7.9.4. Modified dependency:

```
	<dependency>
    	    <groupId>com.fasterxml.jackson.core</groupId>
            <artifactId>jackson-databind</artifactId>
            <version>2.9.9.1</version>
	</dependency>
```

## Additional Notes

Also added mvn-dependency-check - https://jeremylong.github.io/DependencyCheck/dependency-check-maven/ to pom.xml to analyze dependencies and fail build on any vulnerabilites greater than or equal to 7.

```
<plugin>
              <groupId>org.owasp</groupId>
              <artifactId>dependency-check-maven</artifactId>
              <version>5.2.0</version>
              <configuration>
                  <failBuildOnCVSS>7</failBuildOnCVSS>
              </configuration>
              <executions>
                  <execution>
                      <goals>
                          <goal>check</goal>
                      </goals>
                  </execution>
              </executions>
            </plugin>
```

To run, enter command:

```
mvn verify
```

Output from tool on unmodified pom.xml:

```

[INFO] Analysis Started
[INFO] Finished Archive Analyzer (0 seconds)
[INFO] Finished File Name Analyzer (0 seconds)
[INFO] Finished Jar Analyzer (0 seconds)
[INFO] Finished Dependency Merging Analyzer (0 seconds)
[INFO] Finished Version Filter Analyzer (0 seconds)
[INFO] Finished Hint Analyzer (0 seconds)
[INFO] Created CPE Index (1 seconds)
[INFO] Finished CPE Analyzer (2 seconds)
[INFO] Finished False Positive Analyzer (0 seconds)
[INFO] Finished NVD CVE Analyzer (0 seconds)
[INFO] Finished Sonatype OSS Index Analyzer (1 seconds)
[INFO] Finished Vulnerability Suppression Analyzer (0 seconds)
[INFO] Finished Dependency Bundling Analyzer (0 seconds)
[INFO] Analysis Complete (4 seconds)
[WARNING]

One or more dependencies were identified with known vulnerabilities in siwilkins:

jackson-databind-2.7.9.4.jar (pkg:maven/com.fasterxml.jackson.core/jackson-databind@2.7.9.4, cpe:2.3:a:fasterxml:jackson:2.7.9.4:*:*:*:*:*:*:*, cpe:2.3:a:fasterxml:jackson-databind:2.7.9.4:*:*:*:*:*:*:*) : CVE-2017-15095, CVE-2017-17485, CVE-2018-1000873, CVE-2018-14718, CVE-2018-14719, CVE-2018-14720, CVE-2018-14721, CVE-2018-19360, CVE-2018-19361, CVE-2018-19362, CVE-2018-5968, CVE-2019-12086, CVE-2019-12384, CVE-2019-12814
spring-boot-starter-1.1.1.RELEASE.jar (pkg:maven/org.springframework.boot/spring-boot-starter@1.1.1.RELEASE, cpe:2.3:a:pivotal_software:spring_boot:1.1.1.release:*:*:*:*:*:*:*) : CVE-2017-8046, CVE-2018-1196
spring-boot-1.1.1.RELEASE.jar (pkg:maven/org.springframework.boot/spring-boot@1.1.1.RELEASE, cpe:2.3:a:pivotal_software:spring_boot:1.1.1.release:*:*:*:*:*:*:*) : CVE-2017-8046, CVE-2018-1196, Information exposure (classpath files), Memory exposure, Spring Expression Language (SpEL) injection on whitelabel error page
logback-core-1.1.2.jar (pkg:maven/ch.qos.logback/logback-core@1.1.2, cpe:2.3:a:logback:logback:1.1.2:*:*:*:*:*:*:*) : CVE-2017-5929
tomcat-embed-core-7.0.54.jar (pkg:maven/org.apache.tomcat.embed/tomcat-embed-core@7.0.54, cpe:2.3:a:apache:tomcat:7.0.54:*:*:*:*:*:*:*, cpe:2.3:a:apache_software_foundation:tomcat:7.0.54:*:*:*:*:*:*:*, cpe:2.3:a:apache_tomcat:apache_tomcat:7.0.54:*:*:*:*:*:*:*) : CVE-2014-0227, CVE-2014-0230, CVE-2014-7810, CVE-2015-5174, CVE-2015-5345, CVE-2015-5346, CVE-2015-5351, CVE-2016-0706, CVE-2016-0714, CVE-2016-0762, CVE-2016-0763, CVE-2016-3092, CVE-2016-5018, CVE-2016-5388, CVE-2016-6794, CVE-2016-6796, CVE-2016-6797, CVE-2016-6816, CVE-2016-8735, CVE-2016-8745, CVE-2017-12615, CVE-2017-12616, CVE-2017-12617, CVE-2017-5647, CVE-2017-5648, CVE-2017-5664, CVE-2017-7674, CVE-2018-11784, CVE-2018-1304, CVE-2018-1305, CVE-2018-1336, CVE-2018-8014, CVE-2018-8034, CVE-2019-0221, CVE-2019-0232
tomcat-embed-el-7.0.54.jar (pkg:maven/org.apache.tomcat.embed/tomcat-embed-el@7.0.54) : CVE-2014-7810
hibernate-validator-5.0.3.Final.jar (pkg:maven/org.hibernate/hibernate-validator@5.0.3.Final, cpe:2.3:a:redhat:hibernate_validator:5.0.3:*:*:*:*:*:*:*) : CVE-2014-3558
spring-core-4.0.5.RELEASE.jar (pkg:maven/org.springframework/spring-core@4.0.5.RELEASE, cpe:2.3:a:pivotal_software:spring_framework:4.0.5.release:*:*:*:*:*:*:*, cpe:2.3:a:springsource:spring_framework:4.0.5.release:*:*:*:*:*:*:*, cpe:2.3:a:vmware:springsource_spring_framework:4.0.5:*:*:*:*:*:*:*) : CVE-2014-3625, CVE-2015-5211, CVE-2016-5007, CVE-2018-1270, CVE-2018-1271, CVE-2018-1272
spring-web-4.0.5.RELEASE.jar (pkg:maven/org.springframework/spring-web@4.0.5.RELEASE, cpe:2.3:a:pivotal_software:spring_framework:4.0.5.release:*:*:*:*:*:*:*, cpe:2.3:a:springsource:spring_framework:4.0.5.release:*:*:*:*:*:*:*, cpe:2.3:a:vmware:springsource_spring_framework:4.0.5:*:*:*:*:*:*:*) : CVE-2014-3625, CVE-2015-3192, CVE-2015-5211, CVE-2018-1270, CVE-2018-1271, CVE-2018-1272
spring-aop-4.0.5.RELEASE.jar (pkg:maven/org.springframework/spring-aop@4.0.5.RELEASE, cpe:2.3:a:pivotal_software:spring_framework:4.0.5.release:*:*:*:*:*:*:*, cpe:2.3:a:springsource:spring_framework:4.0.5.release:*:*:*:*:*:*:*, cpe:2.3:a:vmware:springsource_spring_framework:4.0.5:*:*:*:*:*:*:*) : CVE-2014-3625, CVE-2018-1270, CVE-2018-1271, CVE-2018-1272
spring-webmvc-4.0.5.RELEASE.jar (pkg:maven/org.springframework/spring-webmvc@4.0.5.RELEASE, cpe:2.3:a:pivotal_software:spring_framework:4.0.5.release:*:*:*:*:*:*:*, cpe:2.3:a:springsource:spring_framework:4.0.5.release:*:*:*:*:*:*:*, cpe:2.3:a:vmware:springsource_spring_framework:4.0.5:*:*:*:*:*:*:*) : CVE-2014-3625, CVE-2015-5211, CVE-2018-1270, CVE-2018-1271, CVE-2018-1272


See the dependency-check report for more details.


[INFO] ------------------------------------------------------------------------
[INFO] BUILD FAILURE
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  8.183 s
[INFO] Finished at: 2019-07-31T22:09:26-06:00
[INFO] ------------------------------------------------------------------------
[ERROR] Failed to execute goal org.owasp:dependency-check-maven:5.2.0:check (default) on project ostk-base-pom:
[ERROR]
[ERROR] One or more dependencies were identified with vulnerabilities that have a CVSS score greater than or equal to '7.0':
[ERROR]
[ERROR] jackson-databind-2.7.9.4.jar: CVE-2017-17485, CVE-2018-5968, CVE-2017-15095, CVE-2018-19362, CVE-2018-19361, CVE-2018-19360, CVE-2018-14718, CVE-2018-14719, CVE-2018-14721, CVE-2018-14720, CVE-2019-12086
[ERROR] spring-boot-starter-1.1.1.RELEASE.jar: CVE-2017-8046
[ERROR] spring-boot-1.1.1.RELEASE.jar: CVE-2017-8046
[ERROR] logback-core-1.1.2.jar: CVE-2017-5929
[ERROR] tomcat-embed-core-7.0.54.jar: CVE-2016-3092, CVE-2016-5018, CVE-2016-8745, CVE-2018-8034, CVE-2018-8014, CVE-2015-5346, CVE-2018-1336, CVE-2019-0232, CVE-2016-6797, CVE-2016-5388, CVE-2016-6796, CVE-2016-8735, CVE-2017-12615, CVE-2017-12616, CVE-2014-0230, CVE-2017-5664, CVE-2016-6816, CVE-2017-5648, CVE-2015-5351, CVE-2016-0714, CVE-2017-5647, CVE-2017-12617
[ERROR] spring-core-4.0.5.RELEASE.jar: CVE-2015-5211, CVE-2018-1272, CVE-2016-5007, CVE-2018-1270
[ERROR] spring-web-4.0.5.RELEASE.jar: CVE-2015-5211, CVE-2018-1272, CVE-2018-1270
[ERROR] spring-aop-4.0.5.RELEASE.jar: CVE-2018-1272, CVE-2018-1270
[ERROR] spring-webmvc-4.0.5.RELEASE.jar: CVE-2015-5211, CVE-2018-1272, CVE-2018-1270
[ERROR]
[ERROR] See the dependency-check report for more details.
[ERROR]
[ERROR]
[ERROR] -> [Help 1]
[ERROR]
[ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
[ERROR] Re-run Maven using the -X switch to enable full debug logging.
[ERROR]
[ERROR] For more information about the errors and possible solutions, please read the following articles:
[ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/MojoFailureException
```

Output from modified pom.xml:

```
[INFO] Analysis Started
[INFO] Finished Archive Analyzer (0 seconds)
[INFO] Finished File Name Analyzer (0 seconds)
[INFO] Finished Jar Analyzer (0 seconds)
[INFO] Finished Dependency Merging Analyzer (0 seconds)
[INFO] Finished Version Filter Analyzer (0 seconds)
[INFO] Finished Hint Analyzer (0 seconds)
[INFO] Created CPE Index (1 seconds)
[INFO] Finished CPE Analyzer (2 seconds)
[INFO] Finished False Positive Analyzer (0 seconds)
[INFO] Finished NVD CVE Analyzer (0 seconds)
[INFO] Finished Sonatype OSS Index Analyzer (0 seconds)
[INFO] Finished Vulnerability Suppression Analyzer (0 seconds)
[INFO] Finished Dependency Bundling Analyzer (0 seconds)
[INFO] Analysis Complete (3 seconds)
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  6.804 s
[INFO] Finished at: 2019-07-31T22:07:11-06:00
[INFO] ------------------------------------------------------------------------
```

---
