# Crowd chant tools

The arena chants ("Let's go, Grizzlies!") are recorded offline with [Piper](https://github.com/rhasspy/piper) text to speech,
one clip per club, in `models/chants.mp3` with a byte index in `models/chants.json` (`"ch_ABBR": [byteOffset, byteLength]`,
the same format as `calls.mp3`). Each clip is sixteen LibriTTS voices saying the line together, each pitched and stretched a
little differently and a few milliseconds apart, with an arena echo on the mix.

The game adds the rest itself (see `CRW` in the game): the "clap, clap, clap-clap-clap" after each chant on the beat,
applause after goals and saves, and the roar of the wave panned to wherever it is in the bowl. Every clip lasts just under
four beats at `BEAT=.5` seconds so the claps land in time.

## Setup

    python3 -m pip install piper-tts numpy      # tested with piper-tts 1.8.0; needs ffmpeg on the PATH
    curl -LO https://github.com/rhasspy/piper/releases/download/v0.0.2/voice-en-us-libritts-high.tar.gz
    mkdir libritts && tar -xzf voice-en-us-libritts-high.tar.gz -C libritts

## Build

    python3 chants.py libritts/en-us-libritts-high.onnx nicks.json out
    cp out/chants.mp3 out/chants.json ../../models/

`nicks.json` lists each club's abbreviation and the nickname the crowd shouts. Name abbreviations after `out` to rebuild only
those clubs (for example after renaming one), then merge the new entries into the index by hand or rebuild them all.
