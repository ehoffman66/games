# Breakaway Checkers

An AHL hockey shootout game against the computer: best of five, then sudden death. Play single games or a full season with standings and a Calder Cup playoff bracket, or play a friend online with each of you on your own phone.

Play it at https://ehoffman66.github.io/games/breakaway-checkers/ (on a phone, Share > Add to Home Screen gives it its own icon and opens it full screen).

Everything is in `index.html` (three.js r149 from jsDelivr). `icons/` and `manifest.webmanifest` give it a home-screen icon. `models/` holds the player and goalie rigs and textures the page loads at startup; if they fail to load, the game falls back to drawn players.

Online games connect the two phones peer to peer through PeerJS (loaded from jsDelivr only when someone hosts or joins) and its free public signaling server. The host's phone runs the game; the friend's phone sends its controls and draws what the host sends back.
