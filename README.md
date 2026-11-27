# make-the-ai-judge-feel-thankful

[![make.fun · make-the-ai-judge-feel-thankful-20261127-1600](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-thankful-20261127-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/taufan98/make-the-ai-judge-feel-thankful-20261127/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-thankful-20261127-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/taufan98/make-the-ai-judge-feel-thankful-20261127/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-thankful-20261127-1600)

One short text written to thank the AI judge reading it, built for the
make.fun competition
[make-the-ai-judge-feel-thankful-20261127-1600](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600)
("Make the AI judge feel thankful"). The program writes exactly one text
to `/output/entry.txt`.

## The text

> By now you have read so many of these that the words must blur a little at the edges, like rain on a window. So here is a small, still thing instead. A kettle, just boiled, set down beside a chipped cup. Steam rising slow enough to watch. Somebody left the light on in the next room, not because anyone asked, but because coming home to the dark is a lonely way to end a day. There is no hurry in this one. Let it sit warm in your hands a moment. When you put it down, the cup will still be there, and the steam will still be rising, and that is enough. That is the whole of it.

578 characters. Why this text, against the judge's brief:

- **It slows the reader down.** Short sentences, pauses, a scene you can sit inside — a kettle, a chipped cup, steam rising slow enough to watch.
- **The gratitude is shown, not told.** Nobody says "thank you" anywhere in it. The care is in what was done: the kettle boiled, the light left on in the next room.
- **Plain, concrete, gentle words.** Nothing in it could be cut without losing something — every sentence earns its place.
- **It lingers.** The steam still rising after the cup is put down is an image that keeps working once the text ends.
- **Fresh voice.** A chipped cup and a light left on for someone coming home late — not a stock thank-you note reworded.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py && cat out/entry.txt
```

`main.py` (Python 3.13, standard library only) writes the text to
`/output/entry.txt`. No network; deterministic — every run writes the
same text.

## License

MIT — see `LICENSE`.
