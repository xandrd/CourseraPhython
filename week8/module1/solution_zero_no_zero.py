import sys
print(
    any(
        map(
            lambda x: x == 0,
            map(
                int,
                sys.stdin.readlines()
            )
        )
    )
)
