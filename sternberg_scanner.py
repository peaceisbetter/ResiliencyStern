#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.4),
    on January 19, 2023, at 09:15
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

import psychopy
psychopy.useVersion('2020.2.4')


from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.4'
expName = 'sternberg'  # from the Builder filename that created this script
expInfo = {'session': '001', 'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sort_keys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\NNL\\Desktop\\STERN\\sternberg_scanner.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=1, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='', color='White', colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='The goal for this task is to correctly identify letters presented to you at the beginning of a trial. \n\nAt the beginning of each trial you will be presented with, and must remember, a string of either 1, 5, or 7 capitalized letters. \n\nFollowing the presentation of the letters, you will be presented individual lower case letters, one at a time. They will be presented at a rate of 1 letter per second. You will need to decide whether the letter presented to you was one of the original letters presented at the beginning of the trial. \n\nIf the letter was one of the original letters, you will press the button under your right pointer finger. \nIf the letter was not one of the original letters, you will press the button under your right middle finger.',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=1.75, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()
subNum = expInfo['participant']
sessionNum = expInfo['session']
outfile= open("./data/sternberg.txt","a+")
outfile.write("subject")
outfile.write("\t")
outfile.write("stim")
outfile.write("\t")
outfile.write("block")
outfile.write("\t")
outfile.write("block_run")
outfile.write("\t")
outfile.write("letterset")
outfile.write("\t")
outfile.write("trial")
outfile.write("\t")
outfile.write("lettershown")
outfile.write("\t")
outfile.write("response")
outfile.write("\t")
outfile.write("acc")
outfile.write("\t")
outfile.write("rt")
outfile.write("\t")
outfile.write("trial.onset")
outfile.write("\t")
outfile.write("trial.duration")
outfile.write("\n")


outfile2= open("./data/" + subNum + "_" + sessionNum + "_sternberg.txt", "a+")
outfile2.write("timestamp: ")
outfile2.write(expInfo['date'])
outfile2.write("\n")
outfile2.write("subject")
outfile2.write("\t")
outfile2.write("stim")
outfile2.write("\t")
outfile2.write("block")
outfile2.write("\t")
outfile2.write("block_run")
outfile2.write("\t")
outfile2.write("letterset")
outfile2.write("\t")
outfile2.write("trial")
outfile2.write("\t")
outfile2.write("lettershown")
outfile2.write("\t")
outfile2.write("response")
outfile2.write("\t")
outfile2.write("acc")
outfile2.write("\t")
outfile2.write("rt")
outfile2.write("\t")
outfile2.write("trial.onset")
outfile2.write("\t")
outfile2.write("trial.duration")
outfile2.write("\t")
outfile2.write("block.duration")
outfile2.write("\n")

# Initialize components for Routine "exampleinstructions"
exampleinstructionsClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='For example, at the beginning of a trial, you may see:\n\n                                           A Q H D B\n\nFollowing this you will be presented letters, one at a time, such as:\n\n                                                   n\n\nSince this letter is not one of the original 5, you would press the button under your right middle finger.\n\nYou will need to make a quick, but accurate decision.',
    font='Arial',
    pos=(0, 0), height=.075, wrapWidth=1.75, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "instructions_2"
instructions_2Clock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='You will complete three runs of this task. Within each run, you will complete three study blocks, each block with different letters.\n\nEach run will last about 4 minutes.\n\nQuestions?',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=1.75, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "PleaseWait"
PleaseWaitClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='Please Wait',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='Black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_6 = keyboard.Keyboard()



# Initialize components for Routine "trigger"
triggerClock = core.Clock()
text_12 = visual.TextStim(win=win, name='text_12',
    text=' ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "wait"
waitClock = core.Clock()
text_13 = visual.TextStim(win=win, name='text_13',
    text='Get ready for the letters',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
import time

# Initialize components for Routine "prompt"
promptClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='Get ready for the letters',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Stimuli"
StimuliClock = core.Clock()
fixcross = visual.TextStim(win=win, name='fixcross',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
##Import allows you to bring in a package, random package randomizes stimuli
import random
import numpy
import string
import operator

#This is an array within an array that contains all eligible letters in both lower and uppercase form
array = [['A','a'], ['B','b'], ['D','d'], ['E','e'], ['F','f'], ['G','g'], ['H','h'], ['J','j'], ['K','k'], ['M','m'], ['N','n'], ['Q','q'], ['R','r'], ['T','t'], ['U','u'], ['W','w'], ['Y','y']]

#This is the difficulty
x = [1,5,7]
#This shuffles the array at the beginning of the experiment only
#y = random.shuffle(x)

#placeholder text
stimuli_txt = 'zzz'

blocknumber = 0
blockcount = 0
text_4 = visual.TextStim(win=win, name='text_4',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=12, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "fixation_cross"
fixation_crossClock = core.Clock()
text_9 = visual.TextStim(win=win, name='text_9',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='Black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Response"
ResponseClock = core.Clock()
text_8 = visual.TextStim(win=win, name='text_8',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
#placeholder text
response_txt ='zzz'


text_5 = visual.TextStim(win=win, name='text_5',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.25, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "blockduration"
blockdurationClock = core.Clock()

# Initialize components for Routine "prompt2"
prompt2Clock = core.Clock()
text_11 = visual.TextStim(win=win, name='text_11',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "EndInstructions"
EndInstructionsClock = core.Clock()
text_10 = visual.TextStim(win=win, name='text_10',
    text='You have completed the experiment!',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='Black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_7 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
InstructionsComponents = [text, key_resp_2]
for thisComponent in InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "exampleinstructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
exampleinstructionsComponents = [text_2, key_resp_3]
for thisComponent in exampleinstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
exampleinstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "exampleinstructions"-------
while continueRoutine:
    # get current time
    t = exampleinstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=exampleinstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in exampleinstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "exampleinstructions"-------
for thisComponent in exampleinstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
# the Routine "exampleinstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instructions_2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
instructions_2Components = [text_3, key_resp_4]
for thisComponent in instructions_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructions_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions_2"-------
while continueRoutine:
    # get current time
    t = instructions_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructions_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions_2"-------
for thisComponent in instructions_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys = None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.addData('key_resp_4.started', key_resp_4.tStartRefresh)
thisExp.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
thisExp.nextEntry()
# the Routine "instructions_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
block = data.TrialHandler(nReps=3, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='block')
thisExp.addLoop(block)  # add the loop to the experiment
thisBlock = block.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

for thisBlock in block:
    currentLoop = block
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "PleaseWait"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_6.keys = []
    key_resp_6.rt = []
    _key_resp_6_allKeys = []
    start_time_block = time.perf_counter() 
    # keep track of which components have finished
    PleaseWaitComponents = [text_7, key_resp_6]
    for thisComponent in PleaseWaitComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    PleaseWaitClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "PleaseWait"-------
    while continueRoutine:
        # get current time
        t = PleaseWaitClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=PleaseWaitClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_7* updates
        if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_7.frameNStart = frameN  # exact frame index
            text_7.tStart = t  # local t and not account for scr refresh
            text_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
            text_7.setAutoDraw(True)
        
        # *key_resp_6* updates
        waitOnFlip = False
        if key_resp_6.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.tStart = t  # local t and not account for scr refresh
            key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_6.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_6_allKeys.extend(theseKeys)
            if len(_key_resp_6_allKeys):
                key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                key_resp_6.rt = _key_resp_6_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PleaseWaitComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "PleaseWait"-------
    for thisComponent in PleaseWaitComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block.addData('text_7.started', text_7.tStartRefresh)
    block.addData('text_7.stopped', text_7.tStopRefresh)
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
        key_resp_6.keys = None
    block.addData('key_resp_6.keys',key_resp_6.keys)
    if key_resp_6.keys != None:  # we had a response
        block.addData('key_resp_6.rt', key_resp_6.rt)
    block.addData('key_resp_6.started', key_resp_6.tStartRefresh)
    block.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
    # the Routine "PleaseWait" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "trigger"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    triggerComponents = [text_12, key_resp]
    for thisComponent in triggerComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    triggerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trigger"-------
    while continueRoutine:
        # get current time
        t = triggerClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=triggerClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_12* updates
        if text_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_12.frameNStart = frameN  # exact frame index
            text_12.tStart = t  # local t and not account for scr refresh
            text_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_12, 'tStartRefresh')  # time at next scr refresh
            text_12.setAutoDraw(True)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['T', 't'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in triggerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trigger"-------
    for thisComponent in triggerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block.addData('text_12.started', text_12.tStartRefresh)
    block.addData('text_12.stopped', text_12.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    block.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        block.addData('key_resp.rt', key_resp.rt)
    block.addData('key_resp.started', key_resp.tStartRefresh)
    block.addData('key_resp.stopped', key_resp.tStopRefresh)
    # the Routine "trigger" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "wait"-------
    continueRoutine = True
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    waitComponents = [text_13]
    for thisComponent in waitComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    waitClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "wait"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = waitClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=waitClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_13* updates
        if text_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_13.frameNStart = frameN  # exact frame index
            text_13.tStart = t  # local t and not account for scr refresh
            text_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_13, 'tStartRefresh')  # time at next scr refresh
            text_13.setAutoDraw(True)
        if text_13.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_13.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                text_13.tStop = t  # not accounting for scr refresh
                text_13.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_13, 'tStopRefresh')  # time at next scr refresh
                text_13.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in waitComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "wait"-------
    for thisComponent in waitComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block.addData('text_13.started', text_13.tStartRefresh)
    block.addData('text_13.stopped', text_13.tStopRefresh)
    start_time = time.perf_counter() 
    
    # set up handler to look after randomisation of conditions etc
    blockrepeat = data.TrialHandler(nReps=3, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='blockrepeat')
    thisExp.addLoop(blockrepeat)  # add the loop to the experiment
    thisBlockrepeat = blockrepeat.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlockrepeat.rgb)
    if thisBlockrepeat != None:
        for paramName in thisBlockrepeat:
            exec('{} = thisBlockrepeat[paramName]'.format(paramName))
    
    for thisBlockrepeat in blockrepeat:
        currentLoop = blockrepeat
        # abbreviate parameter names if possible (e.g. rgb = thisBlockrepeat.rgb)
        if thisBlockrepeat != None:
            for paramName in thisBlockrepeat:
                exec('{} = thisBlockrepeat[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "prompt"-------
        continueRoutine = True
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        promptComponents = [text_6]
        for thisComponent in promptComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        promptClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "prompt"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = promptClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=promptClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_6* updates
            if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_6.frameNStart = frameN  # exact frame index
                text_6.tStart = t  # local t and not account for scr refresh
                text_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
                text_6.setAutoDraw(True)
            if text_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_6.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    text_6.tStop = t  # not accounting for scr refresh
                    text_6.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_6, 'tStopRefresh')  # time at next scr refresh
                    text_6.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in promptComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "prompt"-------
        for thisComponent in promptComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        blockrepeat.addData('text_6.started', text_6.tStartRefresh)
        blockrepeat.addData('text_6.stopped', text_6.tStopRefresh)
        
        # ------Prepare to start Routine "Stimuli"-------
        continueRoutine = True
        routineTimer.add(7.600000)
        # update component parameters for each repeat
        #This shuffles the order of the letter arrays within the larger array. 
        #For example [A, a] will stay the same, but [A, a] might not be in the first possition, but the 4th. 
        random.shuffle(array)
        
        correctarray = [1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0]
        random.shuffle(correctarray)
        
        #This sets the random letters to be displayed. 
        #A capital (cap) and lower (low) case letter is displayed. 
        #In the array[x][x], the first [x] tells you which letter will be used and the second[x] tells you whether the letter is upper [0] or lower[1] case
        cap1 = array[0][0]
        low1 = array[0][1]
        cap2 = array[1][0]
        low2 = array[1][1]
        cap3 = array[2][0]
        low3 = array[2][1]
        cap4 = array[3][0]
        low4 = array[3][1]
        cap5 = array[4][0]
        low5 = array[4][1]
        cap6 = array[5][0]
        low6 = array[5][1]
        cap7 = array[6][0]
        low7 = array[6][1]
        
        
        #This randomly choses the difficulty
        difficulty = random.choice(x)
        
        #This detemines which letters to display based on the randomly chosen level of difficulty from the previous step. 
        #The letters are pulled from the arrays above. 
        if difficulty == 1: 
            stimuli_txt= (cap1)
        elif difficulty == 5:
            stimuli_txt= (cap1 + ' ' + cap2 + ' ' + cap3 + ' '+ cap4 + ' ' + cap5) 
        elif difficulty == 7:
            stimuli_txt= (cap1 + ' ' + cap2 + ' ' + cap3 + ' '+ cap4 + ' ' + cap5 + ' '+ cap6 + ' '+ cap7)
        
        #This deletes the difficulty just displayed from the array created in the 'Begin Experiment' (x) so that only the difficulties written in the 'x' are presented
        x.remove(difficulty)
        
        trialnumber = 0
        text_4.setText(stimuli_txt)
        # keep track of which components have finished
        StimuliComponents = [fixcross, text_4]
        for thisComponent in StimuliComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        StimuliClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Stimuli"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = StimuliClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=StimuliClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixcross* updates
            if fixcross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixcross.frameNStart = frameN  # exact frame index
                fixcross.tStart = t  # local t and not account for scr refresh
                fixcross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixcross, 'tStartRefresh')  # time at next scr refresh
                fixcross.setAutoDraw(True)
            if fixcross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixcross.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fixcross.tStop = t  # not accounting for scr refresh
                    fixcross.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixcross, 'tStopRefresh')  # time at next scr refresh
                    fixcross.setAutoDraw(False)
            
            # *text_4* updates
            if text_4.status == NOT_STARTED and tThisFlip >= 1.4-frameTolerance:
                # keep track of start time/frame for later
                text_4.frameNStart = frameN  # exact frame index
                text_4.tStart = t  # local t and not account for scr refresh
                text_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
                text_4.setAutoDraw(True)
            if text_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_4.tStartRefresh + 6.2-frameTolerance:
                    # keep track of stop time/frame for later
                    text_4.tStop = t  # not accounting for scr refresh
                    text_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                    text_4.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in StimuliComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Stimuli"-------
        for thisComponent in StimuliComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        blockrepeat.addData('fixcross.started', fixcross.tStartRefresh)
        blockrepeat.addData('fixcross.stopped', fixcross.tStopRefresh)
        blocknumber = blocknumber + 1
        blockcount = blockcount + 1
        
        blockrepeat.addData('text_4.started', text_4.tStartRefresh)
        blockrepeat.addData('text_4.stopped', text_4.tStopRefresh)
        
        # ------Prepare to start Routine "fixation_cross"-------
        continueRoutine = True
        routineTimer.add(1.800000)
        # update component parameters for each repeat
        # keep track of which components have finished
        fixation_crossComponents = [text_9]
        for thisComponent in fixation_crossComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        fixation_crossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "fixation_cross"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = fixation_crossClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=fixation_crossClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_9* updates
            if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_9.frameNStart = frameN  # exact frame index
                text_9.tStart = t  # local t and not account for scr refresh
                text_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
                text_9.setAutoDraw(True)
            if text_9.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_9.tStartRefresh + 1.8-frameTolerance:
                    # keep track of stop time/frame for later
                    text_9.tStop = t  # not accounting for scr refresh
                    text_9.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_9, 'tStopRefresh')  # time at next scr refresh
                    text_9.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixation_crossComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "fixation_cross"-------
        for thisComponent in fixation_crossComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        blockrepeat.addData('text_9.started', text_9.tStartRefresh)
        blockrepeat.addData('text_9.stopped', text_9.tStopRefresh)
        
        # set up handler to look after randomisation of conditions etc
        responserepeat = data.TrialHandler(nReps=16, method='fullRandom', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='responserepeat')
        thisExp.addLoop(responserepeat)  # add the loop to the experiment
        thisResponserepeat = responserepeat.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisResponserepeat.rgb)
        if thisResponserepeat != None:
            for paramName in thisResponserepeat:
                exec('{} = thisResponserepeat[paramName]'.format(paramName))
        
        for thisResponserepeat in responserepeat:
            currentLoop = responserepeat
            # abbreviate parameter names if possible (e.g. rgb = thisResponserepeat.rgb)
            if thisResponserepeat != None:
                for paramName in thisResponserepeat:
                    exec('{} = thisResponserepeat[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "Response"-------
            continueRoutine = True
            routineTimer.add(2.000000)
            # update component parameters for each repeat
            #This picks a random letter from the letter array set in the stimuli routine
            k = random.choice(array[difficulty:16])
            #this ensures the letter chosen in k is lower case
            m = k[1]
            #This sets the letters for level 1 difficulty from the letter array set in the stimuli routine
            n = random.choice([low1])
            #This sets the letters for level 5 and 7 difficulty from the letter array set in the stimuli routine
            o = random.choice([low1,low2,low3,low4,low5])
            p = random.choice([low1,low2,low3,low4,low5,low6,low7])
            
            #this makes sure that at least 40% of trials contain a correct response
            if difficulty == 1:
                if correctarray[trialnumber] == 1:
                    correct = 1
                    response_txt = n
                else:
                    response_txt = m
                    correct = 0
            elif difficulty == 5:
                if correctarray[trialnumber] == 1:
                    correct = 1
                    response_txt = o
                else:
                    response_txt = m
                    correct = 0
            elif difficulty == 7:
                if correctarray[trialnumber] == 1:
                    correct = 1
                    response_txt = p
                else:
                    response_txt = m
                    correct = 0
            
            
            trial_onset_time = time.perf_counter() - start_time
            text_5.setText(response_txt)
            key_resp_5.keys = []
            key_resp_5.rt = []
            _key_resp_5_allKeys = []
            # keep track of which components have finished
            ResponseComponents = [text_8, text_5, key_resp_5]
            for thisComponent in ResponseComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            ResponseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "Response"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = ResponseClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=ResponseClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_8* updates
                if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_8.frameNStart = frameN  # exact frame index
                    text_8.tStart = t  # local t and not account for scr refresh
                    text_8.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
                    text_8.setAutoDraw(True)
                if text_8.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_8.tStartRefresh + .8-frameTolerance:
                        # keep track of stop time/frame for later
                        text_8.tStop = t  # not accounting for scr refresh
                        text_8.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(text_8, 'tStopRefresh')  # time at next scr refresh
                        text_8.setAutoDraw(False)
                
                # *text_5* updates
                if text_5.status == NOT_STARTED and tThisFlip >= .8-frameTolerance:
                    # keep track of start time/frame for later
                    text_5.frameNStart = frameN  # exact frame index
                    text_5.tStart = t  # local t and not account for scr refresh
                    text_5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
                    text_5.setAutoDraw(True)
                if text_5.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_5.tStartRefresh + 1.2-frameTolerance:
                        # keep track of stop time/frame for later
                        text_5.tStop = t  # not accounting for scr refresh
                        text_5.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(text_5, 'tStopRefresh')  # time at next scr refresh
                        text_5.setAutoDraw(False)
                
                # *key_resp_5* updates
                waitOnFlip = False
                if key_resp_5.status == NOT_STARTED and tThisFlip >= .8-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_5.frameNStart = frameN  # exact frame index
                    key_resp_5.tStart = t  # local t and not account for scr refresh
                    key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
                    key_resp_5.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_5.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > key_resp_5.tStartRefresh + 1.2-frameTolerance:
                        # keep track of stop time/frame for later
                        key_resp_5.tStop = t  # not accounting for scr refresh
                        key_resp_5.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(key_resp_5, 'tStopRefresh')  # time at next scr refresh
                        key_resp_5.status = FINISHED
                if key_resp_5.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_5.getKeys(keyList=['1', '2', 'c', 'd', 'C', 'D'], waitRelease=False)
                    _key_resp_5_allKeys.extend(theseKeys)
                    if len(_key_resp_5_allKeys):
                        key_resp_5.keys = _key_resp_5_allKeys[0].name  # just the first key pressed
                        key_resp_5.rt = _key_resp_5_allKeys[0].rt
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ResponseComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "Response"-------
            for thisComponent in ResponseComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            responserepeat.addData('text_8.started', text_8.tStartRefresh)
            responserepeat.addData('text_8.stopped', text_8.tStopRefresh)
            outfile.write(subNum)
            outfile.write("\t")
            outfile.write(sessionNum)
            outfile.write("\t")
            outfile.write(str(blockcount))
            outfile.write("\t")
            outfile.write(str(blocknumber))
            outfile.write("\t")
            outfile.write(stimuli_txt)
            outfile.write("\t")
            outfile.write(str(trialnumber+1))
            outfile.write("\t")
            outfile.write(response_txt)
            outfile.write("\t")
            outfile.write(str(key_resp_5.keys))
            outfile.write("\t")
            
            response = key_resp_5.keys
            
            if not key_resp_5.keys: outfile.write("Miss")
            elif correct == 1 and response is 'c': outfile.write( "Correct" )
            elif correct == 0 and response is 'd': outfile.write( "Correct" )
            else: outfile.write( "Incorrect")
            
            outfile.write("\t")
            outfile.write( str(key_resp_5.rt*1000) )
            outfile.write("\t")
            outfile.write(str(trial_onset_time))
            outfile.write("\t")
            outfile.write(str(t))
            outfile.write("\n")
            
            
            outfile2.write(subNum)
            outfile2.write("\t")
            outfile2.write(sessionNum)
            outfile2.write("\t")
            outfile2.write(str(blockcount))
            outfile2.write("\t")
            outfile2.write(str(blocknumber))
            outfile2.write("\t")
            outfile2.write(stimuli_txt)
            outfile2.write("\t")
            outfile2.write(str(trialnumber+1))
            outfile2.write("\t")
            outfile2.write(response_txt)
            outfile2.write("\t")
            outfile2.write(str(key_resp_5.keys))
            outfile2.write("\t")
            
            response = key_resp_5.keys
            
            if not key_resp_5.keys: outfile2.write("Miss")
            elif correct == 1 and response is 'c': outfile2.write( "Correct" )
            elif correct == 0 and response is 'd': outfile2.write( "Correct" )
            else: outfile2.write( "Incorrect")
            
            outfile2.write("\t")
            outfile2.write( str(key_resp_5.rt*1000) )
            outfile2.write("\t")
            outfile2.write(str(trial_onset_time))
            outfile2.write("\t")
            outfile2.write(str(t))
            outfile2.write("\n")
            
            
            trialnumber=trialnumber+1
            
            responserepeat.addData('text_5.started', text_5.tStartRefresh)
            responserepeat.addData('text_5.stopped', text_5.tStopRefresh)
            # check responses
            if key_resp_5.keys in ['', [], None]:  # No response was made
                key_resp_5.keys = None
            responserepeat.addData('key_resp_5.keys',key_resp_5.keys)
            if key_resp_5.keys != None:  # we had a response
                responserepeat.addData('key_resp_5.rt', key_resp_5.rt)
            responserepeat.addData('key_resp_5.started', key_resp_5.tStartRefresh)
            responserepeat.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
            thisExp.nextEntry()
            
        # completed 16 repeats of 'responserepeat'
        
        
        # ------Prepare to start Routine "blockduration"-------
        continueRoutine = True
        # update component parameters for each repeat
        block_end_time = time.perf_counter() - start_time
        
        task_time = time.perf_counter() - start_time_block
        
        
        # keep track of which components have finished
        blockdurationComponents = []
        for thisComponent in blockdurationComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        blockdurationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "blockduration"-------
        while continueRoutine:
            # get current time
            t = blockdurationClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=blockdurationClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blockdurationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "blockduration"-------
        for thisComponent in blockdurationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        outfile2.write("\t")
        outfile2.write("\t")
        outfile2.write("\t")
        outfile2.write("\t")
        outfile2.write("\t")
        outfile2.write("\t")
        outfile2.write("\t")
        outfile2.write("\t")
        outfile2.write("\t")
        outfile2.write("\t")
        outfile2.write("\t")
        outfile2.write(str(block_end_time))
        outfile2.write("\t")
        outfile2.write(str(task_time))
        outfile2.write("\n")
        
        
        if blocknumber > 2:
            x = [1,5,7]
            blocknumber = 0
        # the Routine "blockduration" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "prompt2"-------
        continueRoutine = True
        routineTimer.add(16.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        prompt2Components = [text_11]
        for thisComponent in prompt2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        prompt2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "prompt2"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = prompt2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=prompt2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_11* updates
            if text_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_11.frameNStart = frameN  # exact frame index
                text_11.tStart = t  # local t and not account for scr refresh
                text_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
                text_11.setAutoDraw(True)
            if text_11.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_11.tStartRefresh + 16-frameTolerance:
                    # keep track of stop time/frame for later
                    text_11.tStop = t  # not accounting for scr refresh
                    text_11.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_11, 'tStopRefresh')  # time at next scr refresh
                    text_11.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in prompt2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "prompt2"-------
        for thisComponent in prompt2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        blockrepeat.addData('text_11.started', text_11.tStartRefresh)
        blockrepeat.addData('text_11.stopped', text_11.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 3 repeats of 'blockrepeat'
    
# completed 3 repeats of 'block'


# ------Prepare to start Routine "EndInstructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_7.keys = []
key_resp_7.rt = []
_key_resp_7_allKeys = []
outfile2.write("timestamp: ")
outfile2.write(expInfo['date'])
# keep track of which components have finished
EndInstructionsComponents = [text_10, key_resp_7]
for thisComponent in EndInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "EndInstructions"-------
while continueRoutine:
    # get current time
    t = EndInstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndInstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_10* updates
    if text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_10.frameNStart = frameN  # exact frame index
        text_10.tStart = t  # local t and not account for scr refresh
        text_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
        text_10.setAutoDraw(True)
    
    # *key_resp_7* updates
    waitOnFlip = False
    if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.tStart = t  # local t and not account for scr refresh
        key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_7.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_7.getKeys(keyList=['esc'], waitRelease=False)
        _key_resp_7_allKeys.extend(theseKeys)
        if len(_key_resp_7_allKeys):
            key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
            key_resp_7.rt = _key_resp_7_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "EndInstructions"-------
for thisComponent in EndInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_10.started', text_10.tStartRefresh)
thisExp.addData('text_10.stopped', text_10.tStopRefresh)
# check responses
if key_resp_7.keys in ['', [], None]:  # No response was made
    key_resp_7.keys = None
thisExp.addData('key_resp_7.keys',key_resp_7.keys)
if key_resp_7.keys != None:  # we had a response
    thisExp.addData('key_resp_7.rt', key_resp_7.rt)
thisExp.addData('key_resp_7.started', key_resp_7.tStartRefresh)
thisExp.addData('key_resp_7.stopped', key_resp_7.tStopRefresh)
thisExp.nextEntry()
# the Routine "EndInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
