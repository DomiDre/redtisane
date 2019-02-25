import numpy as np

degToRad = np.pi / 180
def gaussian(p, x):
  return p['A']/np.sqrt(2*np.pi)/p['sigma'] * np.exp( - ((x - p['mu'])/p['sigma'])**2 / 2)

def cosine2(p, x):
  return p['A'] * np.cos((2*np.pi*p['omega']*x - p['phase'])*degToRad)**2 + p['bg']

def residuum(p, x, y, sy, model):
  return (y - model(p, x))/sy

