# Validation
On September 20, 2026, Toritte confirmed selection of four different exosuits and subsequently reported all four working after deployment. Screenshots show their HUD entries, delivery and all four on the ground. Entering, moving, firing and exiting are supported by the tester's report, not independently established by the screenshots.

The tested original ZIP SHA-256 was `4d2dc5426847d56b3e052b90f52e71beae0b6be710a89be85b3c82fe59ae7129`. The release preparation verifies the addon archive matches that ZIP byte for byte. Added artwork, manifests and installation text change the outer ZIP hash. The current archive hash is recorded in config/supported-build.json.

Historical offline checks covered patch preconditions and lifecycle failure handling. This public source package includes packaging tests; it does not include private memory dumps or capture-dependent historical tests. Packaging tests are not gameplay tests.

The new ZIP has not yet been imported and deployed through a manager. Multiplayer, subsequent missions/reconnects, extended sessions, all other mods and future game builds remain unverified. No generic GameGuard compatibility claim is made.
