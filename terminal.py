# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 11:04:58 2016

@author: ddan
"""

import time

def start_timer(minutes):
    time_left = minutes
    while time_left > 0:
        print 'Time left: {}min / {}min'.format(time_left, minutes)
        time.sleep(1)
        time_left -= 1

def main():
    print '---Pomodoro Timer---'
    timer_log = {}
    runs = 1
    
    while True:
        # Start Work
        work_duration = input('\nEnter WORK duration (mins): ')
        raw_input('Press Enter to start the timer...')
        start_timer(work_duration)
    
        #Start Rest
        rest_duration = input('\nEnter REST duration (mins): ')
        raw_input('Press Enter to start the timer...')
        start_timer(rest_duration)
    
        #Update Log
        timer_log[runs] = (work_duration,rest_duration)
        runs += 1
        
        #Print log
        print '\n---Log---'
        for key, value in timer_log.items():
            print 'Run{}: WORK - {}mins, REST - {}mins'.format(key,value[0],value[1])
        
        raw_input('\n---Press Enter to start next run---')
 
    
if __name__ == "__main__":
    main()



