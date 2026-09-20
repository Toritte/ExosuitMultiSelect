# Technical walkthrough
The separately installed Bingus Shared Loader discovers the declaration `mods/lequla/exosuit_multiselect`.

The Lua lifecycle waits for the existing update callback, validates the loaded executable and game DLL hashes, then calls the data patch. It checks a 224-byte selection-code signature, the settings buffer and record pointers, and a baseline of 147 stratagem records. The target records are IDs 26, 10, 89 and 86. For each target it clears bit 20 of the flags at record offset `0x104`, writing the corresponding byte at `0x106`.

The data must already be writable private memory. The code does not change executable instructions or memory protection. Failed application attempts roll back owned edits when their ownership checks allow it. See the Lua sources for exact preconditions and rollback handling.

This changes a shared exosuit classification flag; effects are not inherently confined to selection. It does not add extra stratagem slots or remove restrictions from arbitrary other stratagems.

Package construction wraps the plaintext Lua with a length/version envelope and stores one addon resource in `9ba626afa44a3aa3.patch_0`, with empty stream/GPU sidecars. No loader startup resource is included. The build refuses to package gameplay bytes differing from the configured release archive.
