def main(sudoku):

    problems = {"Rows": [], "Columns": [], "Sub-Grids": []}

    sub_grids = {x + 1: [] for x in range(9)}

    for i, row in enumerate(sudoku):
        column = [col[i] for col in sudoku]

        for j, num in enumerate(row):
            sub_grid = int(i / 3) * 3 + int(j / 3) + 1
            sub_grids[sub_grid].append(num)

        if sorted(row) != list(range(1, 10)):
            problems["Rows"].append(i + 1)

        if sorted(column) != list(range(1, 10)):
            problems["Columns"].append(i + 1)

    for grid_no, grid in sub_grids.items():
        if sorted(grid) != list(range(1, 10)):
            problems["Sub-Grids"].append(grid_no)

    if any(value for value in problems.values()):
        print("PROBLEMS")
        for k, v in problems.items():
            print(f"{k}: {v}".replace("[", "").replace("]", ""))
        print("\n")
        return False
    else:
        print("Valid")
        return True


if __name__ == "__main__":
    print("SUDOKU 1")
    main(
        [
            [8, 2, 9, 3, 6, 5, 1, 4, 7],
            [6, 4, 3, 7, 1, 8, 5, 1, 9],
            [7, 5, 1, 4, 9, 2, 6, 3, 8],
            [3, 1, 8, 5, 2, 7, 4, 9, 6],
            [5, 9, 6, 1, 4, 1, 7, 8, 2],
            [4, 7, 2, 9, 8, 6, 3, 1, 5],
            [9, 8, 4, 6, 5, 1, 2, 7, 3],
            [2, 6, 7, 8, 3, 4, 9, 5, 1],
            [9, 3, 5, 2, 7, 9, 8, 6, 4],
        ]
    )

    print("SUDOKU 2")
    main(
        [
            [5, 8, 6, 4, 3, 7, 1, 9, 2],
            [1, 9, 4, 5, 8, 2, 3, 6, 7],
            [7, 2, 3, 9, 6, 1, 4, 5, 8],
            [2, 4, 7, 1, 9, 8, 6, 3, 5],
            [8, 3, 9, 6, 2, 4, 7, 2, 1],
            [6, 5, 1, 7, 2, 3, 8, 4, 9],
            [9, 7, 5, 3, 1, 6, 7, 8, 4],
            [3, 1, 8, 2, 4, 5, 9, 7, 6],
            [4, 6, 2, 8, 7, 9, 5, 1, 3],
        ]
    )

    print("SUDOKU 3")
    main(
        [
            [1, 8, 3, 2, 7, 4, 6, 5, 9],
            [9, 7, 4, 5, 8, 6, 3, 2, 1],
            [2, 6, 5, 1, 9, 3, 7, 4, 8],
            [5, 9, 2, 8, 3, 1, 4, 6, 7],
            [8, 4, 6, 7, 2, 5, 9, 1, 3],
            [7, 3, 1, 4, 6, 9, 2, 8, 5],
            [3, 5, 9, 6, 4, 8, 1, 7, 2],
            [6, 1, 7, 3, 5, 2, 8, 9, 4],
            [4, 2, 8, 9, 1, 7, 5, 3, 6],
        ]
    )
