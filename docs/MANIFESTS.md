# Package manifests
`manifest.json` describes the mod to the manager: name, icon, identity and files to deploy. `Version: 1` is the schema version, not the mod version. `Guid` is a UUID identifying this mod; retain `9d21a1c4-8d97-4f49-980d-246cbda29a8d` across its updates. Generate a different UUID only for a distinct mod. Never copy another mod's UUID.

Top-level `IconPath` and option `Image` point to `thumbnail.png`. `Options[0].Include` contains `Addon`, so only the deployment folder is selected. The metadata and artwork remain at ZIP root.

`ExosuitMultiSelect-manifest.json` is generated provenance/integrity metadata, not a universal loader-required schema. Its name and contents are specific to this project. It records dependencies, validation scope and SHA-256 values. `files` maps every other ZIP member's relative path to its hash; the manifest excludes itself to avoid a circular hash. SHA-256 is an integrity fingerprint, not a digital signature or permission grant. `resource_sha256` covers the Lua resource including its eight-byte envelope.

Do not type or copy hashes from the hover-pack example. Run `python scripts/build.py` after changing packaging files; both manifests are regenerated consistently. The runtime's stable resource path and manager UUID are different identities, and neither should change just because the public author name changed.
