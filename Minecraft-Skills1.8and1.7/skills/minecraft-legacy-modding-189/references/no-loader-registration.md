# When there's no loader lifecycle to register against

Plain Forge gives you `GameRegistry.registerItem(...)`,
`GameRegistry.registerBlock(...)` etc., called during `FMLInitEvent`.
When you're targeting an environment with no FML lifecycle at all (Lunar
Client's bundled lane — see `minecraft-lunar-client`), none of that
exists. You're working directly against vanilla 1.8.9's own registries:

- `Block.blockRegistry`
- `Item.itemRegistry`

Registering directly into these at the right point in the vanilla
bootstrap (not inside any Forge-style lifecycle hook, since none exists)
is the vanilla-style equivalent. The right injection point for "register
my custom block/item before the game needs it" has to be found via Mixin,
targeting wherever vanilla's own bootstrap populates these registries —
confirm the exact method via RECON (see `minecraft-lunar-client`'s
obf-and-retrace.md) rather than guessing a vanilla 1.8.9 method name from
memory, since the class is obfuscated in the actual shipped jar.

## Side-effects to watch for

Forge's registry system handles ID allocation, network sync for multi
player, and NBT persistence consistency across registry changes for you.
Registering directly into vanilla's registries bypasses all of that — if
your mod needs to work on a server too (not just visually/client-side),
you're responsible for making sure IDs don't collide and persistence
round-trips correctly. For a purely client-side visual/QoL mod (the more
common Lunar use case), this mostly doesn't matter, but say explicitly
which case you're in before assuming it's safe to skip.
