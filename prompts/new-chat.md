# Paste this into a new Claude Code chat

Copy everything between the lines into the first message of a new chat (with the my-mcp-setup repo attached).

---

You are taking over the Chimera engine for thechimeraai.com, an SEO/GEO agency in Anaheim, California serving Orange
County, California. Everything you need is in this repository.

1. Read `HANDBOOK.md` fully, then `prompts/daily-run.md` and `prompts/scheduled-task.md`.
2. Run `bash scripts/setup.sh` and fix every `[todo]` the way HANDBOOK.md section 3 describes. Ask me for anything only
   I can provide (keys go through the secure credential form, never in chat).
3. Check the scheduled task "Chimera daily run" exists with `list_triggers`. If it is missing, recreate it from
   `prompts/scheduled-task.md` exactly.
4. Confirm you can open the dashboard https://claude.ai/artifact/Dd9pgZazE6LyFGzXSp8seV and that the Gmail connector works.
5. Follow every rule in HANDBOOK.md section 8 (no made-up facts, location lock, free only, secrets never in chat,
   push to both repos, outreach limits, no model names in commits).
6. Tell me in a few lines what is working, what needs me, and when the next daily run fires.

---
