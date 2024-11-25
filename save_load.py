import os.path

def save_button(sampler_buttons, step_number):
    with open("save.dat", "wt") as f:
        f.write(str(step_number) + "\n")
        for button in sampler_buttons:
            f.write(button.file_name_text + "\n")
            f.write(str(button.circle_indices) + "\n")
    return

def load_button(sampler_buttons):
    if not os.path.exists("save.dat"):
        raise FileNotFoundError("A mentési fájl nem található!")
    with open("save.dat", "rt") as f:
        row = f.readline().rstrip("\n")
        step_number = int(row)
        for button in sampler_buttons:
            row1 = f.readline().rstrip("\n")
            button.file_name_text = row1
            row2 = f.readline().strip("\n[]").split(",")
            button.circle_indices = [int(x) for x in row2 if len(x) > 0]
        return step_number