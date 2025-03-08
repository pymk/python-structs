# Python Structs

Playing around with Python dataclasses.

## Usage

```python
House(
    name="Stark",
    seat="Winterfell",
    sigil="direwolf",
    words="Winter is coming",
    people=[Person("Ned"), Person("Catelyn")],
)
```

## Example

```
> uv run main.py

House Stark of Winterfell with direwolf sigil and 'Winter is coming' words has 8 members.
 - Eddard Stark
 - Catelyn Tully
 - Robb Stark
 - Sansa Stark
 - Arya Stark
 - Bran Stark
 - Rickon Stark
 - Jon Snow
```
