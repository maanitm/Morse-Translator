import RPi.GPIO as GPIO
import time
import LetterCodes as lc

GPIO.setmode (GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
print("Welcome to the English -> Morse Translator\n")

shortLen = 1
longLen = 3
wordSpace = 7

def on(short):
  GPIO.output(18,GPIO.HIGH)
  if short:
    time.sleep(shortLen)
  else:
    time.sleep(longLen)
  return;
def off(short):
  GPIO.output(18,GPIO.LOW)
  if short:
    time.sleep(shortLen)
  else:
    time.sleep(longLen)
  return;

word = raw_input("Enter the word you would like to show: ")

for letter in word:
  if letter == "a":
    lc.a()
  if letter == "b":
    lc.b()
  if letter == "c":
    lc.c()
  if letter == "d":
    lc.d()
  if letter == "e":
    lc.e()
  if letter == "f":
    lc.f()
  if letter == "g":
    lc.g()
  if letter == "h":
    lc.h()
  if letter == "i":
    lc.i()
  if letter == "j":
    lc.j()
  if letter == "k":
    lc.k()
  if letter == "l":
    lc.l()
  if letter == "m":
    lc.m()
  if letter == "n":
    lc.n()
  if letter == "o":
    lc.o()
  if letter == "p":
    lc.p()
  if letter == "q":
    lc.q()
  if letter == "r":
    lc.r()
  if letter == "s":
    lc.s()
  if letter == "t":
    lc.t()
  if letter == "u":
    lc.u()
  if letter == "v":
    lc.v()
  if letter == "w":
    lc.w()
  if letter == "x":
    lc.x()
  if letter == "y":
    lc.y()
  if letter == "z":
    lc.z()
  if letter == " ":
    lc.space()
