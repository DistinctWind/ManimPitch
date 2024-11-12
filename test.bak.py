from pathlib import Path
import librosa
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# y, sr = librosa.load(librosa.ex('trumpet'))

y, sr = librosa.load(Path("vocal.wav"))
C2_hz = float(librosa.note_to_hz("C2"))
C7_hz = float(librosa.note_to_hz("C7"))
f0, voiced_flag, voiced_probs = librosa.pyin(
    y,
    sr=sr,
    fmin=C2_hz,
    fmax=C7_hz,
)
times = librosa.times_like(f0, sr=sr)

plt.subplot(3, 1, 1)
plt.plot(times, f0, label="f0")
plt.subplot(3, 1, 2)
plt.plot(times, voiced_flag, label="vflag")
plt.subplot(3, 1, 3)
plt.plot(times, voiced_probs, label="vprobs")
plt.gca().xaxis.set_major_locator(MultipleLocator(0.5))
plt.show()
