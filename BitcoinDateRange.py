import urllib, json
import datetime
import sys
import csv
import argparse
from datetime import datetime

def getInputAddresses(inputFile):
	inputFile="input.csv"
	inputAddresses=[]

	with open(inputFile, 'rb') as infile:
		addressReader = csv.reader(infile)
		for fileAddress in addressReader:
			inputAddresses.append(fileAddress[0])
	return inputAddresses


def getTransactionHistory(address, pageNum):
	request = "https://blockchain.info/rawaddr/"
	offsetRequest = "?offset=" + str(pageNum * 50)
	rawaddrResponse = urllib.urlopen(request + address + offsetRequest)
	rawaddr = json.loads(rawaddrResponse.read())
	return rawaddr


def dateRangeBounds(rawaddr, startTime, endTime):
	rawtrans = rawaddr['txs']
	for trans in rawtrans:
		time = trans['time']
		transtime = datetime.fromtimestamp(time)
		if transtime < startTime:
			return True
	return False


def getAllTransactions(address, startTime, endTime):
	allRawTrans = []
	pageNum = 0
	while 1:
		rawaddr = getTransactionHistory(address,pageNum)
		if rawaddr['txs']!=[]:
			if dateRangeBounds(rawaddr, startTime, endTime):
				return allRawTrans
			allRawTrans.append(rawaddr)
		else:
			return allRawTrans
		pageNum = pageNum + 1
		# print("Searching Page #" + str(pageNum))

def processTransactions(allRawTrans, startTime, endTime):
	#rawtrans = allRawTrans[0]['txs']
	cleanedtrans = []
	for fullrawtrans in allRawTrans:
		rawtrans = fullrawtrans['txs']
		for trans in rawtrans:
			inputs = trans['inputs']
			senders = []
			inValues = []
			for sender in inputs:
				senders.append(sender['prev_out']['addr'])
				inValues.append(sender['prev_out']['value'])
			
			outputs = trans['out']
			recievers = []
			outValues = []
			for reciever in outputs:
				if 'addr' in reciever:
					recievers.append(reciever['addr'])
				outValues.append(reciever['value'])

			time = trans['time']
			transtime = datetime.fromtimestamp(time)

			txHash = trans['hash']
			if(startTime<=transtime<=endTime):
				transaction = {}
				transaction['senders'] = senders
				transaction['inValues'] = inValues
				transaction['recievers'] = recievers
				transaction['outValues'] = outValues
				transaction['time'] = time
				transaction['id'] = txHash
				cleanedtrans.append(transaction)
	return cleanedtrans


def transactionsByDate(address, firstDate, lastDate, uniqueTrasnactions):
	allRawTrans = getAllTransactions(address, firstDate, lastDate)
	cleanedTrans = processTransactions(allRawTrans, firstDate, lastDate)
	uniqueTrans = []
	
	for transaction in cleanedTrans:
		if transaction['id'] not in uniqueTrasnactions:
			uniqueTrasnactions.add(transaction['id'])
			uniqueTrans.append(transaction)
	# print "Found: " + str(len(uniqueTrans))
	return uniqueTrans

def transactionGraph(addressList, firstDate, lastDate):
	graph = {}
	uniqueTrasnactions = set()
	for address in addressList:
		graph[address] = transactionsByDate(address, firstDate, lastDate, uniqueTrasnactions)
	return graph


firstDate = datetime(2017, 3, 4, 1, 1, 1)
lastDate = datetime(2017, 3, 5, 1, 1, 1) 
addresses = ["1BoatSLRHtKNngkdXEeobR76b53LETtpyT"]
transactionGraph = transactionGraph(addresses, firstDate, lastDate)
print json.dumps(transactionGraph)

