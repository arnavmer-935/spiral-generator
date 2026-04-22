import argparse

def parse_args():
    parser = argparse.ArgumentParser(prog="drawing",
                                     description="A parametric generative art tool. Tweak different parameters to "
                                                 "generate varying geometric art.")

    parser.add_argument("--length-limit", type=float, default=120,
                        help="Maximum penstroke length before drawing stops (default: 120).")

    parser.add_argument("--length", type=float, default=0.00001,
                        help="Starting length of penstrokes (default: 0.00001).")

    parser.add_argument("--sample-size", type=int, default=3,
                        help="Sample size of color palette for color bands, 1-10 (default: 3).")

    parser.add_argument("--thickness", type=float, default=0,
                        help="Initial penstroke thickness (default: 0).")

    parser.add_argument("--initial-heading", type=float, default=0,
                        help="Starting direction of movement, in degrees (default: 0).")

    parser.add_argument("--rotation-angle", type=float, default=20,
                        help="Fixed rotation angle at each turn (default: 67).")

    parser.add_argument("--growth-rate", type=float, default=0.1,
                        help="How fast stroke length and thickness grow (default: 0.1)")

    return parser.parse_args()


