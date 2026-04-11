# January 7, 2022 Label Precision Notes

## Purpose

This note exists to prevent a specific and dangerous modeling mistake:
- collapsing **attempted profile formations** into **completed profile labels**
- or confusing **weekly annotations** with **day-level structure labels**

## Edward's correction to preserve

For the week ending **January 7, 2022**:

### Tuesday is **not** a true Bikini
Edward's clarification:
- on the weekly chart, Tuesday is labeled a **`bikini failure`**
- meaning:
  - the day **tries** to create a clean TPO high / a structure that could become a Bikini
  - but it later **breaks the low**
  - and becomes a **different day structure**, specifically a **late day trend**

So the machine must not do this:
- see early bilateral tails or center density
- then conclude `Tuesday = Bikini`

That would be wrong.

The correct interpretation is:
- Tuesday may be a **Bikini candidate** or **attempted Bikini formation** early in the session
- but it **fails** and should be labeled as a different final structure once the low breaks and the day transitions

### Friday January 7, 2022 is the true Bikini
Edward's clarification:
- **Friday the 7th** is the actual **Bikini** in this weekly sequence

That means:
- our detector work must distinguish between:
  - `bikini_candidate`
  - `bikini_failure`
  - `true_bikini`

## Modeling implication

This is critical:

A day label cannot be assigned only from the final profile silhouette if the real trading meaning depends on:
- whether the shape was sustained
- whether the opposite side later broke
- whether the day transitioned into a different structure late

So for profile-based labels, the machine likely needs **both**:
1. final profile geometry
2. intraday structural sequence

Not just one.

## Practical rule

When evaluating terms like `Bikini`, the system should ask:
1. did a Bikini-like shape appear?
2. did it hold into the end-state of the session?
3. did the day later break structure and become something else?

If the shape appears and then fails, the machine should prefer:
- `bikini_failure`

not:
- `true_bikini`

## Immediate takeaway

Our current crude detector is too blunt because it is treating end-state geometry too loosely and ignoring sequence.

The next detector design needs to separate:
- attempted shape formation
- failed shape formation
- completed shape formation
