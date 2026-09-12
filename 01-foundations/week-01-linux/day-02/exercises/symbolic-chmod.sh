#!/bin/bash

# This script demonstrates the use of symbolic chmod commands to modify file permissions.
## Exercise

# 1. Create `exercise.sh`.
# 2. Make it executable only for the owner.
# 3. Add read permission for the group.
# 4. Remove read permission from others.

# Try using symbolic commands rather than a single numeric command.

# Solution:

touch exercise.sh
chmod u+x exercise.sh  # Make it executable only for the owner

chmod g+r exercise.sh  # Add read permission for the group
chmod o-r exercise.sh  # Remove read permission from others

