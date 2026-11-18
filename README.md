# Instant Respawn

<img src="art/logo-512.png" width="160" align="right" alt="Instant Respawn icon">

A tiny client-side Fabric mod for Minecraft **1.21.11** and **26.1 – 26.3**.

In vanilla, the **Respawn** button on the death screen is greyed out for one second
(20 ticks) after you die. Instant Respawn makes it clickable the moment the death screen opens.

| | Respawn button clickable after |
|---|---|
| Vanilla | ~1000 ms |
| With Instant Respawn | 0 ms (first frame) |

- Client-side only. Works on any server, no server mod needed.
- No config, no dependencies other than Fabric Loader (Fabric API is not required).
- Hardcore's "Title Screen" button is enabled right away too, same as vanilla after the delay.

## Install

1. Install [Fabric Loader](https://fabricmc.net/use/) for your Minecraft version.
2. Drop the matching jar into your `mods` folder:

| Minecraft | Jar |
|---|---|
| 1.21.11 | `instant-respawn-<version>+1.21.11.jar` |
| 26.1 – 26.3 | `instant-respawn-<version>+26.x.jar` |

## Build

```sh
./gradlew build            # 1.21.11 (JDK 21)  -> build/libs
cd mc26 && ./gradlew build # 26.1 - 26.3 (JDK 25) -> mc26/build/libs
```

From 26.1 Minecraft is no longer obfuscated, so the 26.x build in `mc26/` uses Mojang's names directly
(the field is called `delayTicker` there instead of `ticksSinceDeath`).

## How it works

`DeathScreen.init()` disables the buttons and `DeathScreen.tick()` turns them back on when
`ticksSinceDeath` reaches 20. A mixin at the end of `init()` sets `ticksSinceDeath` to 20 and
enables the buttons immediately.

## License

MIT
