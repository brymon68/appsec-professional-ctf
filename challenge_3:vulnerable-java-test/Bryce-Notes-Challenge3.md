# Challenge 3

## Bryce's Solution

There are a couple issues with the provided statement in my opinion, but the most glaring / obvious would be the omission of a prepared statement for the SELECT query. Instead, the author has opted to use a string which could be easily escaped via:

```
' OR 1=1
```

Effectively escaping the userName entry and appending to the query statement an OR operand which could evaluate to true. A better solution would be to use a prepared statement where input is compiled beforehand and do not use the same formatting / protocol.

Prepared statements are resilient against SQL injection because values which are transmitted later using a different protocol are not compiled like the statement template. Example using parameter / prepared statement:

```
db->prepare("SELECT * FROM users where userid=?");
```

The second issue is purely poor programming practice with using base64 encoding for obfuscation / "securing" of password information. If this state is executed without encryption over the network, it is simple to reverse the base64 encoding and identify the user's password.

## Bryce Notes

1. **getBytes()** encodes a string and returns an array of bytes.
2. **encodeToString()** - Encodes the specified byte array into a String using the Base64 encoding scheme.
