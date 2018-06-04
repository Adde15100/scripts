#!/bin/bash


wget http://whatsmyip.de -qO - | grep -i 'IP Adress' #| cut -c 4-18

