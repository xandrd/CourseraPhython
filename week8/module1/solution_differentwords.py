import sys
print(
    len(
        set(
            ' '.join(
                ''.join(
                    sys.stdin.readlines()
                ).split('\n')
            ).split()
        )
    )
)
