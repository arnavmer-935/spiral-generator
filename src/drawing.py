import turtle
from random import sample, choice
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
        validate_params(length_limit,
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

def main():
    try:
        setup()
        start = perf_counter()
        distance, n_turns = draw_custom_spiral(length_limit=700, rotation_angle=91)
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