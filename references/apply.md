# Apply

"Let's try it." The user accepted a call and wants help implementing it. Apply is entered only when the user
asks to implement or try something. Never enter it from a USE IT verdict on your own, and never from Scout.

Apply stays conservative: the goal is the **smallest setup that can show the benefit**, not the full
environment.

## 1. Confirm what's being applied

One short message:

- The call it implements (technology and first step), from this conversation. If there wasn't one, run a
  quick Advise first. A two-line call is enough when the user is sure.
- Where it goes: **project scope** by default, in the current project, or a sandbox folder or branch if the
  call said sandbox.
- What "done" means: the `Measure` line from the call.

## 2. Ground the install path live

Installation commands and what they create change faster than anything else. Before proposing commands,
check the card's `Lightest path` and `What a full install changes` against the canonical source
(`grounding.md`). If you can't check live, say the commands come from the snapshot of that date and may
have changed.

## 3. Write the plan, and show it before running anything

A numbered list. Each step has:

```
Step 2 — Install the Ruflo core plugin (project scope)
Runs:      <exact command>
Changes:   <files and folders it creates or edits; "nothing outside this project">
Undo:      <exact command or what to delete>
Approval:  needed
```

Rules for the plan:

- **Checkpoint first.** If the project is a git repo with uncommitted changes, the first step suggests a
  commit or a branch so everything after it can be undone. Don't commit for the user without asking.
- **Smallest path first.** Prefer a plugin or library over a full CLI initialization. A full Ruflo
  initialization (or anything that writes `CLAUDE.md`, registers MCP servers, adds hooks or starts
  background processes) is a separate, later step, and only if the trial shows it's needed.
- **Project scope, explicitly.** `claude plugin install` and `claude plugin marketplace add` default to
  **user** scope (every project); `claude mcp add` defaults to **local** (this project, this computer only).
  Pass `--scope project` (shared with the repo) or `--scope local` explicitly, and use user scope only when
  the user asked for every project. Run `claude plugin details <plugin>` first so the user sees what a plugin
  adds (hooks, MCP servers) before it's installed.
- **Ruflo's init touches global config by default.** It appends to `~/.claude/CLAUDE.md` unless given
  `--no-global`. Always pass `--no-global` unless the user explicitly wants the global change, and confirm the
  flag still exists first (`ruflo-init-source` in `sources.json`).
- **Existing files win.** If a step would overwrite `CLAUDE.md`, `.claude/settings.json`, `.mcp.json` or
  any existing config, stop and show the conflict. Offer to merge by hand, or to write the new config to a
  side file for review. Never delete existing configuration.
- **Global changes are separate.** Anything outside the project (`~/.claude/`, a global `npm install -g`,
  a shell profile, a system service) gets its own step, labelled **global**, with its own approval.
- **Adapters first.** When the change touches the user's code, the first code step is the interface
  (`decision-policy.md`, section 7), with the existing implementation behind it still working.
- **Secrets.** If a tool needs an API key, tell the user which environment variable to set and where. Never
  ask them to paste a key into the chat, and never write one into a file.

## 4. Run with approval, one step at a time

- Ask for a yes before each step that runs a command or changes files. "Yes to all" is fine for the
  *project-scope* steps the user has just seen in the plan. Global steps still get their own yes.
- After each step, check it worked (the command's exit status, the files it should have created) and say so
  in one line. If it failed, stop, show the error, and propose a fix or a rollback. Don't push on.
- If you can't run commands in this environment, give the plan as copy-paste commands with the same
  Changes and Undo lines, and stop there.

## 5. Finish

- What's now installed and where, in a short list.
- How to undo all of it, in one block.
- The trial: what to measure, how (with a single-agent or current-stack baseline run of the same task), and
  the result that would justify going further. Going further is a new Advise call, not an automatic next
  step.
- If Shared Profiles is installed and this was for a business, append to its `notes/ruv-lite.md`: what was
  set up, and when to judge the trial.
