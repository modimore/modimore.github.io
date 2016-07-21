---
gh_repo_name: Discord-Dice-Bot
title: "Discord Dice Bot"
languages: [ Python ]
technologies: [ RegEx ]
sort_index: 2
---
A script to run a dice-rolling bot on a [Discord] chat server.

The primary module here is designed to parse a small dice-specification language and generate random die rolls.
The language is based on the needs and reference conventions of tabletop roleplayers, stemming from various versions D&D core rulebooks but usable for any comparable dice-based RPG.

A small python script then creates a chat client that puts messages through this parser and says rolls results back to the original channel. This is achieved through [discord.py], the Discord API for Python.

[discord]: https://discordapp.com
[discord.py]: https://github.com/Rapptz/discord.py
