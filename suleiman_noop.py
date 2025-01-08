"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'noop_1' block
    noop_1(container=container)

    return

@phantom.playbook_block()
def loop_noop_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("loop_noop_1() called")

    loop_state = phantom.LoopState(state=loop_state_json)

    if loop_state.should_continue(container=container, results=results): # should_continue evaluates iteration/timeout/conditions
        loop_state.increment() # increments iteration count
        noop_1(container=container, loop_state_json=loop_state.to_json())

    return


@phantom.playbook_block()
def noop_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("noop_1() called")

    parameters = [{}]

    if not loop_state_json:
        # Loop state is empty. We are creating a new one from the inputs
        loop_state_json = {
            # Looping configs
            "current_iteration": 1,
            "max_iterations": 10,
            "conditions": None,
            "max_ttl": 600,
            "delay_time": 120,
        }

    # Load state from the JSON passed to it
    loop_state = phantom.LoopState(state=loop_state_json)

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="community/noop", parameters=parameters, name="noop_1", callback=loop_noop_1, loop_state=loop_state.to_json())

    return


@phantom.playbook_block()
def on_finish(container, summary):
    phantom.debug("on_finish() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    return