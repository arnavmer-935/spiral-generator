import turtle
from random import sample, choice, uniform, randint, random
from time import perf_counter

colors = [
    'red', 'orange', 'gold', 'yellow',
    'lime', 'green', 'teal',
    'cyan', 'blue', 'indigo',
    'violet', 'magenta', 'pink'
]

t = turtle.Turtle()
screen = turtle.Screen()

def setup():
    screen.bgcolor('black')
    t.speed(0)
    t.ht()

def validate_params(
        length_limit,
        length,
        sample_size,
        thickness,
        rotation_angle,
        gradient
):
    if length_limit <= 0:
        raise ValueError("length limit must be positive")

    if length <= 0:
        raise ValueError("length must be positive")

    if length >= length_limit:
        raise ValueError("length must be less than length limit")

    if not (1 <= sample_size <= len(colors)):
        raise ValueError("sample size must be between 1 and 10")

    if thickness < 0:
        raise ValueError("thickness must be non-negative")

    if rotation_angle <= 0:
        raise ValueError("rotation angle must be positive")

    if gradient <= 0:
        raise ValueError("gradient must be positive")

def draw_custom_spiral(
        length_limit: float = 120,
        length: float = 0.00001,
        sample_size: int = 3,
        thickness: float = 0,
        initial_heading: float = 0,
        rotation_angle: float = 20,
        growth_rate: float = 0.1
):
        validate_params(
            length_limit,
            length,
            sample_size,
            thickness,
            rotation_angle,
            growth_rate
        )

        t.setheading(initial_heading)
        distance_drawn = 0
        turn_count = 0
        steps_before_shuffle = 10

        while length <= length_limit:

            if not turn_count % steps_before_shuffle:
                palette = sample(colors, sample_size)
                t.color(choice(palette))
            else:
                t.color(choice(colors))

            t.pensize(thickness)
            t.forward(length)

            distance_drawn += length
            t.left(rotation_angle + initial_heading)
            turn_count += 1
            length = length + growth_rate * thickness
            thickness += growth_rate

        return distance_drawn, turn_count

def _get_random_args() -> dict[str, float]:
    r_limit = uniform(200, 1001)
    r_start = uniform(0.0000001, 1.1)
    r_sample_size = randint(1,10)
    r_thickness = uniform(0, 2)
    r_initial_heading = uniform(0,360)
    r_rotation_angle = uniform(0,360)
    r_growth_rate = random()

    keys = ["Stroke Length Limit", "Initial Stroke Size", "Palette Sample Size", "Initial Thickness", "Initial Heading",
            "Rotation Angle", "Growth Rate"]

    vals = [r_limit, r_start, r_sample_size, r_thickness, r_initial_heading, r_rotation_angle, r_growth_rate]

    return dict(zip(keys, vals))

def main():
    try:
        setup()
        args = _get_random_args()
        print("---------RANDOMLY CHOSEN PARAMETERS---------")

        for param, value in args.items():
            print(f"{param}: {value:.4f}")

        print()
        start = perf_counter()
        distance, n_turns = draw_custom_spiral(*args.values()) #sample run
        end = perf_counter()
        time_taken = end - start

        print("-------------METRICS----------------")
        print(f"Distance travelled: {distance:.4f} pixels")
        print(f"Number of turns during drawing: {n_turns}")
        print(f"Average drawing speed: {(distance / time_taken):.4f} px/s")

        screen.mainloop()

    except ValueError as e:
        print(e)

    except Exception:
        print("Drawing was terminated.")

if __name__ == "__main__":
    main()