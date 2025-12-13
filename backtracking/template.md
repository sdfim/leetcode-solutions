# Backtracking Template

## Generic pattern

function backtrack(state, path):
if is_solution(state):
record(path)
return

    for choice in choices(state):
        if not valid(choice, state):
            continue

        apply(choice)
        backtrack(new_state, path + choice)
        undo(choice)

---

## Key ideas
- Always restore state (undo)
- Pass minimal state
- Prune as early as possible
- Prefer passing indices over slicing arrays

---

## Common parameters
- index / start
- used[] / visited[]
- remaining sum
- bitmask
