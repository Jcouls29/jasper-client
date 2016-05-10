# -*- coding: utf-8-*-
"""
A drop-in replacement for the Mic class that allows for all I/O to occur
over the terminal. Useful for debugging. Unlike with the typical Mic
implementation, Jasper is always active listening with local_mic.
"""
import logging
import tempfile
import wave
import audioop
import pyaudio
import alteration
import jasperpath

class Mic:
    prev = None

    def __init__(self, speaker, passive_stt_engine, active_stt_engine):
        self._logger = logging.getLogger(__name__)
        self.speaker = speaker
        self.audio = pyaudio.PyAudio()
        self._logger.info("Initialization of PyAudio completed.")

    def passiveListen(self, PERSONA):
        return True, "JASPER"

    def activeListenToAllOptions(self, THRESHOLD=None, LISTEN=True,
                                 MUSIC=False):
        return [self.activeListen(THRESHOLD=THRESHOLD, LISTEN=LISTEN,
                                  MUSIC=MUSIC)]

    def activeListen(self, THRESHOLD=None, LISTEN=True, MUSIC=False):
        if not LISTEN:
            return self.prev

        input = raw_input("YOU: ")
        self.prev = input
        return input

    def say(self, phrase, OPTIONS=None):
        phrase = alteration.clean(phrase)
        print("JASPER: %s" % phrase)
        self.speaker.say(phrase)
