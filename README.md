# Unit 2 Discussion: Stacks and Queues

## Overview and completed work

I implemented a list-backed Stack and a collections.deque-backed Queue. I completed all ten operation TODOs, retained every original TODO prompt, and replaced the placeholder demonstration output. I placed both demonstrations inside main so importing the module did not run the demonstrations.

## Design and real-world scenarios

I modeled text-editor undo history with a stack. push appended an action at the end of the list; pop removed that same end. This produced LIFO behavior because the latest edit was undone first. peek inspected the newest action without removing it.

I modeled support-desk tickets with a queue. enqueue appended a request at the back; dequeue used popleft to remove the oldest request. This produced FIFO behavior and preserved arrival order. front inspected the oldest ticket without removing it. I chose deque so removing the first ticket did not require shifting all remaining items.

## Empty structures and boundary cases

I raised descriptive IndexError exceptions for pop and peek on an empty stack and dequeue and front on an empty queue. The demonstration caught each exception and printed an explanation, allowing execution to continue. I also removed the only item from each structure and verified that is_empty returned True. The structures accepted general Python values, including None; explicit exceptions kept an empty structure distinguishable from a stored None value.

## Verification

I ran the original starter and then the completed program. I checked four-item LIFO and FIFO order, non-removing inspection, all four empty-operation errors, single-item transitions, reuse after emptying, duplicate values, stored None values, and mixed additions and removals. The additional automated checks passed. I verified that all original TODO prompts remained present.

## Time and memory analysis

I used O(n) storage for n stored references in each structure. Memory grew as items were added, with additional container capacity and object overhead. The objects referenced by the containers could require additional memory. Python lists could retain spare capacity after removals, so allocated memory did not necessarily decrease immediately. Stack push was amortized O(1); stack pop and peek were O(1). Queue enqueue, dequeue, and front were O(1). Neither structure imposed a fixed application capacity; available memory limited growth.

## Running the program

Run `python unit2_discussion.py` from this folder. No external packages were required.
