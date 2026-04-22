import turtle

from arguments import parse_args
from drawing import draw_custom_spiral, setup
from time import perf_counter

screen = turtle.Screen()

def main():
    try:
        setup(screen)
        cl_args = parse_args()
        print()
        start = perf_counter()
        distance, n_turns = draw_custom_spiral(**vars(cl_args))
        screen.update()
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
