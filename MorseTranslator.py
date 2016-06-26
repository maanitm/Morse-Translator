import RPi.GPIO as GPIO
import time

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
  
def a():
  on(True)
  off(True)
  on(False)  
  off(False)
  return;
def b():
  on(False)
  off(True)
  on(True)
  off(True)
  on(True)
  off(True)
  on(True)
  off(False)
  return;
def c():
  on(False)
  off(True)
  on(True)
  off(True)
  on(False)
  off(True)
  on(True)
  off(False)
  return;
def d():
  on(False)
  off(True)
  on(True)
  off(True)
  on(True)
  off(False)
  return;
def e():
  on(True)
  off(False)
  return;
def f():
  on(True)
  off(True)
  on(True)
  off(True)
  on(False)
  off(True)
  on(True)
  off(False)
  return;
def g():
  on(False)
  off(True)
  on(False)
  off(True)
  on(True)
  off(False)
  return;

word = raw_input("Enter the word you would like to show: ")

for letter in word:
  if letter == "a":
    a()
  if letter == "b":
    b()
  if letter == "c":
    c()
  if letter == "d":
    d()
  if letter == "e":
    e()
  if letter == "f":
    f()
  if letter == "g":
    g()
  if letter == "h":
    h()
  if letter == "i":
    i()
  if letter == "j":
    j()
  if letter == "k":
    k()
  if letter == "l":
    l()
  if letter == "m":
    m()
  if letter == "n":
    n()
  if letter == "o":
    o()
  if letter == "p":
    p()
  if letter == "q":
    q()
  if letter == "r":
    r()
  if letter == "s":
    s()
  if letter == "t":
    t()
  if letter == "u":
    u()
  if letter == "v":
    v()
  if letter == "w":
    w()
  if letter == "x":
    x()
  if letter == "y":
    y()
  if letter == "z":
    z()
  if letter == " ":
    space()
