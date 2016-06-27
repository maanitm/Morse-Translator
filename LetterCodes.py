import RPi.GPIO as GPIO

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
