# Tmux

Tmux can be used to simulate multiple terminal sessions within a single terminal session.
```
sudo apt install tmux
```
Run a prompt in the background with
```
tmux new -s <name of your temux environment> <your prompt>
```
You can use a terminal like bash as `<your prompt>` for a terminal that runs in the background
Configure gateway environment

If you are in a temux environment you can return to the main environment without ending the task by typing
` Ctrl+B D `

Return to your temux environment with:
```
tmux attach -t <name of your temux environment>
```

## Scrolling

You can scroll up and down by using `Ctrl+B [` and than using the arrow keys to navigate up and down. Use `escape` to stop scrolling.