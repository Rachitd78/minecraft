def on_on_score():
    info.set_score(info.high_score())
    controller.configure_repeat_event_defaults(500, 30)
    for index in range(4):
        game.reset()
info.on_score(100, on_on_score)

game.set_game_over_message(False, "GAME OVER!")
game.set_game_over_message(True, "You won")
scene.set_background_color(0)
game.set_game_over_scoring_type(game.ScoringType.HIGH_SCORE)