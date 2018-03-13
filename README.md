# Input


```python
address: string "1BoatSLRHtKNngkdXEeobR76b53LETtpyT"
startTime: datetime "03/04/2017"
endTime: datetime "03/05/2017"
```


matching criteria: `startTime<= transactionTime <=endTime` 


# Output
{ 

  "time":Unix Time, 

  "outValues":[output btc value], 
  
  "recievers":[reciever address], 
  
  "senders":[sender address], 
  
  "inValues":[input btc value]
  
}
```json
{"time": 1488703979, "outValues": [377000], "recievers": ["19u2VR715Xnwq9K9r29fd2oaGm4quzKrLR"], "senders": ["1BoatSLRHtKNngkdXEeobR76b53LETtpyT"], "inValues": [500000]}
{"time": 1488703671, "outValues": [500000, 1513348, 170000, 471691, 80000, 500000], "recievers": ["1BoatSLRHtKNngkdXEeobR76b53LETtpyT", "3JJ2eTQ1N8Jze3cDjmPXiKWutGkJoD6iBZ", "1GDcVtyioe1WBtMGVy91YfM7BwL639DaVL", "1MFUErzUdqG9b5XzARusxf5jYCdgDKwvmh", "33Vcr5EgTCsr7jnnLNmFiQ3zZ3foQTKftS", "1FWnPWQhkqWgwKZFzmMgSfTx2TgTgpBucQ"], "senders": ["3G9xSjGGqpGoBiyP4QJc4LDZYBVBJ84rq5", "39btywUWnh1HSW78dxQQpk83RHCw947U88", "3B1wYBAWnmfpQU6U37E9p3x1MuVcP28TZQ", "3PeuSaEKJNq9hpmnGz59GJxt9jof1XDVmS"], "inValues": [76000, 105697, 439209, 2802244]}

```
