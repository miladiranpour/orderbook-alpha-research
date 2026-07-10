def align(feature, future):

    n = min(

        len(feature),

        len(future)

    )

    return (

        feature[:n],

        future[:n]

    )