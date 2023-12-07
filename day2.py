from pprint import pprint as pp

BAG = {"red": 12, "green": 13, "blue": 14}

test_inputs_pt1 = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\nGame 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue\nGame 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red\nGame 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red\nGame 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

with open("inputs/day2.txt", "r") as f:
    ips = f.read().splitlines()

test_ips = test_inputs_pt1.splitlines()

games = [ip.split(": ")[1] for ip in ips]
rounds = [game.split("; ") for game in games]
hands = [[colour.split(", ") for colour in colours] for colours in rounds]

for idx_game, game in enumerate(hands):
    for idx_round, round in enumerate(hands[idx_game]):
        for idx_colours, colours in enumerate(hands[idx_game][idx_round]):
            for idx_colour, colour in enumerate(hands[idx_game][idx_round][idx_colours]):
                pass
# pp(ip_dict)
# {
#     1: "3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
#     2: "1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
#     3: "8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
#     4: "1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
#     5: "6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
# }

# for key, val in ip_dict.items():
#     for idx, v in enumerate(val.split("; ")):
#         sv_dict = {idx+1: {"red": 0, "blue": 0, "green": 0}}
#         for sv in v.split(", "):
#             if "blue" in sv.split():
#                 sv_dict[idx + 1]["blue"] = int(sv.split()[0])
#             elif "red" in sv.split():
#                 sv_dict[idx + 1]["red"] = int(sv.split()[0])
#             elif "green" in sv.split():
#                 sv_dict[idx + 1]["green"] = int(sv.split()[0])
#         ip_dict.update()

# pp(ip_dict)
games = 0
# for key, val in ip_dict.items():
#     if (
#         all(
#             [val[1]["blue"] < BAG["blue"]
#             and val[2]["blue"] < BAG["blue"]
#             and val[3]["blue"] < BAG["blue"]]
#         )
#         and all(
#             [val[1]["red"] < BAG["red"]
#             and val[2]["red"] < BAG["red"]
#             and val[3]["red"] < BAG["red"]]
#         )
#         and all(
#             [val[1]["green"] < BAG["green"]
#             and val[2]["green"] < BAG["green"]
#             and val[3]["green"] < BAG["green"]]
#         )
#     ):
#         games += key

print(games)
# {
#     1: {
#         1: {"blue": 3, "green": 0, "red": 4},
#         2: {"blue": 6, "green": 2, "red": 1},
#         3: {"blue": 0, "green": 2, "red": 0},
#     },
#     2: {
#         1: {"blue": 1, "green": 2, "red": 0},
#         2: {"blue": 4, "green": 3, "red": 1},
#         3: {"blue": 1, "green": 1, "red": 0},
#     },
#     3: {
#         1: {"blue": 6, "green": 8, "red": 20},
#         2: {"blue": 5, "green": 13, "red": 4},
#         3: {"blue": 0, "green": 5, "red": 1},
#     },
#     4: {
#         1: {"blue": 6, "green": 1, "red": 3},
#         2: {"blue": 0, "green": 3, "red": 6},
#         3: {"blue": 15, "green": 3, "red": 14},
#     },
#     5: {
#         1: {"blue": 1, "green": 3, "red": 6},
#         2: {"blue": 2, "green": 2, "red": 1},
#         3: {"blue": 0, "green": 0, "red": 0},
#     },
# }
