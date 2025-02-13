import writer as wf

wf.Config.feature_flags = ["workflows", "custom_block_icons"]

def confirm_recording(state):
    state["show_next_steps"] = True


initial_state = wf.init_state({
    "text": "hello",
    "show_next_steps": False
})
