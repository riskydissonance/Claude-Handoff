# Claude Handoff

Copy these files into ~/.claude to use it for all claude code sessions.

You can refer to the individual files for detail, but essentially:

* Your current chat model is used as an orchestrator and architect, recommendation is Fable/Opus/best model available.
* A haiku `explorer` subagent is created and used for data gathering.
* A sonnet `worker` subagent is used to perform edits.
* The current main model is spun up as an `adversary` subagent which is used to perform adversarial input and to 'red team' design that is deemed critical.
* A hook is used to prevent the main agent from making edits to save tokens. Changes are batched to save on agent creation costs.
* Claude is asked to clarify early to prevent wasted work.
* Claude is asked to compress context and prompt the user after chat follows several iterations to prevent context balooning.

## Verify it's working

* Restart claude code and then when you are using it it should list which agent is being used for actions at the bottom (main/worker/explorer).
