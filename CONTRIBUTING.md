# Build from source
Use Python 3.10 or newer. No game installation, third-party Python packages or downloaded loader source is required to build this repository.

From the repository root:
```sh
python -m unittest discover -s tests -v
python scripts/build.py
```
Output: `dist/Exosuit-MultiSelect-v0.2.zip` and `dist/SHA256SUMS.txt`. Installable releases contain this mod only. Obtain the loader separately.

The builder reconstructs the archive from the three Lua sources and compact supported-build configuration, then checks it against the gameplay-tested archive SHA-256. It generates both manifests and verifies all listed files. Changes to gameplay sources intentionally fail this check until separately reviewed and validated; do not replace the expected hash just to silence the check.

Release metadata, installation text and artwork may be repackaged without changing gameplay bytes. Re-test manager import after packaging changes. ZIP bytes are repeatable on the same Python/zlib environment; compression versions may affect the ZIP hash while member hashes remain the same.

The automated package tests do not emulate the game or prove future gameplay compatibility. Historical gameplay evidence is summarized in docs/VALIDATION.md. Do not upload game executables, full memory captures, personal logs or the old v0.1 package. Check THIRD_PARTY.md before public redistribution.
