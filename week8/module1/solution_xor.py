#  xor: s (a | b)& ~(a & b)
print(
    *map(
        int,
        map(
            lambda x: (x[0] or x[1]) and (not (x[0] and x[1])),
            zip(
                map(
                    bool,
                    map(
                        int,
                        input().split()
                    )
                ),
                map(
                    bool,
                    map(
                        int,
                        input().split()
                    )
                )
            )
        )
    )
)
