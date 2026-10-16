# Announcer tools

The game's recorded play-by-play voice is made offline with [Piper](https://github.com/rhasspy/piper) text to speech.
Every call is a short MP3 clip. The clips are packed end to end into `models/calls.mp3`, and `models/calls.json`
maps each clip id to `[byteOffset, byteLength]`. The game decodes clips on demand and plays them back to back
(see `VOX` and `cmtSay` in the game), so "Up next," + "Novak" or "number 17" are separate clips.

## Files

- `script.py`: the script. Fixed calls (with a style: `x` excited, `l` and `n` slower), plus clips generated per team
  (`t_full_`, `t_goal_`, `t_win_`), per roster name (`n_NAME`) and per jersey number (`num_1` to `num_99`).
  `SAY` and `NAMESAY` hold pronunciations.
- `gen.py`: synthesizes every clip, trims silence, applies a light broadcast EQ, compression and room, and writes
  `calls.mp3` and `calls.json`.
- `audition.py`: builds one short sample MP3 per candidate voice, for picking a voice.
- `merge.py`: appends newly generated clips onto an existing `calls.mp3` and `calls.json`, so adding a few calls doesn't mean rebuilding them all.

## Setup

    python3 -m pip install piper-tts numpy      # tested with piper-tts 1.8.0; needs ffmpeg on the PATH
    curl -LO https://github.com/rhasspy/piper/releases/download/v0.0.2/voice-en-us-ryan-high.tar.gz
    mkdir ryan && tar -xzf voice-en-us-ryan-high.tar.gz -C ryan

## Build

    python3 gen.py ryan/en-us-ryan-high.onnx -1 out          # -1 for a single-speaker voice
    cp out/calls.mp3 out/calls.json ../../models/

For a multi-speaker voice (for example `en-us-libritts-high`, 904 speakers) pass the speaker id instead of -1.
To try voices first:

    python3 audition.py samples ryan:ryan/en-us-ryan-high.onnx:-1 lt42:libritts/en-us-libritts-high.onnx:42

## Adding a call

Add the clip to `FIXED` in `script.py`, then either rebuild everything or generate only the new ids and merge them in:

    python3 gen.py ryan/en-us-ryan-high.onnx -1 new c_settle g_laser
    python3 merge.py ../../models new merged && cp merged/calls.* ../../models/

Then use its id in the game with `L("caption text","clip_id")`, usually inside `pickV([...])`, which picks among versions of a call without repeating the last one.
A line whose clips are missing still shows its caption; it just isn't spoken.
