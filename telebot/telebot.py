#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import telepot
import sys
import os
import time
import subprocess
import commands
from datetime import timedelta

valid_id = 0000000000;
valid_id_2 = 0000000004;
name1 = "master";
name2= "secondmaster";
id1 = 0000000000;

def handle(msg):
    chat_id = msg['from']['id']
    message = msg['text'].lower()
    if chat_id != valid_id: 
	bot.sendMessage(valid_id, "Unbekannten-Chat: " + str(msg['from']))
	for x in range(0, 1) :
		bot.sendMessage(chat_id, message)
	return True
    okay = "nö"
    answer = u"Wovon redest du?"
#    bot.sendMessage(chat_id, chat_id)
    print 'Message from "%s": %s' % (msg['from']['first_name'], message)
#    print '    Got message: "%s" - from %s' % (message, msg['from']['first_name'])
     
    if chat_id == valid_id:
	okay = "okay"
    if chat_id == valid_id_2:
        okay = "okay"
	#bot.sendMessage(valid_id_2, "Hallo")
    if okay != "okay":
       print "unauthorised chat id: %i" % ( chat_id )
       bot.sendMessage(20329297, "unauthorised chat_id: " + `chat_id`)
    else:
	if message == "uptime":
	    with open('/proc/uptime', 'r') as f:
		uptime_seconds = float(f.readline().split()[0])
		uptime_string = str(timedelta(seconds = uptime_seconds))
		answer = uptime_string[:-7]
	elif message == "ls -la":
            p = commands.getstatusoutput('ls -la');
            out, err = p
            answer =  err
	elif message == "papa":
            p = commands.getstatusoutput('ping 192.168.110.62 -c 1');
            out, err = p
            answer =  err
	elif message == "mama":
            p = commands.getstatusoutput('ping 192.168.110.65 -c 1');
            out, err = p
            answer =  err
	elif message == "boswatch_raw":
            p = commands.getstatusoutput('cat /opt/boswatch/mm_raw.text');
            out, err = p
            answer =  err		
	elif message == "ssh -start":
            p = commands.getstatusoutput('service ssh start');
            out, err = p
            answer = err
	elif message == "ssh -stop":
            p = commands.getstatusoutput('service ssh stop');
            out, err = p
            answer = err
	elif message == "who -eth":
	    p = commands.getstatusoutput('sudo arp-scan -l -I eth0 | grep 192.168.')
	    out, err = p
	    answer = err
	elif message == "who -wlan":
	    p = commands.getstatusoutput('sudo arp-scan -l -I wlan0 | grep 192.168.')
	    out, err = p
	    answer = err
	elif message == "ip":
            p = commands.getstatusoutput('./opt/telebot/whatsmyip.sh')
            out, err = p
            answer = err
	elif message == "list":
            p = commands.getstatusoutput('cat /opt/telebot/command.list')
            out, err = p
            answer = err
	elif message == "boswatch_log":
            p = commands.getstatusoutput('cat /opt/boswatch/log/boswatch.log')
            out, err = p
            answer = err
	elif message == "user":
	    p = subprocess.Popen(['w', '-sof'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	    answer, err = p.communicate()
	elif message == "reboot":
	    answer = u"Neustart gestartet"
	    os.system("sudo shutdown -r 0 &")
        elif message == "reboot stop":
            p = commands.getstatusoutput('sudo shutdown -c')
            out, err = p
            answer = err
            if answer == "":
               answer = "reboot stoped"
	elif message == "ip":
	    p = commands.getstatusoutput('ip addr show | grep inet')
	    err, answer = p
	else:
		colon = message.find(":")
		if colon != -1:
			chat=message[:colon]
			command = ""
			backup = message[colon+1:].find(" ")
			if chat == name1 :
				chat = id1
			elif chat == "me" :
				chat = valid_id
			elif chat == name2 :
                                chat = valid_id_2
				bot.sendMessage(chat, message[(colon+1):])
				answer = "Message sent to "+str(chat)
			if message[:colon] == "ping" :
                                command = "ping " + message[colon+1:] + " -c 1"
                                p = commands.getstatusoutput(command)
                                err, answer = p
                        elif message[:colon] == "service -r" :
                                command = "service " + message[colon+1:] + " restart"
                                p = commands.getstatusoutput(command)
                                err, answer = p
                        elif message[:colon] == "service -s" :
                                 command = "service " + message[colon+1:] + " status"
                                 p = commands.getstatusoutput(command)
                                 err, answer = p
			else:
				try:
					bot.sendMessage(int(chat), message[(colon+1):])
					answer = "Message sent to "+str(chat)
				except ValueError:
					print "error"


		else:
			if chat_id == valid_id:
				answer = u"Hi, Master, das war kein gültiger Befehl"
			

#    print answer
#    print 'Message from "%s": %s' % (msg['from']['first_name'], answer)  

#    print 'Answering    "%s": %s' % (msg['from']['first_name'], answer)
    if answer != "":
#       answer = "no answer required"
       bot.sendMessage(chat_id, answer)
    print answer

bot = telepot.Bot('00000000000000000000000000000000000000000000000000000000000000000000000000')
bot.sendMessage(valid_id, "Bot gestartet.")
bot.message_loop(handle)

print 'I am listening ...'

while 1:
    time.sleep(10)

